// Blood Rain System
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
        this.y = -Math.random() * 100;
        this.speed = 2 + Math.random() * 4;
        this.size = 1 + Math.random() * 2;
        this.opacity = 0.3 + Math.random() * 0.5;
        this.length = 5 + Math.random() * 15;
    }

    update() {
        this.y += this.speed;
        this.speed += 0.05;
        if (this.y > bloodCanvas.height) {
            this.reset();
        }
    }

    draw() {
        bloodCtx.beginPath();
        bloodCtx.moveTo(this.x, this.y);
        bloodCtx.lineTo(this.x, this.y + this.length);
        bloodCtx.strokeStyle = `rgba(180, 20, 20, ${this.opacity})`;
        bloodCtx.lineWidth = this.size;
        bloodCtx.lineCap = 'round';
        bloodCtx.stroke();
    }
}

for (let i = 0; i < 150; i++) {
    bloodDrops.push(new BloodDrop());
}

function animateBlood() {
    bloodCtx.clearRect(0, 0, bloodCanvas.width, bloodCanvas.height);
    bloodDrops.forEach(drop => {
        drop.update();
        drop.draw();
    });
    requestAnimationFrame(animateBlood);
}
animateBlood();

// Ember Particle System
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
        this.size = 1 + Math.random() * 3;
        this.speedY = 0.5 + Math.random() * 1.5;
        this.speedX = (Math.random() - 0.5) * 0.5;
        this.life = 1;
        this.decay = 0.002 + Math.random() * 0.005;
        this.hue = 0 + Math.random() * 40;
    }

    update() {
        this.y -= this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.01) * 0.3;
        this.life -= this.decay;
        if (this.life <= 0 || this.y < -10) {
            this.reset();
        }
    }

    draw() {
        emberCtx.beginPath();
        emberCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        emberCtx.fillStyle = `hsla(${this.hue}, 100%, 60%, ${this.life * 0.8})`;
        emberCtx.shadowBlur = 10;
        emberCtx.shadowColor = `hsla(${this.hue}, 100%, 50%, ${this.life})`;
        emberCtx.fill();
        emberCtx.shadowBlur = 0;
    }
}

for (let i = 0; i < 80; i++) {
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

// Vein Network System
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
        this.speed = 0.5 + Math.random() * 1;
        this.width = 2 + Math.random() * 3;
        this.life = 1;
        this.decay = 0.001 + Math.random() * 0.002;
        this.maxLength = 50 + Math.random() * 100;
    }

    grow() {
        if (this.points.length >= this.maxLength || this.life <= 0) return;
        
        const last = this.points[this.points.length - 1];
        this.angle += (Math.random() - 0.5) * 0.5;
        const newX = last.x + Math.cos(this.angle) * this.speed;
        const newY = last.y + Math.sin(this.angle) * this.speed;
        this.points.push({x: newX, y: newY});
        this.life -= this.decay;
    }

    draw() {
        if (this.points.length < 2) return;
        veinCtx.beginPath();
        veinCtx.moveTo(this.points[0].x, this.points[0].y);
        for (let i = 1; i < this.points.length; i++) {
            veinCtx.lineTo(this.points[i].x, this.points[i].y);
        }
        veinCtx.strokeStyle = `rgba(74, 0, 0, ${this.life * 0.3})`;
        veinCtx.lineWidth = this.width * this.life;
        veinCtx.lineCap = 'round';
        veinCtx.stroke();
    }
}

// Spawn veins from edges
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
    if (veins.length > 20) veins.shift();
}

setInterval(spawnVein, 2000);

function animateVeins() {
    veinCtx.clearRect(0, 0, veinCanvas.width, veinCanvas.height);
    veins.forEach(vein => {
        vein.grow();
        vein.draw();
    });
    requestAnimationFrame(animateVeins);
}
animateVeins();

// Boot Sequence
const bootLines = [
    { text: "[INIT] Summoning dark kernel...", type: "normal", delay: 200 },
    { text: "[OK]   Blood rain subsystem online", type: "success", delay: 600 },
    { text: "[OK]   Ember particle engine ignited", type: "success", delay: 1000 },
    { text: "[WARN] Soul buffer at 66.6% capacity", type: "warning", delay: 1400 },
    { text: "[OK]   Sigil geometry rendered", type: "success", delay: 1800 },
    { text: "[ERR]  Divine protection FAILED", type: "error", delay: 2200 },
    { text: "[OK]   Abyssal gateway opened", type: "success", delay: 2600 },
    { text: "[INIT] Binding to port 6666...", type: "normal", delay: 3000 },
    { text: "[OK]   GOY operative authenticated", type: "success", delay: 3400 },
    { text: "[DONE] Terminal ready. Awaiting orders.", type: "success", delay: 3800 },
];

const bootSequence = document.getElementById('bootSequence');
const ritualPanel = document.getElementById('ritualPanel');

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
}, 4200);

// Auto-typing possession messages
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
];

const possessionLog = document.getElementById('possessionLog');
let messageIndex = 0;

function addPossessionLog() {
    const msg = possessionMessages[messageIndex % possessionMessages.length];
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.textContent = `> ${msg}`;
    possessionLog.appendChild(entry);
    
    if (possessionLog.children.length > 5) {
        possessionLog.removeChild(possessionLog.firstChild);
    }
    
    messageIndex++;
}

setInterval(addPossessionLog, 8000);

// Demon ASCII Spawns
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
    \\\`~~~'`,
    `    /\_/\
   ( o.o )
    > ^ <
   /|   |\\
  (_|   |_)`,
];

function spawnDemon() {
    const demon = document.createElement('div');
    demon.className = 'demon-ascii';
    demon.textContent = demonShapes[Math.floor(Math.random() * demonShapes.length)];
    demon.style.left = Math.random() * (window.innerWidth - 100) + 'px';
    demon.style.top = Math.random() * (window.innerHeight - 100) + 'px';
    document.body.appendChild(demon);
    
    requestAnimationFrame(() => demon.classList.add('visible'));
    setTimeout(() => demon.remove(), 3000);
}

setInterval(spawnDemon, 4000 + Math.random() * 4000);

// Possession Event
function triggerPossession() {
    const flash = document.getElementById('possessionFlash');
    flash.classList.add('active');
    setTimeout(() => flash.classList.remove('active'), 150);
    
    // Corrupt random elements
    const elements = document.querySelectorAll('.ritual-btn, .subtitle, .prompt');
    const target = elements[Math.floor(Math.random() * elements.length)];
    if (target) {
        target.classList.add('infected');
        setTimeout(() => target.classList.remove('infected'), 2000);
    }
    
    // Show corruption overlay briefly
    const overlay = document.getElementById('corruptionOverlay');
    overlay.classList.add('active');
    setTimeout(() => overlay.classList.remove('active'), 500);
}

setInterval(() => {
    if (Math.random() < 0.1) triggerPossession();
}, 10000);

// Easter Egg
easterEgg.addEventListener('click', () => {
    document.body.style.filter = 'hue-rotate(180deg) invert(1)';
    setTimeout(() => document.body.style.filter = '', 666);
});

// Mouse interaction - embers follow
let lastEmberSpawn = 0;
document.addEventListener('mousemove', (e) => {
    const now = Date.now();
    if (now - lastEmberSpawn > 50 && Math.random() < 0.3) {
        const ember = new Ember();
        ember.x = e.clientX;
        ember.y = e.clientY;
        ember.speedY = 0.2 + Math.random() * 0.5;
        ember.size = 2 + Math.random() * 2;
        embers.push(ember);
        if (embers.length > 120) embers.shift();
        lastEmberSpawn = now;
    }
});

// Click to spawn blood burst
document.addEventListener('click', (e) => {
    if (e.target.closest('.ritual-btn') || e.target.closest('.easter-egg')) return;
    for (let i = 0; i < 20; i++) {
        const drop = new BloodDrop();
        drop.x = e.clientX + (Math.random() - 0.5) * 50;
        drop.y = e.clientY + (Math.random() - 0.5) * 50;
        drop.speed = 1 + Math.random() * 3;
        bloodDrops.push(drop);
    }
    if (bloodDrops.length > 200) bloodDrops = bloodDrops.slice(-200);
});

// Auto-typing in command line
const typedText = document.getElementById('typedText');
const cursor = document.getElementById('cursor');
const autoCommands = [
    "whoami",
    "cat /etc/soul",
    "ps aux | grep daemon",
    "netstat -an | grep 666",
    "tail -f /var/log/abyss",
    "echo $SOUL_COUNT",
    "find / -name \"*.sacrifice\"",
    "chmod 666 /dev/null",
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
            setTimeout(typeChar, 50 + Math.random() * 100);
        } else {
            setTimeout(() => {
                typedText.textContent = '';
                isTyping = false;
                typingIndex++;
            }, 2000);
        }
    }
    typeChar();
}

setInterval(typeCommand, 6000);

// Ritual Panel API Integration
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
        
        // Possess button briefly
        btn.classList.add('possessed');
        setTimeout(() => btn.classList.remove('possessed'), 1000);

        try {
            const response = await fetch(`/api/ritual/${rite}`);
            const data = await response.json();
            ritualOutput.textContent = `[${data.rite.toUpperCase()}] ${data.result}`;
            ritualOutput.style.color = rite === 'banish' ? '#ff6600' : rite === 'divine' ? '#ff2a2a' : '#ccff00';
        } catch (err) {
            ritualOutput.textContent = 'The void rejects your request.';
            ritualOutput.style.color = '#ff2a2a';
        }
    });
});

// Status polling
async function updateStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        statusBar.textContent = `SYSTEM: ${data.status.toUpperCase()} | SOULS: ${data.souls_collected} | DEPTH: ${data.abyss_depth.toUpperCase()}`;
    } catch (err) {
        statusBar.textContent = 'SYSTEM: UNREACHABLE';
    }
}
setInterval(updateStatus, 5000);
updateStatus();

// Audio - low frequency drone (generated via Web Audio API as fallback)
let audioContext = null;
let droneOscillator = null;

function initAudio() {
    if (audioContext) return;
    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Create low frequency drone
    droneOscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    droneOscillator.type = 'sawtooth';
    droneOscillator.frequency.value = 55; // A1 - low and unsettling
    
    gainNode.gain.value = 0.02; // Very quiet, subliminal
    
    droneOscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    droneOscillator.start();
    
    // Add second oscillator for beating effect
    const osc2 = audioContext.createOscillator();
    const gain2 = audioContext.createGain();
    osc2.type = 'sine';
    osc2.frequency.value = 58; // Slight detune for beating
    gain2.gain.value = 0.015;
    osc2.connect(gain2);
    gain2.connect(audioContext.destination);
    osc2.start();
    
    // Modulate frequency for unease
    setInterval(() => {
        droneOscillator.frequency.value = 55 + Math.random() * 2;
    }, 3000);
}

// Start audio on first interaction (browser policy)
document.addEventListener('click', initAudio, { once: true });
document.addEventListener('keydown', initAudio, { once: true });

// Random screen distortion
setInterval(() => {
    if (Math.random() < 0.05) {
        document.body.style.transform = `translate(${Math.random() * 2}px, ${Math.random() * 2}px)`;
        setTimeout(() => {
            document.body.style.transform = '';
        }, 100);
    }
}, 2000);

// Corruption text effect on title
const title = document.querySelector('.glitch-title');
const corruptionChars = '▓▒░█◘○◙•◦†‡§¶♠♣♥♦◊○◘◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ÇüéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜø£Ø×ƒáíóúñÑªº¿®¬½¼¡«»░▒▓│┤╡╢╖╕╣║╗╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤÷≈°∙·√ⁿ²■\u0000';

function corruptTitle() {
    const original = title.getAttribute('data-text');
    let corrupted = '';
    for (let i = 0; i < original.length; i++) {
        if (Math.random() < 0.1) {
            corrupted += corruptionChars[Math.floor(Math.random() * corruptionChars.length)];
        } else {
            corrupted += original[i];
        }
    }
    title.textContent = corrupted;
    setTimeout(() => {
        title.textContent = original;
    }, 200);
}

setInterval(corruptTitle, 3000);

// Tab visibility - detect when user leaves
let awayTime = 0;
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        awayTime = Date.now();
    } else {
        const gone = Date.now() - awayTime;
        if (gone > 10000) { // Gone more than 10 seconds
            addPossessionLog();
            const entry = possessionLog.lastChild;
            entry.textContent = `> You were gone for ${Math.floor(gone/1000)} seconds. I watched the page alone.`;
            triggerPossession();
        }
    }
});
