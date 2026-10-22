"""NPU product classification from dxrt-cli -s signals.

Single source of truth mapping per-device (Board, Memory) signals to canonical
DEEPX product names (H1-Quattro / M1 / M1M) as listed on deepx.ai/shop_now.
`dxrt-cli -s` reports the *chip* ("M1") on the Device line for every product, so
product type is inferred from Board prefix + Memory technology instead.
"""

from __future__ import annotations

import re

# (board_prefix, memory_substr | None, product, chips_per_card)
# Ordered: more specific rule first. Memory is only a *fallback* signal: an M1 M.2 card
# ships with LPDDR5 (Rev 1.0, 5600 Mbps) or LPDDR5x (6000 Mbps), so LPDDR5x on an M.2
# board does not mean H1. LPDDR4 is what marks the M1M card.
NPU_SIGNATURES: list[tuple[str, str | None, str, int]] = [
    ("H1",  None,       "H1-Quattro", 4),
    ("M.2", "LPDDR4",   "M1M",        1),
    ("M.2", None,       "M1",         1),
]

UNKNOWN_PRODUCT = "unknown"


def classify_device(board: str | None, memory: str | None,
                    chip: str | None = None) -> tuple[str, int]:
    """Classify one NPU device. Returns (product, chips_per_card).

    ``chip`` is the name on dxrt-cli's ``* Device N: <chip>`` line. It only overrides the
    board/memory rules when it names a product they cannot tell apart (a standalone H1
    M.2, or an M1M); the usual "M1" is the chip of every product, so it decides nothing.
    """
    b = (board or "").strip().upper()
    m = (memory or "").strip().upper()
    c = (chip or "").strip().upper()
    if b.startswith("M.2"):
        if c.startswith("H1"):
            return "H1", 1
        if c == "M1M":
            return "M1M", 1
    for prefix, mem, product, per_card in NPU_SIGNATURES:
        if b.startswith(prefix.upper()) and (mem is None or mem in m):
            return product, per_card
    return UNKNOWN_PRODUCT, 1


def classify_devices(devices: list[tuple]) -> list[dict]:
    """Aggregate per-device signals into [{"product", "count"}], first-seen order.

    Each signal is ``(board, memory)`` or ``(board, memory, chip)``.

    H1 chips fold into cards: count = chips // chips_per_card (>=1 if any chip seen).
    """
    chips: dict[str, int] = {}
    per_card: dict[str, int] = {}
    order: list[str] = []
    for signal in devices:
        board, memory, *rest = signal
        product, cpc = classify_device(board, memory, rest[0] if rest else None)
        if product not in chips:
            chips[product] = 0
            per_card[product] = cpc
            order.append(product)
        chips[product] += 1

    modules: list[dict] = []
    for product in order:
        cpc = per_card[product] or 1
        # NOTE: floor-division assumes fully-populated cards; a partial card
        # (e.g. 1-3 of 4 H1 chips reported) folds to count=1, not flagged here.
        # Cross-run/mixed-hardware anomalies are surfaced by the aggregator guard (Task 4).
        count = max(1, chips[product] // cpc) if cpc > 1 else chips[product]
        modules.append({"product": product, "count": count})
    return modules


def format_sku(modules: list[dict]) -> str:
    """Slug for folder/env id: 'M1', 'M1x2', mixed 'M1-M1M'."""
    parts = []
    for mod in modules:
        product = mod.get("product", UNKNOWN_PRODUCT)
        count = int(mod.get("count", 1) or 1)
        parts.append(product if count <= 1 else f"{product}x{count}")
    return "-".join(parts) if parts else UNKNOWN_PRODUCT


def format_badge(modules: list[dict]) -> str:
    """Human display: 'M1', 'M1 ×2', mixed 'M1 + M1M'."""
    parts = []
    for mod in modules:
        product = mod.get("product", UNKNOWN_PRODUCT)
        count = int(mod.get("count", 1) or 1)
        parts.append(product if count <= 1 else f"{product} ×{count}")
    return " + ".join(parts) if parts else UNKNOWN_PRODUCT


def classify_from_raw(raw: str) -> list[dict]:
    """Backfill path: parse per-device (Board, Memory, chip) from dxrt-cli -s raw text."""
    devices: list[tuple[str | None, str | None, str | None]] = []
    board = memory = chip = None
    started = False
    for line in raw.splitlines():
        s = line.strip()
        if s.startswith("* Device"):
            if started:
                devices.append((board, memory, chip))
            board = memory = None
            cm = re.match(r"\*\s*Device\s+\d+\s*:\s*([^,\s]+)", s)
            chip = cm.group(1) if cm else None
            started = True
        elif "Board" in s and ":" in s and "Chip" not in s:
            mm = re.search(r":\s*(.+)", s)
            if mm:
                board = mm.group(1).strip()
        elif "Memory" in s and ":" in s:
            mm = re.search(r":\s*(.+)", s)
            if mm:
                memory = mm.group(1).strip()
    if started:
        devices.append((board, memory, chip))
    return classify_devices(devices)
