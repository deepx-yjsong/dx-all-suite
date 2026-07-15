"""Adaptive buffer-count knee-search (protocol v2, Task 1).

Throughput vs --buffer-count is a unimodal saturation curve (rise → knee →
slight decline). We ascend from a core-count floor (3), stop at the knee, and
pick the smallest buffer-count on the plateau. See spec 2026-07-15-benchmark-
protocol-v2-design.md.
"""
from benchmark.runner_model import select_buffer_count


def _curve(mapping):
    seen = {}

    def probe(c):
        seen[c] = mapping[c]
        return mapping[c]

    probe.seen = seen
    return probe


def test_picks_knee_and_stops_on_decline_large_model():
    # x-large shape: rises to 4, declines at 5 → winner 4, never probes high.
    p = _curve({3: 45.0, 4: 49.0, 5: 47.0})
    win, curve, edge = select_buffer_count(p, start=3, decline_eps=0.02)
    assert win == 4
    assert 6 not in p.seen and 16 not in p.seen
    assert edge is False


def test_plateau_prefers_smaller():
    # nano-ish plateau: within 1% from c=6 up → prefer 6 (smallest within eps of best).
    p = _curve({3: 219.0, 4: 282.0, 5: 298.0, 6: 302.0, 7: 304.0, 8: 305.0})
    win, curve, edge = select_buffer_count(p, start=3, improve_eps=0.01)
    assert win == 6


def test_edge_flag_when_still_rising_at_cap():
    p = _curve({3: 10.0, 4: 20.0, 5: 30.0})
    win, curve, edge = select_buffer_count(p, start=3, max_probe=5)
    assert win == 5 and edge is True


def test_winner_equals_start_probes_below_once():
    # peak lies below the floor: 3 wins the ascent but 2 is actually better.
    p = _curve({3: 40.0, 4: 38.0, 2: 41.0})
    win, curve, edge = select_buffer_count(p, start=3, decline_eps=0.02)
    assert 2 in p.seen
    assert win == 2
