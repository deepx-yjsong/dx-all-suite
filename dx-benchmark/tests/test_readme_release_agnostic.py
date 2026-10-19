"""README must not change on every SDK release.

Release-specific data (versions, run ids, measured numbers) lives in results/ and
docs/ANALYSIS_*; the README only links to them.
"""
import re
from pathlib import Path

README = (Path(__file__).resolve().parents[1] / "README.md").read_text()


def test_readme_has_no_hardcoded_versions():
    assert not re.findall(r"\bv\d+\.\d+\.\d+\b", README)


def test_readme_has_no_hardcoded_run_ids():
    assert not re.findall(r"\b\d{8}_\d{6}\b", README)


def test_readme_points_to_analysis_instead_of_inlining_results():
    assert "docs/ANALYSIS_EN.md" in README and "docs/ANALYSIS_KOR.md" in README
    assert "At a Glance" not in README
    assert not re.search(r"\d+(\.\d+)? fps / \d+ ch", README)
