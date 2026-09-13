# Flappy Bird — Multi-Mode Educational Game

Canonical sources: **`js/game.js`** + **`data/idiom-bank.json`**

## Quick start (phone, iPad, laptop)

```bash
cd /home/wendy/flappy
python3 -m http.server 8080
```

- **Laptop:** http://localhost:8080
- **Phone (same Wi‑Fi):** http://YOUR_COMPUTER_IP:8080

Touch or click to flap; **Space** on keyboard. Top-left 🔊 mutes sound.

## File layout

| File | Purpose |
|------|---------|
| `index.html` | Page shell |
| `css/style.css` | Styles (canvas-only UI) |
| `js/game.js` | **Edit game logic here** |
| `data/idiom-bank.json` | **Edit idioms here** |
| `js/idiom-bank.js` | Auto-synced from JSON (local `file://` load) |
| `codepen/` | Generated bundle for CodePen Project |

## Workflow

**Edit game:**
1. Change `js/game.js`
2. Run `python3 _extract_game.py` → refreshes `codepen/`
3. Re-paste `codepen/*` into CodePen if needed

**Edit idioms:**
1. Change `data/idiom-bank.json`
2. Run `python3 _sync_idiom_from_json.py` → updates `js/idiom-bank.js`
3. Run `python3 _extract_game.py` → updates `codepen/script.js`

Or run both:

```bash
python3 _sync_idiom_from_json.py && python3 _extract_game.py
```

## CodePen (free Project — 3 files)

Copy into your CodePen Project (same filenames):

| CodePen | Local |
|---------|-------|
| `index.html` | `codepen/index.html` |
| `style.css` | `codepen/style.css` |
| `script.js` | `codepen/script.js` |

## Modes

- **Boy / Girl** — classic Flappy pipes
- **Chinese** — fill-in-blank idioms & poems (pinyin toggle on menu)
- **Math** — grade 1–7; EN/中文 toggle top-right on canvas; fixed ⏸ / ⏭ buttons bottom corners

## Controls (Chinese & Math)

| Button | Position |
|--------|----------|
| ⏸ Pause | Bottom-left |
| ⏭ Skip | Bottom-right |
| EN / 中文 | Top-right (Math mode only) |
