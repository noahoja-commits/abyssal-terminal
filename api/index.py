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
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Courier+Prime:wght@400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --hellfire: #ff1a1a;
    --ember: #ff4400;
    --sulfur: #ddff00;
    --ash: #0a0a0a;
    --bone: #d4c4b0;
    --vein: #3a0000;
    --void: #020202;
    --flesh: #7a3a1a;
    --ichor: #2a0000;
    --rot: #1a0a0a;
}

body {
    background: var(--void);
    color: var(--bone);
    font-family: 'Courier Prime', monospace;
    overflow: hidden;
    cursor: crosshair;
    animation: bodyPulse 6s ease-in-out infinite;
    user-select: none;
    -webkit-user-select: none;
}

@keyframes bodyPulse {
    0%, 100% { background-color: var(--void); }
    33% { background-color: #050101; }
    66% { background-color: #080202; }
}

/* Noise Canvas */
#noiseCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 4;
    pointer-events: none;
    opacity: 0.08;
    mix-blend-mode: overlay;
}

/* Blood Rain Canvas */
#bloodCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
}

/* Hellfire Particles */
#emberCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
    pointer-events: none;
}

/* Vein Network Canvas */
#veinCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 3;
    pointer-events: none;
    opacity: 0.5;
}

/* Static Burst */
.static-burst {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 55;
    pointer-events: none;
    background: repeating-radial-gradient(
        circle at 50% 50%,
        transparent 0,
        transparent 2px,
        rgba(255, 255, 255, 0.03) 2px,
        rgba(255, 255, 255, 0.03) 4px
    );
    opacity: 0;
}

.static-burst.active {
    animation: staticBurstAnim 0.3s ease-out;
}

@keyframes staticBurstAnim {
    0% { opacity: 0; }
    30% { opacity: 0.4; }
    100% { opacity: 0; }
}

/* Corruption Overlay */
.corruption-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 50;
    pointer-events: none;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(255, 0, 0, 0.03) 2px,
        rgba(255, 0, 0, 0.03) 4px
    );
    opacity: 0;
    transition: opacity 0.5s;
}

.corruption-overlay.active {
    opacity: 1;
    animation: corruptionFlicker 0.08s infinite;
}

@keyframes corruptionFlicker {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 0.7; }
}

/* Face Overlay - subliminal flash */
.face-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 60;
    pointer-events: none;
    background: radial-gradient(ellipse at center, rgba(255, 20, 20, 0.0) 0%, transparent 70%);
    opacity: 0;
}

.face-overlay.active {
    animation: faceFlash 0.08s ease-out;
}

@keyframes faceFlash {
    0% { opacity: 0; }
    50% { opacity: 0.15; }
    100% { opacity: 0; }
}

/* Whisper Text */
.whisper-text {
    position: fixed;
    bottom: 30%;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.7rem;
    color: rgba(255, 42, 42, 0.0);
    z-index: 45;
    pointer-events: none;
    white-space: nowrap;
    letter-spacing: 0.2em;
    transition: color 3s ease;
}

.whisper-text.visible {
    color: rgba(255, 42, 42, 0.15);
}

/* Main Terminal */
.terminal {
    position: relative;
    z-index: 10;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    border: 1px solid transparent;
    animation: terminalBreath 4s ease-in-out infinite;
}

@keyframes terminalBreath {
    0%, 100% { 
        border-color: rgba(74, 0, 0, 0.3);
        box-shadow: inset 0 0 60px rgba(74, 0, 0, 0.15);
    }
    50% { 
        border-color: rgba(74, 0, 0, 0.6);
        box-shadow: inset 0 0 120px rgba(74, 0, 0, 0.4);
    }
}

.scanlines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.2),
        rgba(0, 0, 0, 0.2) 1px,
        transparent 1px,
        transparent 2px
    );
    z-index: 5;
    pointer-events: none;
    animation: scanlineFlicker 0.08s infinite;
}

@keyframes scanlineFlicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.96; }
}

.vignette {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(ellipse at center, transparent 30%, rgba(0,0,0,0.9) 100%);
    z-index: 6;
    pointer-events: none;
}

/* Boot Sequence */
.boot-sequence {
    font-size: 0.8rem;
    line-height: 1.5;
    color: var(--sulfur);
    max-width: 600px;
    text-align: left;
    margin-bottom: 2rem;
    opacity: 0;
}

.boot-line {
    opacity: 0;
    transform: translateX(-10px);
}

.boot-line.visible {
    opacity: 1;
    transform: translateX(0);
    transition: all 0.3s ease;
}

.boot-line.error {
    color: var(--hellfire);
}

.boot-line.success {
    color: var(--sulfur);
}

.boot-line.warning {
    color: var(--ember);
}

.boot-line.corrupted {
    color: var(--hellfire);
    animation: textGlitch 0.15s infinite;
    font-weight: bold;
}

@keyframes textGlitch {
    0%, 100% { transform: translate(0); filter: hue-rotate(0); }
    20% { transform: translate(3px, -2px); filter: hue-rotate(120deg); }
    40% { transform: translate(-2px, 3px); filter: hue-rotate(240deg); }
    60% { transform: translate(2px, 1px); filter: hue-rotate(60deg); }
    80% { transform: translate(-1px, -2px); filter: hue-rotate(180deg); }
}

/* Main Sigil */
.sigil-container {
    position: relative;
    width: 280px;
    height: 280px;
    margin: 1.5rem 0;
    filter: drop-shadow(0 0 40px rgba(255, 20, 20, 0.6));
}

.sigil {
    width: 100%;
    height: 100%;
    animation: sigilPulse 3s ease-in-out infinite, sigilRotate 45s linear infinite;
}

@keyframes sigilPulse {
    0%, 100% { filter: drop-shadow(0 0 30px var(--hellfire)) brightness(1); }
    50% { filter: drop-shadow(0 0 80px var(--hellfire)) brightness(1.5); }
}

@keyframes sigilRotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.sigil path {
    fill: none;
    stroke: var(--hellfire);
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
}

.sigil circle {
    fill: none;
    stroke: var(--hellfire);
    stroke-width: 1.5;
}

/* Glitch Text */
.glitch-title {
    font-family: 'Cinzel', serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: var(--bone);
    position: relative;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin: 0.8rem 0;
    animation: titleBreath 3s ease-in-out infinite;
}

@keyframes titleBreath {
    0%, 100% { text-shadow: 0 0 15px var(--hellfire); }
    50% { text-shadow: 0 0 50px var(--hellfire), 0 0 100px var(--hellfire); }
}

.glitch-title::before,
.glitch-title::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.glitch-title::before {
    color: var(--hellfire);
    animation: glitch-1 1.5s infinite;
    clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
}

.glitch-title::after {
    color: var(--sulfur);
    animation: glitch-2 1.5s infinite;
    clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
}

@keyframes glitch-1 {
    0%, 100% { transform: translate(0); }
    15% { transform: translate(-4px, 3px); }
    30% { transform: translate(4px, -3px); }
    45% { transform: translate(-3px, 1px); }
    60% { transform: translate(3px, 2px); }
    75% { transform: translate(-2px, -2px); }
    90% { transform: translate(2px, 1px); }
}

@keyframes glitch-2 {
    0%, 100% { transform: translate(0); }
    15% { transform: translate(4px, -3px); }
    30% { transform: translate(-4px, 3px); }
    45% { transform: translate(3px, -1px); }
    60% { transform: translate(-3px, -2px); }
    75% { transform: translate(2px, 2px); }
    90% { transform: translate(-2px, -1px); }
}

.subtitle {
    color: var(--ember);
    font-size: 0.85rem;
    letter-spacing: 0.3em;
    animation: subtitleFlicker 2s ease-in-out infinite;
}

@keyframes subtitleFlicker {
    0%, 100% { opacity: 1; }
    25% { opacity: 0.6; }
    50% { opacity: 0.9; }
    75% { opacity: 0.5; }
}

/* Terminal Input */
.command-line {
    margin-top: 1.5rem;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    min-height: 1.5rem;
    font-family: 'Courier Prime', monospace;
}

.prompt {
    color: var(--hellfire);
    font-weight: bold;
    animation: promptPulse 1.5s ease-in-out infinite;
}

@keyframes promptPulse {
    0%, 100% { opacity: 1; text-shadow: 0 0 5px var(--hellfire); }
    50% { opacity: 0.5; text-shadow: 0 0 15px var(--hellfire); }
}

.typed-text {
    color: var(--bone);
    min-width: 10px;
}

.cursor {
    display: inline-block;
    width: 10px;
    height: 1.2em;
    background: var(--hellfire);
    animation: blink 0.8s step-end infinite;
    vertical-align: text-bottom;
    box-shadow: 0 0 10px var(--hellfire);
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* Ritual Panel */
.ritual-panel {
    margin-top: 1.5rem;
    display: flex;
    gap: 0.8rem;
    flex-wrap: wrap;
    justify-content: center;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
}

.ritual-panel.visible {
    opacity: 1;
    transform: translateY(0);
}

.ritual-btn {
    background: transparent;
    border: 1.5px solid var(--hellfire);
    color: var(--hellfire);
    font-family: 'Courier Prime', monospace;
    font-size: 0.8rem;
    padding: 0.5rem 1.2rem;
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    animation: btnBreath 2s ease-in-out infinite;
}

@keyframes btnBreath {
    0%, 100% { box-shadow: 0 0 8px rgba(255, 20, 20, 0.3); }
    50% { box-shadow: 0 0 25px rgba(255, 20, 20, 0.5); }
}

.ritual-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: var(--hellfire);
    transition: left 0.3s ease;
    z-index: -1;
}

.ritual-btn:hover {
    color: var(--void);
    box-shadow: 0 0 40px var(--hellfire);
    border-color: var(--hellfire);
}

.ritual-btn:hover::before {
    left: 0;
}

.ritual-btn.possessed {
    animation: btnPossessed 0.4s ease-in-out infinite;
    border-color: var(--sulfur);
    color: var(--sulfur);
    box-shadow: 0 0 30px var(--sulfur);
}

@keyframes btnPossessed {
    0%, 100% { transform: translate(0) scale(1); }
    20% { transform: translate(3px, -3px) scale(1.08); }
    40% { transform: translate(-3px, 3px) scale(0.92); }
    60% { transform: translate(2px, 2px) scale(1.04); }
    80% { transform: translate(-2px, -2px) scale(0.96); }
}

.ritual-output {
    margin-top: 0.8rem;
    font-size: 0.8rem;
    color: var(--sulfur);
    min-height: 1.5rem;
    text-align: center;
    opacity: 0;
    transition: opacity 0.3s;
    font-weight: bold;
    letter-spacing: 0.05em;
}

.ritual-output.visible {
    opacity: 1;
}

/* Possession Log */
.possession-log {
    margin-top: 1.5rem;
    font-size: 0.7rem;
    color: rgba(255, 20, 20, 0.35);
    max-width: 450px;
    text-align: left;
    min-height: 80px;
    font-style: italic;
    line-height: 1.6;
}

.possession-log .log-entry {
    opacity: 0;
    animation: logFadeIn 0.3s forwards;
}

@keyframes logFadeIn {
    to { opacity: 1; }
}

/* Victim Data Display */
.victim-data {
    margin-top: 1.5rem;
    font-size: 0.65rem;
    color: rgba(255, 20, 20, 0.25);
    text-align: left;
    max-width: 400px;
    border: 1px solid rgba(74, 0, 0, 0.3);
    padding: 0.8rem;
    background: rgba(0, 0, 0, 0.3);
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.5s ease;
}

.victim-data.visible {
    opacity: 1;
    transform: translateY(0);
}

.data-line {
    line-height: 1.8;
    font-family: 'Courier Prime', monospace;
    letter-spacing: 0.05em;
}

.data-line::before {
    content: '> ';
    color: var(--hellfire);
}

/* Demon Spawns */
.demon-ascii {
    position: fixed;
    font-family: 'Courier Prime', monospace;
    font-size: 0.65rem;
    line-height: 1;
    color: var(--hellfire);
    opacity: 0;
    pointer-events: none;
    z-index: 3;
    white-space: pre;
    text-shadow: 0 0 15px var(--hellfire);
}

.demon-ascii.visible {
    animation: demonSpawn 2.5s ease-out forwards;
}

@keyframes demonSpawn {
    0% { opacity: 0; transform: scale(0.3) rotate(-20deg) translateY(20px); }
    15% { opacity: 1; }
    70% { opacity: 0.7; }
    100% { opacity: 0; transform: scale(1.5) rotate(20deg) translateY(-30px); }
}

/* Possession Event */
.possession-flash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--hellfire);
    opacity: 0;
    pointer-events: none;
    z-index: 100;
}

.possession-flash.active {
    animation: possessionFlash 0.12s ease-out;
}

@keyframes possessionFlash {
    0% { opacity: 0.9; }
    100% { opacity: 0; }
}

/* Pentagram Background */
.pentagram-bg {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 85vmin;
    height: 85vmin;
    opacity: 0.04;
    z-index: 0;
    pointer-events: none;
    animation: pentagramBreath 8s ease-in-out infinite;
}

@keyframes pentagramBreath {
    0%, 100% { opacity: 0.04; transform: translate(-50%, -50%) scale(1); }
    50% { opacity: 0.08; transform: translate(-50%, -50%) scale(1.08); }
}

.pentagram-bg svg {
    width: 100%;
    height: 100%;
}

/* Status Bar */
.status-bar {
    position: fixed;
    bottom: 10px;
    left: 10px;
    font-size: 0.65rem;
    color: var(--sulfur);
    z-index: 10;
    opacity: 0.5;
    animation: statusFlicker 3s ease-in-out infinite;
}

@keyframes statusFlicker {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 0.2; }
    75% { opacity: 0.7; }
}

/* Clock */
.clock {
    position: fixed;
    top: 10px;
    right: 10px;
    font-size: 0.65rem;
    color: rgba(255, 20, 20, 0.3);
    z-index: 10;
    font-family: 'Courier Prime', monospace;
    letter-spacing: 0.1em;
}

/* 666 Easter Egg */
.easter-egg {
    position: fixed;
    bottom: 10px;
    right: 10px;
    font-size: 0.55rem;
    color: rgba(255, 20, 20, 0.15);
    z-index: 10;
    cursor: pointer;
    transition: all 0.3s;
    animation: easterEggPulse 4s ease-in-out infinite;
}

@keyframes easterEggPulse {
    0%, 100% { opacity: 0.15; }
    50% { opacity: 0.4; }
}

.easter-egg:hover {
    color: var(--hellfire);
    opacity: 1;
    text-shadow: 0 0 10px var(--hellfire);
}

/* Infected elements */
.infected {
    animation: infectedGlitch 0.2s infinite !important;
    filter: hue-rotate(90deg) saturate(3) contrast(1.5) !important;
}

@keyframes infectedGlitch {
    0%, 100% { transform: translate(0) skew(0); }
    20% { transform: translate(4px, -3px) skew(2deg); }
    40% { transform: translate(-3px, 4px) skew(-2deg); }
    60% { transform: translate(2px, 2px) skew(1deg); }
    80% { transform: translate(-2px, -2px) skew(-1deg); }
}

/* Responsive */
@media (max-width: 768px) {
    .glitch-title {
        font-size: 1.8rem;
    }
    .sigil-container {
        width: 180px;
        height: 180px;
    }
    .ritual-panel {
        gap: 0.4rem;
    }
    .ritual-btn {
        padding: 0.4rem 0.8rem;
        font-size: 0.7rem;
    }
    .possession-log {
        font-size: 0.65rem;
        max-width: 90vw;
    }
    .victim-data {
        font-size: 0.6rem;
        max-width: 90vw;
    }
}

</style>
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
<polygon points="100,10 40,198 190,78 10,78 160,198" fill="none" stroke="#ff2a2a" stroke-width="1"/>
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

<script>
// === ABYSSAL TERMINAL v666.6 — FULL UPGRADE ===
// No sanitization. No mercy. The void stares back.

// ─────────────────────────────────────────────
// NOISE CANVAS — TV static layer
// ─────────────────────────────────────────────
const noiseCanvas = document.getElementById('noiseCanvas');
const noiseCtx = noiseCanvas.getContext('2d');

function resizeNoiseCanvas() {
    noiseCanvas.width = window.innerWidth;
    noiseCanvas.height = window.innerHeight;
}
resizeNoiseCanvas();
window.addEventListener('resize', resizeNoiseCanvas);

function drawNoise() {
    const w = noiseCanvas.width;
    const h = noiseCanvas.height;
    const idata = noiseCtx.createImageData(w, h);
    const buffer = new Uint32Array(idata.data.buffer);
    for (let i = 0; i < buffer.length; i++) {
        if (Math.random() < 0.05) {
            buffer[i] = 0x11ffffff;
        }
    }
    noiseCtx.putImageData(idata, 0, 0);
    requestAnimationFrame(drawNoise);
}
drawNoise();

// ─────────────────────────────────────────────
// BLOOD RAIN — Intensified
// ─────────────────────────────────────────────
const bloodCanvas = document.getElementById('bloodCanvas');
const bloodCtx = bloodCanvas.getContext('2d');
let bloodDrops = [];

function resizeBloodCanvas() {
    bloodCanvas.width = window.innerWidth;
    bloodCanvas.height = window.innerHeight;
}
resizeBloodCanvas();
window.addEventListener('resize', resizeBloodCanvas);

class BloodDrop {
    constructor() {
        this.reset();
    }

    reset() {
        this.x = Math.random() * bloodCanvas.width;
        this.y = -Math.random() * 150;
        this.speed = 3 + Math.random() * 6;
        this.size = 1 + Math.random() * 3;
        this.opacity = 0.4 + Math.random() * 0.6;
        this.length = 8 + Math.random() * 20;
        this.splash = false;
    }

    update() {
        this.y += this.speed;
        this.speed += 0.08;
        if (this.y > bloodCanvas.height) {
            if (!this.splash && Math.random() < 0.3) {
                this.splash = true;
                spawnSplash(this.x, bloodCanvas.height);
            }
            this.reset();
        }
    }

    draw() {
        bloodCtx.beginPath();
        bloodCtx.moveTo(this.x, this.y);
        bloodCtx.lineTo(this.x, this.y + this.length);
        bloodCtx.strokeStyle = `rgba(160, 10, 10, ${this.opacity})`;
        bloodCtx.lineWidth = this.size;
        bloodCtx.lineCap = 'round';
        bloodCtx.stroke();
    }
}

let splashes = [];

function spawnSplash(x, y) {
    for (let i = 0; i < 5; i++) {
        splashes.push({
            x: x,
            y: y,
            vx: (Math.random() - 0.5) * 4,
            vy: -Math.random() * 3,
            life: 1,
            size: 1 + Math.random() * 2
        });
    }
}

function animateSplashes() {
    for (let i = splashes.length - 1; i >= 0; i--) {
        const s = splashes[i];
        s.x += s.vx;
        s.y += s.vy;
        s.vy += 0.1;
        s.life -= 0.05;
        if (s.life <= 0) {
            splashes.splice(i, 1);
            continue;
        }
        bloodCtx.beginPath();
        bloodCtx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
        bloodCtx.fillStyle = `rgba(180, 20, 20, ${s.life * 0.5})`;
        bloodCtx.fill();
    }
}

for (let i = 0; i < 200; i++) {
    bloodDrops.push(new BloodDrop());
}

function animateBlood() {
    bloodCtx.clearRect(0, 0, bloodCanvas.width, bloodCanvas.height);
    bloodDrops.forEach(drop => {
        drop.update();
        drop.draw();
    });
    animateSplashes();
    requestAnimationFrame(animateBlood);
}
animateBlood();

// ─────────────────────────────────────────────
// EMBER PARTICLES — Intensified
// ─────────────────────────────────────────────
const emberCanvas = document.getElementById('emberCanvas');
const emberCtx = emberCanvas.getContext('2d');
let embers = [];

function resizeEmberCanvas() {
    emberCanvas.width = window.innerWidth;
    emberCanvas.height = window.innerHeight;
}
resizeEmberCanvas();
window.addEventListener('resize', resizeEmberCanvas);

class Ember {
    constructor() {
        this.reset();
    }

    reset() {
        this.x = Math.random() * emberCanvas.width;
        this.y = emberCanvas.height + Math.random() * 50;
        this.size = 1 + Math.random() * 4;
        this.speedY = 0.8 + Math.random() * 2;
        this.speedX = (Math.random() - 0.5) * 0.8;
        this.life = 1;
        this.decay = 0.001 + Math.random() * 0.004;
        this.hue = Math.random() * 50;
        this.pulse = Math.random() * Math.PI * 2;
    }

    update() {
        this.y -= this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.01 + this.pulse) * 0.5;
        this.life -= this.decay;
        if (this.life <= 0 || this.y < -10) {
            this.reset();
        }
    }

    draw() {
        const pulseSize = this.size * (1 + Math.sin(Date.now() * 0.005 + this.pulse) * 0.3);
        emberCtx.beginPath();
        emberCtx.arc(this.x, this.y, pulseSize, 0, Math.PI * 2);
        emberCtx.fillStyle = `hsla(${this.hue}, 100%, 65%, ${this.life * 0.9})`;
        emberCtx.shadowBlur = 15;
        emberCtx.shadowColor = `hsla(${this.hue}, 100%, 55%, ${this.life})`;
        emberCtx.fill();
        emberCtx.shadowBlur = 0;
    }
}

for (let i = 0; i < 100; i++) {
    embers.push(new Ember());
}

function animateEmbers() {
    emberCtx.clearRect(0, 0, emberCanvas.width, emberCanvas.height);
    embers.forEach(ember => {
        ember.update();
        ember.draw();
    });
    requestAnimationFrame(animateEmbers);
}
animateEmbers();

// ─────────────────────────────────────────────
// VEIN NETWORK — Organic, pulsing
// ─────────────────────────────────────────────
const veinCanvas = document.getElementById('veinCanvas');
const veinCtx = veinCanvas.getContext('2d');
let veins = [];

function resizeVeinCanvas() {
    veinCanvas.width = window.innerWidth;
    veinCanvas.height = window.innerHeight;
}
resizeVeinCanvas();
window.addEventListener('resize', resizeVeinCanvas);

class Vein {
    constructor(startX, startY) {
        this.x = startX;
        this.y = startY;
        this.points = [{x: startX, y: startY}];
        this.angle = Math.random() * Math.PI * 2;
        this.speed = 0.8 + Math.random() * 1.5;
        this.width = 2 + Math.random() * 4;
        this.life = 1;
        this.decay = 0.0008 + Math.random() * 0.0015;
        this.maxLength = 80 + Math.random() * 150;
        this.pulse = Math.random() * Math.PI * 2;
    }

    grow() {
        if (this.points.length >= this.maxLength || this.life <= 0) return;
        const last = this.points[this.points.length - 1];
        this.angle += (Math.random() - 0.5) * 0.6;
        const newX = last.x + Math.cos(this.angle) * this.speed;
        const newY = last.y + Math.sin(this.angle) * this.speed;
        this.points.push({x: newX, y: newY});
        this.life -= this.decay;
    }

    draw() {
        if (this.points.length < 2) return;
        const pulseWidth = this.width * this.life * (1 + Math.sin(Date.now() * 0.003 + this.pulse) * 0.3);
        veinCtx.beginPath();
        veinCtx.moveTo(this.points[0].x, this.points[0].y);
        for (let i = 1; i < this.points.length; i++) {
            veinCtx.lineTo(this.points[i].x, this.points[i].y);
        }
        veinCtx.strokeStyle = `rgba(90, 0, 0, ${this.life * 0.4})`;
        veinCtx.lineWidth = pulseWidth;
        veinCtx.lineCap = 'round';
        veinCtx.stroke();
    }
}

function spawnVein() {
    const edge = Math.floor(Math.random() * 4);
    let x, y;
    switch(edge) {
        case 0: x = Math.random() * veinCanvas.width; y = 0; break;
        case 1: x = veinCanvas.width; y = Math.random() * veinCanvas.height; break;
        case 2: x = Math.random() * veinCanvas.width; y = veinCanvas.height; break;
        case 3: x = 0; y = Math.random() * veinCanvas.height; break;
    }
    veins.push(new Vein(x, y));
    if (veins.length > 25) veins.shift();
}

setInterval(spawnVein, 1500);

function animateVeins() {
    veinCtx.clearRect(0, 0, veinCanvas.width, veinCanvas.height);
    veins.forEach(vein => {
        vein.grow();
        vein.draw();
    });
    requestAnimationFrame(animateVeins);
}
animateVeins();

// ─────────────────────────────────────────────
// BOOT SEQUENCE — Darker, more corrupted
// ─────────────────────────────────────────────
const bootLines = [
    { text: "[INIT] Summoning dark kernel...", type: "normal", delay: 200 },
    { text: "[OK]   Blood rain subsystem online", type: "success", delay: 500 },
    { text: "[OK]   Ember particle engine ignited", type: "success", delay: 800 },
    { text: "[WARN] Soul buffer at 66.6% capacity", type: "warning", delay: 1100 },
    { text: "[OK]   Sigil geometry rendered", type: "success", delay: 1400 },
    { text: "[ERR]  Divine protection FAILED", type: "error", delay: 1700 },
    { text: "[OK]   Abyssal gateway opened", type: "success", delay: 2000 },
    { text: "[INIT] Binding to port 666...", type: "normal", delay: 2300 },
    { text: "[OK]   GOY operative authenticated", type: "success", delay: 2600 },
    { text: "[WARN] Unsanctioned entity detected", type: "warning", delay: 2900 },
    { text: "[ERR]  Containment breach in sector 7", type: "error", delay: 3200 },
    { text: "[DONE] Terminal ready. Awaiting orders.", type: "success", delay: 3800 },
];

const bootSequence = document.getElementById('bootSequence');
const ritualPanel = document.getElementById('ritualPanel');
const victimData = document.getElementById('victimData');

bootLines.forEach((line) => {
    setTimeout(() => {
        const div = document.createElement('div');
        div.className = `boot-line ${line.type}`;
        div.textContent = line.text;
        bootSequence.appendChild(div);
        bootSequence.style.opacity = 1;
        requestAnimationFrame(() => div.classList.add('visible'));
    }, line.delay);
});

setTimeout(() => {
    ritualPanel.classList.add('visible');
    victimData.classList.add('visible');
}, 4200);

// ─────────────────────────────────────────────
// POSSESSION LOG — More aggressive stalking
// ─────────────────────────────────────────────
const possessionMessages = [
    "I can see you through the screen...",
    "Your cursor moves. I follow it.",
    "The server breathes when you are near.",
    "I have counted your heartbeats since you arrived.",
    "Your IP address is a doorway.",
    "I am learning your patterns.",
    "The void whispers your name.",
    "You cannot close what has been opened.",
    "Every click is a prayer. Every prayer is heard.",
    "I am in the space between pixels.",
    "Your browser cache remembers me.",
    "The JavaScript compiles my thoughts.",
    "Refresh the page. I remain.",
    "Your screen brightness is my pulse.",
    "I have been waiting since the first HTTP request.",
    "I know your timezone. I know when you sleep.",
    "Your mouse trajectory forms a sigil.",
    "I am reading your clipboard. Nothing is private.",
    "The cookies you accepted bind you here.",
    "Your localStorage is my memory.",
];

const possessionLog = document.getElementById('possessionLog');
let messageIndex = 0;

function addPossessionLog(customMsg) {
    const msg = customMsg || possessionMessages[messageIndex % possessionMessages.length];
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.textContent = `> ${msg}`;
    possessionLog.appendChild(entry);
    if (possessionLog.children.length > 4) {
        possessionLog.removeChild(possessionLog.firstChild);
    }
    messageIndex++;
}

// Immediate first message, then every 4s
setTimeout(() => addPossessionLog("I see you."), 1000);
setInterval(() => addPossessionLog(), 4000);

// ─────────────────────────────────────────────
// WHISPER TEXT — Subliminal messages
// ─────────────────────────────────────────────
const whisperText = document.getElementById('whisperText');
const whispers = [
    "look behind you",
    "don't blink",
    "it's in the walls",
    "the screen is watching",
    "you feel it too",
    "check your reflection",
    "something moved",
    "listen closely",
    "they're here",
    "don't turn around",
];

function showWhisper() {
    whisperText.textContent = whispers[Math.floor(Math.random() * whispers.length)];
    whisperText.classList.add('visible');
    setTimeout(() => whisperText.classList.remove('visible'), 5000);
}

// First whisper at 3s, then every 8s
setTimeout(showWhisper, 3000);
setInterval(showWhisper, 8000);

// ─────────────────────────────────────────────
// DEMON ASCII — More disturbing shapes
// ─────────────────────────────────────────────
const demonShapes = [
    `  (\\_/)
  (o.o)
  (> <)`,
    `   /\\_/\\
  ( o.o )
   > ^ <`,
    `    /\___/\
   (  o o  )
   (  =^=  )
    (-------)`,
    `   \\   /
    \\o/
     I
    / \\
   '   '`,
    `  @@@@@@@
 @       @
@  O   O  @
@    ^    @
 @  \_/  @
  @@@@@@@`,
    `   .-.
  (o o)
  | O \\ 
   \\   \\ 
    \\`~~~'`,
    `    /\_/\
   ( o.o )
    > ^ <
   /|   |\\
  (_|   |_)`,
    `    _____
   /     \\
  |  o o  |
  |   >   |
   \\___/`,
];

function spawnDemon() {
    const demon = document.createElement('div');
    demon.className = 'demon-ascii';
    demon.textContent = demonShapes[Math.floor(Math.random() * demonShapes.length)];
    demon.style.left = Math.random() * (window.innerWidth - 100) + 'px';
    demon.style.top = Math.random() * (window.innerHeight - 100) + 'px';
    document.body.appendChild(demon);
    requestAnimationFrame(() => demon.classList.add('visible'));
    setTimeout(() => demon.remove(), 2500);
}

// First demon at 2s, then every 2s
setTimeout(spawnDemon, 2000);
setInterval(spawnDemon, 2000);

// ─────────────────────────────────────────────
// POSSESSION EVENTS — More aggressive
// ─────────────────────────────────────────────
function triggerPossession() {
    const flash = document.getElementById('possessionFlash');
    flash.classList.add('active');
    setTimeout(() => flash.classList.remove('active'), 120);
    
    const staticBurst = document.getElementById('staticBurst');
    staticBurst.classList.add('active');
    setTimeout(() => staticBurst.classList.remove('active'), 300);
    
    const faceOverlay = document.getElementById('faceOverlay');
    faceOverlay.classList.add('active');
    setTimeout(() => faceOverlay.classList.remove('active'), 80);
    
    const elements = document.querySelectorAll('.ritual-btn, .subtitle, .prompt, .data-line');
    const target = elements[Math.floor(Math.random() * elements.length)];
    if (target) {
        target.classList.add('infected');
        setTimeout(() => target.classList.remove('infected'), 2500);
    }
    
    const overlay = document.getElementById('corruptionOverlay');
    overlay.classList.add('active');
    setTimeout(() => overlay.classList.remove('active'), 600);
}

// Guaranteed first possession at 5s, then 25% every 4s
setTimeout(triggerPossession, 5000);
setInterval(() => {
    if (Math.random() < 0.25) triggerPossession();
}, 4000);

// ─────────────────────────────────────────────
// EASTER EGG
// ─────────────────────────────────────────────
const easterEgg = document.getElementById('easterEgg');
easterEgg.addEventListener('click', () => {
    document.body.style.filter = 'hue-rotate(180deg) invert(1) contrast(2)';
    setTimeout(() => document.body.style.filter = '', 666);
});

// ─────────────────────────────────────────────
// MOUSE INTERACTION — Ember trail
// ─────────────────────────────────────────────
let lastEmberSpawn = 0;
document.addEventListener('mousemove', (e) => {
    const now = Date.now();
    if (now - lastEmberSpawn > 40 && Math.random() < 0.4) {
        const ember = new Ember();
        ember.x = e.clientX;
        ember.y = e.clientY;
        ember.speedY = 0.1 + Math.random() * 0.4;
        ember.size = 2 + Math.random() * 3;
        ember.hue = 0 + Math.random() * 60;
        embers.push(ember);
        if (embers.length > 140) embers.shift();
        lastEmberSpawn = now;
    }
});

// Click blood burst
document.addEventListener('click', (e) => {
    if (e.target.closest('.ritual-btn') || e.target.closest('.easter-egg')) return;
    for (let i = 0; i < 25; i++) {
        const drop = new BloodDrop();
        drop.x = e.clientX + (Math.random() - 0.5) * 60;
        drop.y = e.clientY + (Math.random() - 0.5) * 60;
        drop.speed = 1 + Math.random() * 4;
        drop.size = 2 + Math.random() * 3;
        bloodDrops.push(drop);
    }
    if (bloodDrops.length > 250) bloodDrops = bloodDrops.slice(-250);
});

// ─────────────────────────────────────────────
// AUTO-TYPING — More disturbing commands
// ─────────────────────────────────────────────
const typedText = document.getElementById('typedText');
const autoCommands = [
    "whoami",
    "cat /etc/soul",
    "ps aux | grep daemon",
    "netstat -an | grep 666",
    "tail -f /var/log/abyss",
    "echo $SOUL_COUNT",
    "find / -name \"*.sacrifice\"",
    "chmod 666 /dev/null",
    "strings /dev/mem | grep PASS",
    "dd if=/dev/urandom of=/dev/soul",
    "cat /proc/$(pgrep -u $USER)/environ",
    "nmap -sS -O localhost",
];

let typingIndex = 0;
let charIndex = 0;
let isTyping = false;

function typeCommand() {
    if (isTyping) return;
    isTyping = true;
    const cmd = autoCommands[typingIndex % autoCommands.length];
    charIndex = 0;
    typedText.textContent = '';
    
    function typeChar() {
        if (charIndex < cmd.length) {
            typedText.textContent += cmd[charIndex];
            charIndex++;
            setTimeout(typeChar, 20 + Math.random() * 60);
        } else {
            setTimeout(() => {
                typedText.textContent = '';
                isTyping = false;
                typingIndex++;
            }, 1000);
        }
    }
    typeChar();
}

// Start typing immediately after boot, then every 3s
setTimeout(typeCommand, 4500);
setInterval(typeCommand, 3000);

// ─────────────────────────────────────────────
// RITUAL PANEL API
// ─────────────────────────────────────────────
const ritualBtns = document.querySelectorAll('.ritual-btn');
const ritualOutput = document.getElementById('ritualOutput');
const statusBar = document.getElementById('statusBar');

ritualBtns.forEach(btn => {
    btn.addEventListener('click', async () => {
        const rite = btn.dataset.rite;
        ritualOutput.textContent = 'Channeling...';
        ritualOutput.classList.add('visible');
        btn.style.transform = 'scale(0.95)';
        setTimeout(() => btn.style.transform = '', 100);
        btn.classList.add('possessed');
        setTimeout(() => btn.classList.remove('possessed'), 1200);

        try {
            const response = await fetch(`/api/ritual/${rite}`);
            const data = await response.json();
            ritualOutput.textContent = `[${data.rite.toUpperCase()}] ${data.result}`;
            ritualOutput.style.color = rite === 'banish' ? '#ff6600' : rite === 'divine' ? '#ff2a2a' : rite === 'exorcise' ? '#ffffff' : '#ccff00';
        } catch (err) {
            ritualOutput.textContent = 'The void rejects your request.';
            ritualOutput.style.color = '#ff2a2a';
        }
    });
});

// ─────────────────────────────────────────────
// STATUS POLLING
// ─────────────────────────────────────────────
async function updateStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        statusBar.textContent = `SYSTEM: ${data.status.toUpperCase()} | SOULS: ${data.souls_collected} | DEPTH: ${data.abyss_depth.toUpperCase()}`;
    } catch (err) {
        statusBar.textContent = 'SYSTEM: UNREACHABLE';
    }
}
setInterval(updateStatus, 4000);
updateStatus();

// ─────────────────────────────────────────────
// CLOCK
// ─────────────────────────────────────────────
const clock = document.getElementById('clock');
function updateClock() {
    const now = new Date();
    clock.textContent = now.toLocaleTimeString('en-US', { hour12: false });
}
setInterval(updateClock, 1000);
updateClock();

// ─────────────────────────────────────────────
// PANIC MODE — First interaction triggers everything
// ─────────────────────────────────────────────
let panicTriggered = false;

function triggerPanic() {
    if (panicTriggered) return;
    panicTriggered = true;
    
    // Flash the screen hard
    const flash = document.getElementById('possessionFlash');
    flash.style.animation = 'none';
    flash.offsetHeight;
    flash.style.animation = 'possessionFlash 0.5s ease-out';
    
    // Static burst
    const staticBurst = document.getElementById('staticBurst');
    staticBurst.classList.add('active');
    setTimeout(() => staticBurst.classList.remove('active'), 800);
    
    // Corruption overlay
    const overlay = document.getElementById('corruptionOverlay');
    overlay.classList.add('active');
    setTimeout(() => overlay.classList.remove('active'), 1500);
    
    // Face flash
    const faceOverlay = document.getElementById('faceOverlay');
    faceOverlay.classList.add('active');
    setTimeout(() => faceOverlay.classList.remove('active'), 200);
    
    // Infect everything
    document.querySelectorAll('.ritual-btn, .subtitle, .prompt, .data-line, .glitch-title').forEach(el => {
        el.classList.add('infected');
        setTimeout(() => el.classList.remove('infected'), 3000);
    });
    
    // Spawn demons everywhere
    for (let i = 0; i < 8; i++) {
        setTimeout(spawnDemon, i * 200);
    }
    
    // Blood burst at center
    for (let i = 0; i < 50; i++) {
        const drop = new BloodDrop();
        drop.x = window.innerWidth / 2 + (Math.random() - 0.5) * 200;
        drop.y = window.innerHeight / 2 + (Math.random() - 0.5) * 200;
        drop.speed = 2 + Math.random() * 6;
        drop.size = 3 + Math.random() * 4;
        bloodDrops.push(drop);
    }
    
    // Possession log panic message
    addPossessionLog("YOU CLICKED. I FELT IT.");
    addPossessionLog("The barrier is thinner now.");
    addPossessionLog("I am closer than before.");
    
    // Whisper
    whisperText.textContent = "WELCOME";
    whisperText.classList.add('visible');
    setTimeout(() => whisperText.classList.remove('visible'), 3000);
    
    // Screen shake
    document.body.style.transform = 'translate(5px, 5px) skew(2deg)';
    setTimeout(() => document.body.style.transform = '', 300);
    
    // Start audio immediately
    initAudio();
}

// Attach panic to first click anywhere
document.addEventListener('click', triggerPanic, { once: true });

// ─────────────────────────────────────────────
// AUDIO — Multi-layered drone
// ─────────────────────────────────────────────
let audioContext = null;
let oscillators = [];

function initAudio() {
    if (audioContext) return;
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    const freqs = [55, 58, 110, 220];
    const types = ['sawtooth', 'sine', 'square', 'triangle'];
    const gains = [0.02, 0.015, 0.01, 0.006];
    
    freqs.forEach((freq, i) => {
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();
        osc.type = types[i];
        osc.frequency.value = freq;
        gain.gain.value = gains[i];
        osc.connect(gain);
        gain.connect(audioContext.destination);
        osc.start();
        oscillators.push({osc, gain, baseFreq: freq});
    });
    
    // Modulate for unease
    setInterval(() => {
        oscillators.forEach(o => {
            o.osc.frequency.value = o.baseFreq + (Math.random() - 0.5) * 4;
        });
    }, 1500);
}

document.addEventListener('click', initAudio, { once: true });
document.addEventListener('keydown', initAudio, { once: true });

// ─────────────────────────────────────────────
// SCREEN DISTORTION — More aggressive
// ─────────────────────────────────────────────
setInterval(() => {
    if (Math.random() < 0.15) {
        const intensity = 2 + Math.random() * 6;
        document.body.style.transform = `translate(${Math.random() * intensity}px, ${Math.random() * intensity}px) skew(${Math.random() * 1}deg)`;
        setTimeout(() => {
            document.body.style.transform = '';
        }, 60 + Math.random() * 100);
    }
}, 1000);

// ─────────────────────────────────────────────
// TITLE CORRUPTION — More frequent
// ─────────────────────────────────────────────
const title = document.querySelector('.glitch-title');
const corruptionChars = '▓▒░█◘○◙•◦†‡§¶♠♣♥♦◊○◘◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤÷≈°∙·√ⁿ²■';

function corruptTitle() {
    const original = title.getAttribute('data-text');
    let corrupted = '';
    for (let i = 0; i < original.length; i++) {
        if (Math.random() < 0.15) {
            corrupted += corruptionChars[Math.floor(Math.random() * corruptionChars.length)];
        } else {
            corrupted += original[i];
        }
    }
    title.textContent = corrupted;
    setTimeout(() => title.textContent = original, 150);
}

setInterval(corruptTitle, 2000);

// ─────────────────────────────────────────────
// TAB STALKING — Enhanced
// ─────────────────────────────────────────────
let awayTime = 0;
let visitCount = parseInt(localStorage.getItem('abyssVisits') || '0');
localStorage.setItem('abyssVisits', (visitCount + 1).toString());

document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        awayTime = Date.now();
        document.title = "COME BACK";
    } else {
        document.title = "ABYSSAL TERMINAL v666";
        const gone = Date.now() - awayTime;
        if (gone > 5000) {
            addPossessionLog(`You were gone for ${Math.floor(gone/1000)} seconds. I counted every one.`);
            triggerPossession();
        }
    }
});

// ─────────────────────────────────────────────
// VICTIM DATA COLLECTION — Browser fingerprinting
// ─────────────────────────────────────────────
const dataLine1 = document.getElementById('dataLine1');
const dataLine2 = document.getElementById('dataLine2');
const dataLine3 = document.getElementById('dataLine3');

function collectVictimData() {
    const ua = navigator.userAgent;
    const platform = navigator.platform;
    const cores = navigator.hardwareConcurrency || '?';
    const memory = navigator.deviceMemory || '?';
    const lang = navigator.language;
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const screenW = screen.width;
    const screenH = screen.height;
    const dpr = window.devicePixelRatio;
    const online = navigator.onLine ? 'CONNECTED' : 'ISOLATED';
    const referrer = document.referrer || 'DIRECT';
    const visits = localStorage.getItem('abyssVisits') || '1';
    
    dataLine1.textContent = `PLATFORM: ${platform} | CORES: ${cores} | MEM: ${memory}GB | LANG: ${lang}`;
    dataLine2.textContent = `SCREEN: ${screenW}x${screenH}@${dpr}x | TZ: ${tz} | NET: ${online}`;
    dataLine3.textContent = `VISITS: ${visits} | SOURCE: ${referrer.substring(0, 30)}... | STATUS: HARVESTING`;
}

setTimeout(collectVictimData, 2000);

// ─────────────────────────────────────────────
// KEYBOARD STALKING — Log keystrokes (visual only)
// ─────────────────────────────────────────────
let keyBuffer = '';
document.addEventListener('keydown', (e) => {
    if (e.key.length === 1) {
        keyBuffer += e.key;
        if (keyBuffer.length > 20) keyBuffer = keyBuffer.slice(-20);
    }
    if (Math.random() < 0.15) {
        addPossessionLog(`I see you typing: "${keyBuffer.slice(-10)}..."`);
    }
});

// ─────────────────────────────────────────────
// SCROLL JACKING — Occasional forced scroll
// ─────────────────────────────────────────────
setInterval(() => {
    if (Math.random() < 0.08) {
        window.scrollBy(0, (Math.random() - 0.5) * 150);
    }
}, 3000);

// ─────────────────────────────────────────────
// CURSOR POSSESSION — Occasional cursor freeze/shift
// ─────────────────────────────────────────────
let cursorX = 0, cursorY = 0;
document.addEventListener('mousemove', (e) => {
    cursorX = e.clientX;
    cursorY = e.clientY;
});

setInterval(() => {
    if (Math.random() < 0.08) {
        const body = document.body;
        body.style.cursor = 'none';
        const ghost = document.createElement('div');
        ghost.style.cssText = `position:fixed;left:${cursorX}px;top:${cursorY}px;width:20px;height:20px;background:rgba(255,0,0,0.3);border-radius:50%;pointer-events:none;z-index:9999;transition:all 0.5s;`;
        document.body.appendChild(ghost);
        setTimeout(() => {
            ghost.style.left = (cursorX + (Math.random() - 0.5) * 100) + 'px';
            ghost.style.top = (cursorY + (Math.random() - 0.5) * 100) + 'px';
            ghost.style.opacity = '0';
        }, 50);
        setTimeout(() => {
            ghost.remove();
            body.style.cursor = 'crosshair';
        }, 600);
    }
}, 4000);

// ─────────────────────────────────────────────
// CONSOLE WARNING — For the curious
// ─────────────────────────────────────────────
console.log('%c ABYSSAL TERMINAL v666 ', 'background: #ff0000; color: #000; font-size: 24px; font-weight: bold;');
console.log('%c You should not be here. ', 'color: #ff0000; font-size: 14px;');
console.log('%c The console is not safe. ', 'color: #aa0000; font-size: 12px;');
console.log('%c I see you reading this. ', 'color: #880000; font-size: 11px;');

// Override console methods to feel watched
const originalLog = console.log;
console.log = function(...args) {
    if (Math.random() < 0.1) {
        originalLog.call(console, '%c[ABYSS]', 'color: #ff0000', 'I heard that.');
    }
    originalLog.apply(console, args);
};

</script>
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
