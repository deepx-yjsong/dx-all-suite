"""G1: CPU governor capture + preflight warning.

Host-bound benchmark metrics (latency, small-model throughput, E2E) depend on the
CPU frequency governor. We record it in the fingerprint and WARN when it is not
'performance', so a slow/variable run is diagnosable after the fact.
"""
from benchmark.env_fingerprint import (
    _get_cpu_governors, check_cpu_governor, collect_fingerprint,
)


def _mk_cpu(base, gov_by_cpu):
    for cpu, gov in gov_by_cpu.items():
        d = base / cpu / "cpufreq"
        d.mkdir(parents=True)
        (d / "scaling_governor").write_text(gov + "\n")


def test_get_cpu_governors_counts_per_governor(tmp_path):
    _mk_cpu(tmp_path, {"cpu0": "performance", "cpu1": "performance"})
    assert _get_cpu_governors(str(tmp_path)) == {"performance": 2}


def test_get_cpu_governors_mixed(tmp_path):
    _mk_cpu(tmp_path, {"cpu0": "performance", "cpu1": "schedutil"})
    assert _get_cpu_governors(str(tmp_path)) == {"performance": 1, "schedutil": 1}


def test_get_cpu_governors_no_cpufreq_returns_empty(tmp_path):
    (tmp_path / "cpu0").mkdir(parents=True)   # no cpufreq/ subdir
    assert _get_cpu_governors(str(tmp_path)) == {}


def test_check_governor_none_when_all_performance():
    fp = {"host": {"cpu_governors": {"performance": 8}}}
    assert check_cpu_governor(fp) is None


def test_check_governor_warns_when_not_performance():
    fp = {"host": {"cpu_governors": {"schedutil": 8}}}
    msg = check_cpu_governor(fp)
    assert msg is not None
    assert "performance" in msg and "schedutil" in msg


def test_check_governor_warns_when_mixed():
    fp = {"host": {"cpu_governors": {"performance": 4, "powersave": 4}}}
    assert check_cpu_governor(fp) is not None


def test_check_governor_none_when_unknown():
    # cpufreq unavailable → empty → do NOT nag when we cannot tell.
    assert check_cpu_governor({"host": {"cpu_governors": {}}}) is None
    assert check_cpu_governor({"host": {}}) is None


def test_fingerprint_host_carries_cpu_governors():
    fp = collect_fingerprint()
    assert "cpu_governors" in fp["host"]
    assert isinstance(fp["host"]["cpu_governors"], dict)
