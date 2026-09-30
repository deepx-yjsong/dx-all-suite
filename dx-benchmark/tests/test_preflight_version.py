"""The run_model minimum-version gate: parsing, the threshold, and its scope.

Scope matters as much as the threshold -- and the scope is *everything*. The
gate is not about `--max-throughput` being callable; it is about every row of a
campaign describing the same runtime. The E2E / multi-stream families drive
GStreamer pipelines whose dxstream plugin links the same libdxrt.so that ships
with `run_model`, so the runtime version moves their numbers too. Preflight
therefore blocks a too-old runtime for every family, not just the model one.
"""

import pytest

from benchmark import env_fingerprint as ef
from benchmark.env_fingerprint import _parse_dxrt_version, check_preflight


def test_parse_dxrt_version_from_help_first_line():
    # The banner is argv[0]-dependent: `run_model` is a symlink to `dxrun`,
    # so both spellings occur in the wild. Verified against real v3.4.0/v3.5.0.
    assert _parse_dxrt_version("DXRT v3.5.0 run_model") == (3, 5, 0)
    assert _parse_dxrt_version("DXRT v3.5.0 dxrun") == (3, 5, 0)
    assert _parse_dxrt_version("DXRT v3.4.0 run_model") == (3, 4, 0)


def test_parse_dxrt_version_tolerates_build_stamp():
    # `_normalize_version` is not applied here, so a dirty build must still parse.
    assert _parse_dxrt_version("DXRT v3.5.0+9ef3f4c-dirty run_model") == (3, 5, 0)


def test_parse_dxrt_version_accepts_prerelease_as_that_version():
    # D6: staging itself is a v3.5.0-rc and does carry --max-throughput.
    assert _parse_dxrt_version("DXRT v3.5.0-rc.4 dxrun") == (3, 5, 0)


def test_parse_dxrt_version_tolerates_missing_v_prefix():
    # A banner that drops the 'v' must not read as "too old" on every host.
    assert _parse_dxrt_version("DXRT 3.5.0 run_model") == (3, 5, 0)


def test_parse_dxrt_version_returns_none_on_garbage():
    assert _parse_dxrt_version("unknown") is None
    assert _parse_dxrt_version(None) is None
    assert _parse_dxrt_version("") is None


def test_preflight_rejects_outdated_run_model():
    fp = {"missing_required": [],
          "outdated_required": [("run_model", "DXRT v3.4.0 run_model", "v3.5.0")]}
    ok, errors = check_preflight(fp)
    assert ok is False
    assert any("run_model" in e and "3.4.0" in e and "3.5.0" in e for e in errors)


def test_preflight_rejects_unparseable_version():
    # D5: fail closed. A present-but-broken run_model must not start a campaign.
    fp = {"missing_required": [], "outdated_required": [("run_model", "unknown", "v3.5.0")]}
    ok, errors = check_preflight(fp)
    assert ok is False
    assert any("unknown" in e for e in errors)


def test_preflight_still_rejects_a_missing_tool():
    # Absence and obsolescence are both preflight failures, with distinct messages.
    ok, errors = check_preflight({"missing_required": ["run_model"], "outdated_required": []})
    assert ok is False
    assert any("run_model" in e and "not found" in e for e in errors)


def test_preflight_passes_when_nothing_is_wrong():
    ok, errors = check_preflight({"missing_required": [], "outdated_required": []})
    assert ok is True
    assert errors == []


def test_fingerprint_flags_this_hosts_run_model():
    # Integration: whatever is installed here, the two lists must agree with it.
    from benchmark.env_fingerprint import (collect_fingerprint, MIN_TOOL_VERSIONS,
                                           _parse_dxrt_version)
    fp = collect_fingerprint()
    info = fp["tools"]["run_model"]
    outdated = dict((t, (f, n)) for t, f, n in fp["outdated_required"])
    if not info["available"]:
        assert "run_model" in fp["missing_required"]
        return
    found = _parse_dxrt_version(info["version"])
    if found is None or found < MIN_TOOL_VERSIONS["run_model"]:
        assert "run_model" in outdated
    else:
        assert "run_model" not in outdated


# (banner, must_be_blocked) -- pins the threshold AND the fail-closed policy.
# Verified to kill all four mutants that survived the original suite:
#   min->(3,4,0) | min->(9,9,9) | `<` -> `<=` | `is None or` -> `is not None and`
_VERSION_TABLE = [
    ("DXRT v3.4.0 run_model",  True),   # below the minimum
    ("DXRT v3.5.0 run_model",  False),  # exactly the minimum -- must NOT be blocked
    ("DXRT v3.10.0 run_model", False),  # 10 > 5 numerically, not lexically
    ("unknown",                True),   # D5: unparseable fails closed
]


@pytest.mark.parametrize("banner,blocked", _VERSION_TABLE)
def test_version_gate_decision_table(monkeypatch, banner, blocked):
    real = ef._tool_version

    def fake(name):
        if name == "run_model":
            return {"path": "/stub/run_model", "version": banner, "available": True}
        return real(name)

    monkeypatch.setattr(ef, "_tool_version", fake)
    fp = ef.collect_fingerprint()
    flagged = [t for t, _f, _n in fp["outdated_required"]]
    assert ("run_model" in flagged) is blocked, \
        f"{banner!r}: expected blocked={blocked}, got outdated_required={fp['outdated_required']}"


def test_minimum_version_is_pinned():
    """A literal pin, so raising or lowering the bar is a deliberate edit.

    Mirrors tests/test_tool_version.py::test_protocol_version_is_v2_for_dxrun_sweep,
    which pins PROTOCOL_VERSION the same way and for the same reason.
    """
    assert ef.MIN_TOOL_VERSIONS["run_model"] == (3, 5, 0)


@pytest.mark.parametrize("family", ["model", "e2e", "multi", "all"])
def test_version_gate_blocks_every_family(monkeypatch, capsys, family):
    """Pins the scope: a too-old runtime stops `run` whatever --family asks for.

    This is the property that family scoping would break, so it is asserted the
    only way that actually bites -- by driving ``cmd_run`` itself with a v3.4.0
    fingerprint and requiring rc=1 plus the "too old" message. Re-introducing a
    ``if "model" in families`` guard lets the pipeline families walk past the
    gate, and the ``_resolve_output_dir`` tripwire below turns that into a
    failure instead of a silently degraded campaign. An assertion on the
    ``families`` expression alone could not do that: the expression would no
    longer exist.
    """
    from benchmark import __main__ as m

    fp = {"missing_required": [], "missing_e2e": [],
          "outdated_required": [("run_model", "DXRT v3.4.0 run_model", "v3.5.0")]}
    monkeypatch.setattr(m, "collect_fingerprint", lambda: fp)
    monkeypatch.setattr(m, "check_cpu_governor", lambda _fp: None)

    def _tripwire(*_a, **_k):
        raise AssertionError(
            f"--family {family} walked past the version gate on a v3.4.0 runtime"
        )

    monkeypatch.setattr(m, "_resolve_output_dir", _tripwire)

    args = m._build_parser().parse_args(["run", "--family", family])
    rc = m.cmd_run(args)
    out = capsys.readouterr().out

    assert rc == 1, f"--family {family}: expected the version gate to block, got rc={rc}"
    assert "too old" in out, f"--family {family}: blocked, but not by the version gate:\n{out}"
