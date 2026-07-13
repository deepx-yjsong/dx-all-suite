from benchmark.config import BenchmarkConfig
from benchmark.runner_pipeline import PipeOutcome, _build_single_pipeline, _build_multi_pipeline


def test_watchdog_config_defaults():
    c = BenchmarkConfig()
    assert c.e2e_stall_timeout == 90.0
    assert c.e2e_hard_cap == 1800.0


def test_pipeoutcome_values():
    assert PipeOutcome.OK.value == "ok"
    assert PipeOutcome.HANG.value == "hang"
    assert PipeOutcome.RUNAWAY.value == "runaway"


def test_pipelines_have_progressreport():
    sp = _build_single_pipeline("m.dxnn", True, "/v.mp4", "pp.json")
    mp = _build_multi_pipeline("m.dxnn", True, "/v.mp4", "pp.json", 2)
    assert "progressreport" in sp
    assert "progressreport" in mp
    # heartbeat sits right before the terminal fakesink
    assert sp.index("progressreport") < sp.index("fakesink")
    assert mp.index("progressreport") < mp.index("fakesink")
