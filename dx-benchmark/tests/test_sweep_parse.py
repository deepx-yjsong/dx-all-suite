"""dxrun --max-throughput 출력 파서 단위 테스트."""

from benchmark.runner_model import _parse_sweep

# v3.5.0 (staging a918c3da) 실측 출력. yolo26-n, --buffer-count 3-6 --probe-time 2
SWEEP_LOG = """\
Searching I/O Buffer Count range=3-6
Runtime Framework Version: v3.5.0
Run model target mode : Max-Throughput Mode
Max-throughput sweep: start=3 step=1 cap=6 round-time=2s peak-drop-threshold=3% (patience 2, stall 3)
=== Model File: /path/yolo26-n_640x640.dxnn ===
[max-throughput] Measuring buffer-count=3 for 2s ...
[max-throughput] buffer-count=3 fps=100.83 loops=205
[max-throughput] Measuring buffer-count=4 for 2s ...
[max-throughput] buffer-count=4 fps=115.55 loops=236 improvement=14.59% peak-drop=0.00% stall=0
[max-throughput] Measuring buffer-count=5 for 2s ...
[max-throughput] buffer-count=5 fps=132.68 loops=271 improvement=14.83% peak-drop=0.00% stall=0
[max-throughput] Measuring buffer-count=6 for 2s ...
[max-throughput] buffer-count=6 fps=141.66 loops=290 improvement=6.76% peak-drop=0.00% stall=0
====================================================
* Max-Throughput Sweep Result
  Stop reason : reached buffer-count cap (6)

   buffer-count |        FPS |  improvement
  --------------+------------+-------------
              3 |     100.83 |          --
              4 |     115.55 |     +14.59%
              5 |     132.68 |     +14.83%
              6 |     141.66 |      +6.76%  <== best

  => Recommended buffer-count : 6
     Max FPS                  : 141.66  (loops=290)
====================================================

[max-throughput] Final run with buffer-count=6 ...
=============================================
* Benchmark Result (429 inputs)
  - FPS : 141.21
=============================================
"""

FAILED_LOG = """\
Searching I/O Buffer Count range=3-16
[max-throughput] Measuring buffer-count=3 for 10s ...
[max-throughput] buffer-count=3 fps=0.00 loops=0
[max-throughput] Measuring buffer-count=4 for 10s ...
[max-throughput] buffer-count=4 fps=0.00 loops=0 improvement=0.00% peak-drop=0.00% stall=1
[max-throughput] Measuring buffer-count=5 for 10s ...
[max-throughput] buffer-count=5 fps=0.00 loops=0 improvement=0.00% peak-drop=0.00% stall=2

[ERR] Max-throughput sweep completed but every round measured 0 fps; no buffer count can be recommended.
"""


def test_parse_sweep_extracts_winner_and_curve():
    winner, curve = _parse_sweep(SWEEP_LOG)
    assert winner == 6
    assert curve == {3: 100.83, 4: 115.55, 5: 132.68, 6: 141.66}


def test_parse_sweep_returns_none_when_no_recommendation():
    winner, curve = _parse_sweep(FAILED_LOG)
    assert winner is None
    assert curve == {3: 0.0, 4: 0.0, 5: 0.0}


def test_parse_sweep_handles_empty_log():
    winner, curve = _parse_sweep("")
    assert winner is None
    assert curve == {}
