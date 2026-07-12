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

// Reveal ritual panel after boot
setTimeout(() => {
    ritualPanel.classList.add('visible');
}, 4200);

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
  @@@@@@@`
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
}

setInterval(() => {
    if (Math.random() < 0.1) triggerPossession();
}, 10000);

// Easter Egg
const easterEgg = document.getElementById('easterEgg');
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

// Ritual Panel API Integration
const ritualBtns = document.querySelectorAll('.ritual-btn');
const ritualOutput = document.getElementById('ritualOutput');
const statusBar = document.getElementById('statusBar');

ritualBtns.forEach(btn => {
    btn.addEventListener('click', async () => {
        const rite = btn.dataset.rite;
        ritualOutput.textContent = 'Channeling...';
        btn.style.transform = 'scale(0.95)';
        setTimeout(() => btn.style.transform = '', 100);

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
