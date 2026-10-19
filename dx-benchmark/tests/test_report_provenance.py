"""REPORT.md must carry the provenance / environment facts needed to reproduce a run.

Covers: model provenance columns, environment rows (single- and multi-device NPUs),
glossary, classification ORT note, and a smoke pass over every tracked host.
"""
import json
import re
from pathlib import Path

import pytest

from benchmark.reporter import (
    _add_environment_section,
    _add_model_info_section,
    _add_pipeline_section,
    generate_markdown_report,
)

RESULTS = Path(__file__).resolve().parents[1] / "results"

_PCIE_RAW_4 = "\n".join(
    f" * PCIe   : Gen3 X4 [0{i}:00:00]" for i in range(1, 5))


def _model(**kw):
    base = {"name": "yolo26-n_640x640.dxnn", "task": "object_detection", "size": "n",
            "format_version": "v9", "dxcom_version": "v2.5.0-rc.1+c6ae2e3",
            "sha256": "ab" * 32}
    base.update(kw)
    return base


def _fp(**kw):
    fp = {
        "host": {"hostname": "h", "os": "Ubuntu", "kernel": "6.8", "cpu": "AMD Ryzen 5",
                 "cpu_count": 12, "ram_gb": 30.5, "cpu_governors": {"powersave": 12}},
        "npu": {"sku": "H1-Quattro", "device_count": 4, "rt_version": "v3.5.0",
                "driver": "v2.7.0", "pcie_driver": "v2.7.0", "firmware": "v2.7.6",
                "memory": "LPDDR5x 6000 Mbps, 3.92GiB", "board": "H1, Rev 0.0",
                "pcie": "Gen3 X4 [04:00:00]", "raw": _PCIE_RAW_4},
        "software": {"dx_stream": "3.2.0"},
        "tools": {},
        "tool_commit": "abc1234-dirty",
        "benchmarked_models": [_model()],
        "model_source": "https://example.com/models/2_5_0",
    }
    fp.update(kw)
    return fp


def _env(fp):
    lines = []
    _add_environment_section(lines, fp)
    return "\n".join(lines)


# ── Task 1: models table ────────────────────────────────────────────────

def test_models_table_has_provenance_columns():
    lines = []
    _add_model_info_section(lines, _fp(), [])
    out = "\n".join(lines)
    assert "| Format | DX-COM | SHA256 |" in out
    assert "v2.5.0-rc.1+c6ae2e3" in out
    assert "abababababab" in out and "abababababab" + "ab" not in out
    assert "Model source: https://example.com/models/2_5_0" in out
    assert "NPU Memory (MiB)" in out


def test_models_table_missing_provenance_is_dash():
    fp = _fp(benchmarked_models=[_model(format_version=None, dxcom_version=None, sha256=None)])
    fp.pop("model_source")
    lines = []
    _add_model_info_section(lines, fp, [])
    out = "\n".join(lines)
    assert "Model source" not in out
    row = [l for l in lines if l.startswith("| yolo26-n_640x640.dxnn")][0]
    assert row.count("| — ") >= 3


# ── Task 2: environment rows ────────────────────────────────────────────

def test_env_multi_device():
    out = _env(_fp())
    assert "| NPU Devices | 4 (H1-Quattro) |" in out
    assert "| NPU Memory (per device) |" in out
    assert "| NPU PCIe | Gen3 X4 ×4 |" in out


def test_env_single_device_has_no_per_device_note():
    fp = _fp()
    fp["npu"].update(sku="M1", device_count=1, raw=" * PCIe   : Gen3 X2 [03:00:00]",
                     pcie="Gen3 X2 [03:00:00]")
    out = _env(fp)
    assert "| NPU Devices | 1 (M1) |" in out
    assert "per device" not in out
    assert "| NPU PCIe | Gen3 X2 [03:00:00] |" in out


def test_env_host_rows():
    out = _env(_fp())
    assert "| CPU Threads | 12 |" in out
    assert "| CPU Governor | powersave |" in out
    assert "| DX-Stream | 3.2.0 |" in out
    assert "| Tool commit | abc1234-dirty |" in out
    assert "| RAM | 30.5 GiB |" in out


def test_env_mixed_governors_and_missing_cpu():
    fp = _fp()
    fp["host"].update(cpu="-", cpu_governors={"ondemand": 6, "performance": 2})
    out = _env(fp)
    assert "| CPU | N/A |" in out
    assert "| CPU Governor | ondemand ×6, performance ×2 |" in out


def test_env_host_health_only_when_present():
    assert "Host Health" not in _env(_fp())
    fp = _fp(host_health={"throttled": "throttled=0x0", "pmic_ext5v_v": 5.18714})
    assert "| Host Health | throttled=0x0, EXT5V 5.19 V |" in _env(fp)


# ── Task 3: glossary, classification note, timestamp ────────────────────

def _min_report(tmp_path, pipeline=None):
    p = tmp_path / "REPORT.md"
    generate_markdown_report(_fp(protocol={"version": "v2"}), [], pipeline or [], [], p)
    return p.read_text()


def test_report_has_glossary(tmp_path):
    out = _min_report(tmp_path)
    assert "## Glossary" in out
    for term in ("ORT", "BC", "Latency", "NPU MHz", "Max Channels"):
        assert re.search(rf"\| \*\*{re.escape(term)}", out), term


def test_generated_line_states_utc_offset(tmp_path):
    out = _min_report(tmp_path)
    assert re.search(r"\*\*Generated:\*\* .+ \(UTC[+-]\d\d:\d\d, local\)", out)


def _pipe(model, task, size, ort, fps):
    return {"model": model, "task": task, "size": size, "use_ort": ort,
            "avg_e2e_fps": fps, "frame_count": 10, "runs": 3, "requested_runs": 3,
            "status": "ok", "decoder": "vaapidecodebin"}


def test_classification_replaces_ort_comparison_with_note():
    rows = [_pipe(f"yolo26-cls-{s}_224x224.dxnn", "classification", s, o, 700.0)
            for s in "nsmlx" for o in (True, False)]
    lines = []
    _add_pipeline_section(lines, rows)
    out = "\n".join(lines)
    assert "ORT Comparison" not in out
    assert "no CPU part" in out


def test_detection_keeps_ort_comparison():
    rows = [_pipe("yolo26-n_640x640.dxnn", "object_detection", "n", o, 400.0)
            for o in (True, False)]
    lines = []
    _add_pipeline_section(lines, rows)
    assert "ORT Comparison" in "\n".join(lines)


# ── Smoke: every tracked host (H1-Quattro, M1, M1M, ...) ────────────────

def _run_dirs():
    return sorted(p.parent for p in RESULTS.glob("*/*/environment.json")
                  if (p.parent / "model_results.json").exists())


@pytest.mark.skipif(not _run_dirs(), reason="no tracked result sets")
@pytest.mark.parametrize("run_dir", _run_dirs(), ids=lambda p: f"{p.parent.name}/{p.name}")
def test_report_generates_for_every_host(run_dir, tmp_path):
    load = lambda n: json.loads((run_dir / n).read_text())
    fp = load("environment.json")
    out_path = tmp_path / "REPORT.md"
    generate_markdown_report(fp, load("model_results.json"), load("pipeline_results.json"),
                             load("multi_stream_results.json"), out_path,
                             video_infos=fp.get("video_infos"))
    out = out_path.read_text()
    for needle in ("## Glossary", "NPU Devices", "CPU Governor", "| Format | DX-COM | SHA256 |"):
        assert needle in out, needle
    n = fp["npu"].get("device_count")
    if n and n > 1:
        assert "NPU Memory (per device)" in out
    elif n == 1:
        assert "per device" not in out


# ── YOLO26 is NMS-free: the CPU part is decode + TopK (raw log: output [1,300,6] + TopK) ──

def test_cpu_part_wording_does_not_claim_nms():
    from benchmark.config import TASK_MODEL_META
    docs = Path(__file__).resolve().parents[1] / "docs"
    for task, meta in TASK_MODEL_META.items():
        assert "NMS" not in meta["ort_offload"], task
    for name in ("ANALYSIS_EN.md", "ANALYSIS_KOR.md"):
        line = next(l for l in (docs / name).read_text().splitlines() if "(CPU offload)**" in l)
        assert "NMS-free" in line or "NMS가 필요 없" in line, name
