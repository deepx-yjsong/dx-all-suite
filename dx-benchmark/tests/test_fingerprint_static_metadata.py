"""Static fingerprint metadata: model input tensor and CPU description.

Both are properties of the model file / host, so they must be collected up front on
every invocation — not as a side effect of a benchmark cell running. Capturing the
input shape from run_model logs lost 24/25 shapes on OrangePi5+ v2.5.0 after a
`--retry-failed` resume that re-ran only one model.
"""
from benchmark import env_fingerprint as ef

# Real `parse_model -m yolo26-s_640x640.dxnn -v` output (orange127, DXRT 3.5.0), trimmed.
PARSE_MODEL_V = """\
===================== Model Information ======================
 Model File Path        : yolo26-s_640x640.dxnn
 .dxnn Format Version   : v9
 DX-COM Version         : v2.5.0-rc.1+c6ae2e3

 Model Input Tensors:
  - \x1b[32mimages\x1b[0m

 Model Output Tensors:
  - output0

 Model Memory Usage:
  - Total             : 151.94 MB (159,321,088 bytes)

Task[0]: npu_0 [NPU] (model input)
  +- Inputs:
  |  +- images {shape: [1, 640, 640, 3], dtype: uint8, size: 1.17 MB (1,228,800 bytes)} [layout: PRE_IM2COL]
  +- Outputs:
     +- /model.23/one2one_cv2.0/one2one_cv2.0.2/Conv_output_0 {shape: [1, 4, 80, 80], dtype: float32, size: 100.00 KB (102,400 bytes)}
"""

# Non-verbose output (older parse_model, or -v unsupported): no tensor details.
PARSE_MODEL_PLAIN = """\
 .dxnn Format Version   : v9
 DX-COM Version         : v2.5.0-rc.1+c6ae2e3
 Model Input Tensors:
  - images
  - Total             : 151.94 MB (159,321,088 bytes)
"""

# Real `LC_ALL=C lscpu` from OrangePi 5 Plus (RK3588, big.LITTLE), trimmed.
LSCPU_RK3588 = """\
Architecture:                    aarch64
CPU(s):                          8
Vendor ID:                       ARM
Model name:                      Cortex-A55
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
CPU max MHz:                     1800.0000
Model name:                      Cortex-A76
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
CPU max MHz:                     2304.0000
L1d cache:                       384 KiB (8 instances)
"""

LSCPU_X86 = """\
Architecture:                            x86_64
Vendor ID:                               AuthenticAMD
Model name:                              AMD Ryzen 5 9600X 6-Core Processor
Core(s) per socket:                      6
Socket(s):                               1
CPU max MHz:                             5484.0000
"""

LSCPU_BIOS_DASH = """\
Architecture:                    aarch64
Vendor ID:                       ARM
  BIOS Vendor ID:                Rockchip
Model name:                      -
  BIOS Model name:               -
Core(s) per socket:              4
"""


def _stub_run(monkeypatch, text):
    calls = []

    def fake(cmd, *a, **k):
        calls.append(cmd)
        return text
    monkeypatch.setattr(ef, "_run", fake)
    return calls


def test_model_metadata_reads_input_tensor_from_verbose_parse_model(tmp_path, monkeypatch):
    f = tmp_path / "m.dxnn"
    f.write_bytes(b"x")
    calls = _stub_run(monkeypatch, PARSE_MODEL_V)
    meta = ef.collect_model_metadata(f)
    assert "-v" in calls[0]
    assert meta["input_tensor_shape"] == [1, 640, 640, 3]   # first model input, not an output
    assert meta["input_tensor_dtype"] == "UINT8"            # same casing as run_model capture
    assert meta["dxcom_version"] == "v2.5.0-rc.1+c6ae2e3"
    assert meta["total_memory_mb"] == 151.94


def test_model_metadata_without_tensor_details_omits_shape(tmp_path, monkeypatch):
    f = tmp_path / "m.dxnn"
    f.write_bytes(b"x")
    _stub_run(monkeypatch, PARSE_MODEL_PLAIN)
    meta = ef.collect_model_metadata(f)
    assert "input_tensor_shape" not in meta and "input_tensor_dtype" not in meta
    assert meta["format_version"] == "v9"


def test_lscpu_big_little_lists_every_cluster_big_first():
    assert ef._parse_lscpu_model(LSCPU_RK3588) == "Cortex-A76 x4 + Cortex-A55 x4"


def test_lscpu_single_cluster_is_unchanged():
    assert ef._parse_lscpu_model(LSCPU_X86) == "AMD Ryzen 5 9600X 6-Core Processor"


def test_lscpu_dash_and_bios_lines_are_not_a_model():
    assert ef._parse_lscpu_model(LSCPU_BIOS_DASH) is None


def test_cpu_model_falls_back_to_device_tree(tmp_path, monkeypatch):
    dt = tmp_path / "model"
    dt.write_bytes(b"Radxa ROCK 5B+\x00")
    monkeypatch.setattr(ef, "DEVICE_TREE_MODEL", str(dt))
    monkeypatch.setattr(ef, "PROC_CPUINFO", str(tmp_path / "missing"))
    monkeypatch.setattr(ef.shutil, "which", lambda name: "/usr/bin/" + name)
    _stub_run(monkeypatch, LSCPU_BIOS_DASH)
    assert ef._get_cpu_model() == "Radxa ROCK 5B+"


# Real ROCK 5B+ (Radxa kernel 6.1.43-15-rk2312) /proc/cpuinfo, trimmed to one CPU per
# cluster ×4. The vendor "cpu model" line makes lscpu 2.38 print "Model name: -" for
# every core, so the CPU must be decoded from "CPU part" instead.
def _cpuinfo_block(n, part):
    return (f"processor\t: {n}\nBogoMIPS\t: 48.00\ncpu model\t: Rockchip RK3588\n"
            f"CPU implementer\t: 0x41\nCPU architecture: 8\nCPU part\t: {part}\nCPU revision\t: 0\n\n")


CPUINFO_ROCK5B = ("".join(_cpuinfo_block(n, "0xd05") for n in range(4))
                  + "".join(_cpuinfo_block(n, "0xd0b") for n in range(4, 8))
                  + "Serial\t\t: 67a174b81a0cc2e3\n")


def _mk_max_freq(base, khz_by_cpu):
    for n, khz in khz_by_cpu.items():
        d = base / f"cpu{n}" / "cpufreq"
        d.mkdir(parents=True)
        (d / "cpuinfo_max_freq").write_text(f"{khz}\n")


def test_cpuinfo_parts_decode_big_little_big_first(tmp_path):
    _mk_max_freq(tmp_path, {**{n: 1800000 for n in range(4)}, **{n: 2352000 for n in range(4, 8)}})
    assert ef._parse_cpuinfo_model(CPUINFO_ROCK5B, str(tmp_path)) == "Cortex-A76 x4 + Cortex-A55 x4"


def test_cpuinfo_unknown_part_or_no_parts_is_none(tmp_path):
    assert ef._parse_cpuinfo_model("processor\t: 0\nCPU implementer\t: 0x41\nCPU part\t: 0xfff\n",
                                   str(tmp_path)) is None
    assert ef._parse_cpuinfo_model("processor\t: 0\nBogoMIPS\t: 48.00\n", str(tmp_path)) is None


def test_cpu_model_prefers_cpuinfo_over_device_tree(tmp_path, monkeypatch):
    dt = tmp_path / "model"
    dt.write_bytes(b"Radxa ROCK 5B+\x00")
    ci = tmp_path / "cpuinfo"
    ci.write_text(CPUINFO_ROCK5B)
    monkeypatch.setattr(ef, "DEVICE_TREE_MODEL", str(dt))
    monkeypatch.setattr(ef, "PROC_CPUINFO", str(ci))
    monkeypatch.setattr(ef, "CPU_SYSFS_BASE", str(tmp_path / "nosysfs"))
    monkeypatch.setattr(ef.shutil, "which", lambda name: "/usr/bin/" + name)
    _stub_run(monkeypatch, LSCPU_BIOS_DASH)
    assert ef._get_cpu_model() == "Cortex-A55 x4 + Cortex-A76 x4"   # no cpufreq → cpuinfo order


# ── Portability: any host must yield a sane value, never an exception ──────────

def test_parse_model_without_verbose_support_falls_back_to_plain_call(tmp_path, monkeypatch):
    f = tmp_path / "m.dxnn"
    f.write_bytes(b"x")
    calls = []

    def fake(cmd, *a, **k):
        calls.append(cmd)
        return "parse_model: unrecognized option '-v'" if "-v" in cmd else PARSE_MODEL_PLAIN
    monkeypatch.setattr(ef, "_run", fake)
    meta = ef.collect_model_metadata(f)
    assert len(calls) == 2 and "-v" not in calls[1]
    assert meta["format_version"] == "v9" and "input_tensor_shape" not in meta


def test_lscpu_merges_blocks_of_the_same_core_type():
    # RK3588 bins its two A76 clusters at different max clocks → separate lscpu blocks.
    text = ("Model name: Cortex-A55\nCore(s) per socket: 4\nSocket(s): 1\nCPU max MHz: 1800\n"
            "Model name: Cortex-A76\nCore(s) per socket: 2\nSocket(s): 1\nCPU max MHz: 2352\n"
            "Model name: Cortex-A76\nCore(s) per socket: 2\nSocket(s): 1\nCPU max MHz: 2304\n")
    assert ef._parse_lscpu_model(text) == "Cortex-A76 x4 + Cortex-A55 x4"


def test_cpuinfo_x86_and_homogeneous_arm_keep_the_bare_name(tmp_path):
    x86 = "".join(f"processor\t: {n}\nvendor_id\t: AuthenticAMD\n"
                  f"model name\t: AMD Ryzen 5 9600X 6-Core Processor\n\n" for n in range(12))
    assert ef._parse_cpuinfo_model(x86, str(tmp_path)) == "AMD Ryzen 5 9600X 6-Core Processor"
    rpi5 = "".join(_cpuinfo_block(n, "0xd0b") for n in range(4))
    assert ef._parse_cpuinfo_model(rpi5, str(tmp_path)) == "Cortex-A76"


def test_cpuinfo_non_arm_implementer_is_not_guessed(tmp_path):
    qcom = "processor\t: 0\nCPU implementer\t: 0x51\nCPU part\t: 0xd05\n\n"
    assert ef._parse_cpuinfo_model(qcom, str(tmp_path)) is None


def test_cpu_model_never_raises_and_ends_at_unknown(tmp_path, monkeypatch):
    monkeypatch.setattr(ef, "PROC_CPUINFO", str(tmp_path / "missing"))
    monkeypatch.setattr(ef, "DEVICE_TREE_MODEL", str(tmp_path / "missing"))
    monkeypatch.setattr(ef.shutil, "which", lambda name: None)
    monkeypatch.setattr(ef.platform, "processor", lambda: "")
    assert ef._get_cpu_model() == "unknown"
