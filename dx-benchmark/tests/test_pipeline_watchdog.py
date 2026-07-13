from benchmark.config import BenchmarkConfig


def test_watchdog_config_defaults():
    c = BenchmarkConfig()
    assert c.e2e_stall_timeout == 90.0
    assert c.e2e_hard_cap == 1800.0
