import pytest


@pytest.fixture(autouse=True)
def _no_real_dxtop_probe(monkeypatch):
    """collect_fingerprint() starts a real dxtop for ~2 s on hosts that have one.

    Tests that call it dozens of times must not pay that, nor depend on the machine
    they run on. The probe itself is covered by tests/test_completeness.py, which
    calls `npu_monitor.probe_npu_monitor` directly with a patched NpuMonitor.
    """
    from benchmark import env_fingerprint
    monkeypatch.setattr(env_fingerprint, "_probe_npu_monitor",
                        lambda: {"ok": True, "reason": "stubbed in tests"})
