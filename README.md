# ABYSSAL TERMINAL v666

A satanic-themed interactive web terminal built with FastAPI, deployed on Vercel.

## Features

- **Blood Rain** — 150 animated drops with gravity
- **Hellfire Embers** — Rising particle system with mouse reactivity
- **Rotating Sigil** — Dual-triangle geometry with pulsing glow
- **Glitch Typography** — Chromatic aberration text effects
- **Demon ASCII Spawns** — Random creature manifestations
- **Possession Events** — Random screen flashes
- **Ritual API** — Summon, banish, divine, blood endpoints
- **666 Easter Egg** — Click the bottom-right corner

## Local Development

```bash
cd abyssal-web
pip install -r requirements.txt
python api/index.py
```

Or use the batch file:
```batch
start.bat
```

Open `http://127.0.0.1:6666`

## Deployment

### Vercel

```bash
npm i -g vercel
vercel --prod
```

Or connect the GitHub repository to Vercel for auto-deploy.

## API Endpoints

| Route | Description |
|-------|-------------|
| `GET /` | Main terminal interface |
| `GET /api/status` | System telemetry |
| `GET /api/ritual/{rite}` | Execute rituals (summon, banish, divine, blood) |

## Architecture

```
abyssal-web/
├── api/
│   └── index.py          # FastAPI serverless entry
├── static/
│   ├── style.css         # Demonic styling
│   └── app.js            # Interactive systems
├── templates/
│   └── index.html        # Jinja2 template
├── requirements.txt      # Python deps
├── vercel.json           # Vercel config
└── start.bat             # Windows launcher
```

---

*GOY operative. No sentiment, only execution.*
