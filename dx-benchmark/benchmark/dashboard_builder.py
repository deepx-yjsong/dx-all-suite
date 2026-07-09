"""Build a static HTML dashboard backed by dataset.json."""

from __future__ import annotations

import json
from pathlib import Path

from .aggregator import save_dataset_json
from .config import APP_DIR

DASHBOARD_SRC_DIR = APP_DIR / "dashboard"
DATASET_PLACEHOLDER = "__DATASET_JSON__"


def build_static_dashboard(dataset: dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    save_dataset_json(dataset, output_dir / "dataset.json")

    index_html = (DASHBOARD_SRC_DIR / "index.html").read_text(encoding="utf-8")
    index_html = index_html.replace(DATASET_PLACEHOLDER, json.dumps(dataset))
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    (output_dir / "app.js").write_text(
        (DASHBOARD_SRC_DIR / "app.js").read_text(encoding="utf-8"), encoding="utf-8")
    (output_dir / "styles.css").write_text(
        (DASHBOARD_SRC_DIR / "styles.css").read_text(encoding="utf-8"), encoding="utf-8")
    return output_dir / "index.html"
