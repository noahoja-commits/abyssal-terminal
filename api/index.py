from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

app = FastAPI(title="Abyssal Terminal v666")

# Determine base path (works locally and on Vercel)
BASE_DIR = Path(__file__).parent.parent

# Mount static files from static directory
static_dir = BASE_DIR / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Read the HTML template
template_path = BASE_DIR / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
async def root():
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    return "<h1>ABYSSAL TERMINAL</h1><p>Template not found. The void is silent.</p>"

@app.get("/favicon.ico")
async def favicon():
    return ""

@app.get("/api/status")
async def status():
    return {
        "status": "operational",
        "version": "666.0.0",
        "operative": "GOY",
        "souls_collected": 666,
        "abyss_depth": "unlimited"
    }

@app.get("/api/ritual/{rite}")
async def ritual(rite: str):
    rites = {
        "summon": "Entity manifesting in sector 7",
        "banish": "Cleansing protocols initiated",
        "divine": "No divine signal detected",
        "blood": "Blood rain intensity increased",
    }
    return {
        "rite": rite,
        "result": rites.get(rite, "Unknown ritual. The void stares back."),
        "timestamp": "eternity"
    }
