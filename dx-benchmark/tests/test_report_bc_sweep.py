"""REPORT.md throughput section shows the buffer-count winner + sweep curve."""
from benchmark.reporter import _add_model_throughput_section


def _row(**kw):
    base = {"model": "yolo26-n_640x640.dxnn", "task": "object_detection", "size": "n",
            "use_ort": False, "family": "throughput", "fps": 322.0, "fps_std": 1.0,
            "cpu_pct": 180.0, "status": "ok"}
    base.update(kw)
    return base


def test_throughput_table_has_bc_column_with_winner():
    rows = [_row(buffer_count=5, buffer_count_curve="3:215.0 4:282.0 5:322.0 6:302.0 7:298.0 8:297.0")]
    lines = []
    _add_model_throughput_section(lines, rows)
    out = "\n".join(lines)
    assert "BC" in out                      # BC column header
    # the winner value appears in the throughput row (…| 322.0 ±1.0 | 5 | 180 |…)
    assert "| 5 |" in out


def test_throughput_section_has_sweep_curve_with_bolded_winner():
    rows = [_row(buffer_count=5, buffer_count_curve="3:215.0 4:282.0 5:322.0 6:302.0 7:298.0 8:297.0")]
    lines = []
    _add_model_throughput_section(lines, rows)
    out = "\n".join(lines)
    assert "Buffer-count sweep" in out       # dedicated sub-table below throughput
    assert "[3]:215" in out and "[8]:297" in out  # curve endpoints, bracketed bc
    assert " · " in out                       # pairs clearly separated
    assert "**[5]:322" in out                 # winner bolded
    assert "★" in out                         # winner marked


def test_bc_columns_absent_for_legacy_rows_without_buffer_count():
    rows = [_row()]   # no buffer_count / buffer_count_curve (old data)
    lines = []
    _add_model_throughput_section(lines, rows)
    out = "\n".join(lines)
    assert "Buffer-count sweep" not in out    # no empty sweep table for legacy runs
