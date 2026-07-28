"""dx-benchmark — DEEPX NPU benchmark suite.

``__version__`` is the tool's own SemVer, independent of:
  - the dx-all-suite release it MEASURES (recorded per-run as ``dx_all_suite_version``), and
  - the measurement methodology version (``benchmark.config.PROTOCOL_VERSION``).

Bump this on tool code/CLI/output-schema changes only (a new suite-version data
campaign with an unchanged tool does NOT bump it).
"""

__version__ = "0.1.0"
"""dx-benchmark tool version (SemVer). Beta line starts at 0.x."""
