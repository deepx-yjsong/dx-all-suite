"""The run_model minimum-version gate: parsing, the threshold, and its scope.

Scope matters as much as the threshold -- the gate belongs to the model
family alone (D7), so preflight must report it without blocking E2E / multi.
"""

import pytest

from benchmark import env_fingerprint as ef
from benchmark.env_fingerprint import (_parse_dxrt_version, check_model_family_readiness,
                                       check_preflight)


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


def test_model_family_readiness_rejects_outdated_run_model():
    fp = {"missing_required": [],
          "outdated_required": [("run_model", "DXRT v3.4.0 run_model", "v3.5.0")]}
    ok, errors = check_model_family_readiness(fp)
    assert ok is False
    assert any("run_model" in e and "3.4.0" in e and "3.5.0" in e for e in errors)


def test_model_family_readiness_rejects_unparseable_version():
    # D5: fail closed. A present-but-broken run_model must not start a campaign.
    fp = {"missing_required": [], "outdated_required": [("run_model", "unknown", "v3.5.0")]}
    ok, errors = check_model_family_readiness(fp)
    assert ok is False
    assert any("unknown" in e for e in errors)


def test_model_family_readiness_passes_when_version_ok():
    ok, errors = check_model_family_readiness({"outdated_required": []})
    assert ok is True
    assert errors == []


def test_preflight_ignores_an_outdated_run_model():
    # D7: the version gate belongs to the model family alone. `--max-throughput`
    # is only ever invoked by runner_model, so a v3.4.0 host must still clear
    # preflight and run the E2E / multi families.
    fp = {"missing_required": [],
          "outdated_required": [("run_model", "DXRT v3.4.0 run_model", "v3.5.0")]}
    ok, errors = check_preflight(fp)
    assert ok is True
    assert errors == []


def test_preflight_still_rejects_a_missing_tool():
    # D7 narrows the gate to versions only -- absence still blocks everything.
    ok, errors = check_preflight({"missing_required": ["run_model"], "outdated_required": []})
    assert ok is False
    assert any("run_model" in e for e in errors)


def test_preflight_passes_when_nothing_is_wrong():
    ok, errors = check_preflight({"missing_required": [], "outdated_required": []})
    assert ok is True
    assert errors == []


def test_cmd_run_consults_the_model_family_gate():
    """Pins the wiring: the gate must be looked up inside ``cmd_run`` itself.

    It does not pin the ``families`` condition around it -- that is covered by
    the live model/e2e x installed/shim check recorded in the task notes.
    """
    from benchmark.__main__ import cmd_run
    assert "check_model_family_readiness" in cmd_run.__code__.co_names


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
