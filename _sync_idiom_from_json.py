#!/usr/bin/env python3
"""Copy data/idiom-bank.json → js/idiom-bank.js (after editing JSON)."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
data = json.loads((ROOT / "data" / "idiom-bank.json").read_text(encoding="utf-8"))
(ROOT / "js" / "idiom-bank.js").write_text(
    "window.IDIOM_BANK = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8",
)
print(f"Synced {len(data)} entries to js/idiom-bank.js")
