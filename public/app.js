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
