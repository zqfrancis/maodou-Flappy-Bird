#!/usr/bin/env python3
"""Regenerate codepen/ from js/game.js + data/idiom-bank.json."""
import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).parent / "_extract_game.py"), run_name="__main__")
