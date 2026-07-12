from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import random

app = FastAPI(title="Abyssal Terminal v666")

# HTML template embedded to avoid filesystem issues on serverless
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ABYSSAL TERMINAL v666</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <canvas id="bloodCanvas"></canvas>
    <canvas id="emberCanvas"></canvas>
    <canvas id="veinCanvas"></canvas>
    <canvas id="noiseCanvas"></canvas>
    <div class="scanlines"></div>
    <div class="vignette"></div>
    <div class="possession-flash" id="possessionFlash"></div>
    <div class="corruption-overlay" id="corruptionOverlay"></div>
    <div class="static-burst" id="staticBurst"></div>

    <div class="pentagram-bg">
        <svg viewBox="0 0 200 200">
            <polygon points="100,10 40,198 190,78 10,78 160,198" 
                     fill="none" stroke="#ff2a2a" stroke-width="1"/>
            <circle cx="100" cy="100" r="95" fill="none" stroke="#ff2a2a" stroke-width="0.5"/>
        </svg>
    </div>

    <div class="terminal">
        <div class="boot-sequence" id="bootSequence"></div>

        <div class="sigil-container">
            <svg class="sigil" viewBox="0 0 200 200">
                <circle cx="100" cy="100" r="95"/>
                <circle cx="100" cy="100" r="70"/>
                <path d="M100,15 L15,170 L185,170 Z"/>
                <path d="M100,185 L15,30 L185,30 Z"/>
                <ellipse cx="100" cy="100" rx="20" ry="12"/>
                <circle cx="100" cy="100" r="6"/>
                <path d="M100,5 L100,15 M100,185 L100,195"/>
                <path d="M5,100 L15,100 M185,100 L195,100"/>
                <path d="M50,50 Q100,30 150,50"/>
                <path d="M50,150 Q100,170 150,150"/>
            </svg>
        </div>

        <h1 class="glitch-title" data-text="ABYSSAL TERMINAL">ABYSSAL TERMINAL</h1>
        <p class="subtitle">v666.6.6 — GOY OPERATIVE</p>

        <div class="command-line" id="commandLine">
            <span class="prompt">root@abyss:~$</span>
            <span class="typed-text" id="typedText"></span>
            <span class="cursor" id="cursor"></span>
        </div>

        <div class="ritual-panel" id="ritualPanel">
            <button class="ritual-btn" data-rite="summon">SUMMON</button>
            <button class="ritual-btn" data-rite="banish">BANISH</button>
            <button class="ritual-btn" data-rite="divine">DIVINE</button>
            <button class="ritual-btn" data-rite="blood">BLOOD</button>
            <button class="ritual-btn" data-rite="exorcise">EXORCISE</button>
        </div>
        <div class="ritual-output" id="ritualOutput"></div>

        <div class="possession-log" id="possessionLog"></div>
        
        <div class="victim-data" id="victimData">
            <div class="data-line" id="dataLine1">COLLECTING...</div>
            <div class="data-line" id="dataLine2">...</div>
            <div class="data-line" id="dataLine3">...</div>
        </div>
    </div>

    <div class="easter-egg" id="easterEgg">666</div>
    <div class="status-bar" id="statusBar">SYSTEM: OPERATIONAL</div>
    <div class="clock" id="clock">00:00:00</div>

    <div class="face-overlay" id="faceOverlay"></div>
    <div class="whisper-text" id="whisperText"></div>

    <script src="/app.js"></script>
</body>
</html>'''

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML_TEMPLATE

@app.get("/favicon.ico")
async def favicon():
    return ""

@app.get("/api/status")
async def status():
    return {
        "status": "operational",
        "version": "666.6.6",
        "operative": "GOY",
        "souls_collected": random.randint(665, 667),
        "abyss_depth": "unlimited",
        "containment": "breached",
        "entities_active": random.randint(1, 13)
    }

@app.get("/api/ritual/{rite}")
async def ritual(rite: str):
    rites = {
        "summon": "Entity manifesting in sector 7. Do not look directly at it.",
        "banish": "Cleansing protocols initiated. It resists.",
        "divine": "No divine signal detected. The heavens are silent.",
        "blood": "Blood rain intensity increased. Splatter radius expanded.",
        "exorcise": "The entity laughs. You cannot cast out what was invited.",
    }
    return {
        "rite": rite,
        "result": rites.get(rite, "Unknown ritual. The void stares back. Something stares with it."),
        "timestamp": "eternity",
        "corruption_level": random.randint(1, 100)
    }

@app.get("/api/telemetry")
async def telemetry():
    return {
        "message": "Telemetry endpoint active. The server sees everything.",
        "warning": "Your connection is not anonymous.",
        "suggestion": "Do not refresh."
    }
