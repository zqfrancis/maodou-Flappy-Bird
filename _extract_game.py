#!/usr/bin/env python3
"""Build codepen/ from canonical js/game.js + data/idiom-bank.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent

js = (ROOT / "js" / "game.js").read_text(encoding="utf-8")
css = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
idiom_data = json.loads((ROOT / "data" / "idiom-bank.json").read_text(encoding="utf-8"))

(ROOT / "js" / "idiom-bank.js").write_text(
    "window.IDIOM_BANK = " + json.dumps(idiom_data, ensure_ascii=False, indent=2) + ";\n",
    encoding="utf-8",
)

(ROOT / "codepen").mkdir(exist_ok=True)

(ROOT / "codepen" / "index.html").write_text(
    """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Flappy Bird - Choose Theme Style</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>

<div id="debug-log"></div>
<div id="game-container">
    <canvas id="birdCanvas"></canvas>
</div>

<script src="./script.js"></script>
</body>
</html>
""",
    encoding="utf-8",
)

(ROOT / "codepen" / "style.css").write_text(css + "\n", encoding="utf-8")

codepen_js = "const idiomBank = " + json.dumps(idiom_data, ensure_ascii=False, indent=2) + ";\n\n"
codepen_js += re.sub(r"    let idiomBank = window\.IDIOM_BANK \|\| \[\];\n\n", "", js)
codepen_js = re.sub(
    r"\n    async function loadIdiomBank\(\)[\s\S]*?\n    \}\n",
    "\n",
    codepen_js,
    count=1,
)
codepen_js = codepen_js.replace("async function safeInit()", "function safeInit()")
codepen_js = codepen_js.replace("        await loadIdiomBank();\n", "")
(ROOT / "codepen" / "script.js").write_text(codepen_js, encoding="utf-8")

print(f"OK: codepen/ refreshed ({len(js.splitlines())} lines game.js, {len(idiom_data)} idioms)")
