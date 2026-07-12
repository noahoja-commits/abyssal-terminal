from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="Abyssal Terminal v666")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Read the HTML template
HTML_PATH = Path(__file__).parent / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML_PATH.read_text(encoding="utf-8")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=6666)
