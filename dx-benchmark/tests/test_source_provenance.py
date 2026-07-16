"""Source provenance: git branch/commit capture + REPORT exposure.

The installed binaries expose version strings (+ a commit hash for RT); to trace
WHICH source branch/commit produced a run, we also record the git state of the
suite source checkouts.
"""
from benchmark.env_fingerprint import _git_provenance, _get_source_provenance
from benchmark.reporter import _add_environment_section


def test_git_provenance_returns_commit_and_branch_for_a_repo():
    p = _git_provenance(".")            # pytest runs inside the suite git checkout
    assert p is not None
    assert p["commit"] and len(p["commit"]) >= 7
    assert "branch" in p and "describe" in p


def test_git_provenance_none_for_non_repo(tmp_path):
    assert _git_provenance(str(tmp_path)) is None


def test_get_source_provenance_is_a_dict():
    prov = _get_source_provenance()
    assert isinstance(prov, dict)
    # running inside the checkout, at least one repo's provenance is captured
    assert prov and all("commit" in v for v in prov.values())


def test_report_environment_shows_provenance_and_rt_commit():
    fp = {
        "host": {}, "product_name": None,
        "npu": {"sku": "M1", "rt_version": "v3.4.0", "rt_version_raw": "v3.4.0+ed51532",
                "driver": "v2.5.1", "firmware": "v2.7.1"},
        "tools": {},
        "source_provenance": {
            "dx_runtime": {"branch": "feat/x", "commit": "abcdef1234567890", "describe": "v2.4.0-3-gabcdef1"},
        },
    }
    lines = []
    _add_environment_section(lines, fp)
    out = "\n".join(lines)
    assert "v3.4.0+ed51532" in out          # RT commit surfaced
    assert "Source Provenance" in out
    assert "feat/x" in out and "abcdef123456" in out
