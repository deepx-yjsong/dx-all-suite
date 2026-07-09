from benchmark.env_fingerprint import _read_release_ver, resolve_dx_all_suite_version


def test_read_release_ver_walks_up(tmp_path):
    root = tmp_path / "suite"
    root.mkdir()
    (root / "release.ver").write_text("v2.4.0\n")
    deep = root / "a" / "b"
    deep.mkdir(parents=True)
    assert _read_release_ver(deep) == "v2.4.0"


def test_read_release_ver_none_when_absent(tmp_path):
    assert _read_release_ver(tmp_path) is None


def test_resolve_explicit_wins(tmp_path):
    (tmp_path / "release.ver").write_text("v2.3.0")
    assert resolve_dx_all_suite_version("v9.9.9", start=tmp_path) == "v9.9.9"


def test_resolve_falls_back_to_release_ver(tmp_path):
    (tmp_path / "release.ver").write_text("v2.3.0")
    assert resolve_dx_all_suite_version(None, start=tmp_path) == "v2.3.0"


def test_resolve_none_when_nothing(tmp_path):
    assert resolve_dx_all_suite_version(None, start=tmp_path) is None


def test_resolve_whitespace_explicit_falls_back(tmp_path):
    (tmp_path / "release.ver").write_text("v2.3.0")
    assert resolve_dx_all_suite_version("   ", start=tmp_path) == "v2.3.0"
