"""Minimum run_model version check in preflight."""

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


def test_preflight_passes_when_version_ok():
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
