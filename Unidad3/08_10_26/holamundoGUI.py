from flask import Flask

app = Flask(__name__)


@app.route("/")
def pacman():
    return r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Pac-Man</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background:
        radial-gradient(circle at center, #111827, #020617 70%);
    color: white;
    font-family: Arial, sans-serif;

    min-height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    overflow: hidden;
}

.game-container {
    width: min(95vw, 650px);
}

/* =========================
   TITULO
========================= */

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;

    color: #facc15;

    text-shadow:
        0 0 10px #facc15,
        0 0 25px #facc15;

    margin-bottom: 12px;
}

.title span {
    color: #3b82f6;
}

/* =========================
   HUD
========================= */

.hud {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;

    gap: 8px;

    margin-bottom: 10px;
}

.stat {
    background: #111827;

    border: 1px solid #334155;

    border-radius: 10px;

    padding: 8px;

    text-align: center;
}

.stat small {
    display: block;

    color: #94a3b8;

    font-size: 10px;
}

.stat strong {
    color: #facc15;

    font-size: 18px;
}

/* =========================
   JUEGO
========================= */

#game {
    position: relative;

    width: 100%;

    aspect-ratio: 1 / 1;

    background: #000;

    border:
        3px solid #1d4ed8;

    border-radius: 15px;

    box-shadow:
        0 0 30px #1d4ed855;

    overflow: hidden;
}

canvas {
    width: 100%;
    height: 100%;

    display: block;
}

/* =========================
   MENU
========================= */

.screen {
    position: absolute;

    inset: 0;

    background:
        rgba(0,0,0,.88);

    display: flex;

    justify-content: center;
    align-items: center;

    z-index: 20;

    text-align: center;
}

.panel {
    padding: 30px;

    width: 85%;

    background:
        linear-gradient(
            145deg,
            #111827,
            #1e1b4b
        );

    border:
        1px solid #475569;

    border-radius: 20px;
}

.panel h1 {
    color: #facc15;

    font-size: 40px;

    margin-bottom: 10px;
}

.panel p {
    color: #cbd5e1;

    line-height: 1.6;

    margin-bottom: 20px;
}

.btn {
    width: 100%;

    padding: 15px;

    border: none;

    border-radius: 12px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );

    color: white;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;
}

.btn:hover {
    filter: brightness(1.2);
}

/* =========================
   CONTROLES
========================= */

.controls {
    margin-top: 12px;

    display: grid;

    grid-template-columns:
        1fr 1fr 1fr;

    gap: 8px;

    max-width: 280px;

    margin-left: auto;
    margin-right: auto;
}

.control {
    height: 50px;

    border:
        1px solid #334155;

    background: #111827;

    color: white;

    border-radius: 12px;

    font-size: 22px;

    cursor: pointer;
}

.control:hover {
    background: #1e293b;
}

.up {
    grid-column: 2;
}

.left {
    grid-column: 1;
    grid-row: 2;
}

.down {
    grid-column: 2;
    grid-row: 2;
}

.right {
    grid-column: 3;
    grid-row: 2;
}

/* =========================
   MOVIL
========================= */

@media(max-width: 500px) {

    .title {
        font-size: 30px;
    }

    .panel h1 {
        font-size: 30px;
    }

}

</style>
</head>


<body>


<div class="game-container">

    <div class="title">
        PAC<span>-</span>MAN
    </div>


    <div class="hud">

        <div class="stat">
            <small>PUNTOS</small>
            <strong id="score">0</strong>
        </div>

        <div class="stat">
            <small>RÉCORD</small>
            <strong id="best">0</strong>
        </div>

        <div class="stat">
            <small>VIDAS</small>
            <strong id="lives">3</strong>
        </div>

    </div>


    <div id="game">

        <canvas id="canvas"></canvas>


        <!-- MENU -->

        <div class="screen" id="menu">

            <div class="panel">

                <h1>🟡 PAC-MAN</h1>

                <p>
                    Come todos los puntos,
                    evita a los fantasmas
                    y consigue el récord.
                </p>

                <button
                    class="btn"
                    id="start">
                    🎮 JUGAR
                </button>

            </div>

        </div>


        <!-- GAME OVER -->

        <div
            class="screen"
            id="gameOver"
            style="display:none;">

            <div class="panel">

                <h1>GAME OVER</h1>

                <p id="result">
                    Fin de la partida.
                </p>

                <button
                    class="btn"
                    id="restart">
                    🔄 VOLVER A JUGAR
                </button>

            </div>

        </div>


        <!-- VICTORIA -->

        <div
            class="screen"
            id="win"
            style="display:none;">

            <div class="panel">

                <h1>🏆 ¡GANASTE!</h1>

                <p>
                    ¡Te comiste todos
                    los puntos del nivel!
                </p>

                <button
                    class="btn"
                    id="next">
                    🚀 SIGUIENTE NIVEL
                </button>

            </div>

        </div>

    </div>


    <!-- CONTROLES -->

    <div class="controls">

        <button
            class="control up"
            data-dir="up">
            ▲
        </button>

        <button
            class="control left"
            data-dir="left">
            ◀
        </button>

        <button
            class="control down"
            data-dir="down">
            ▼
        </button>

        <button
            class="control right"
            data-dir="right">
            ▶
        </button>

    </div>

</div>


<script>

/* ======================================
   CANVAS
====================================== */

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");


canvas.width = 600;
canvas.height = 600;


/* ======================================
   MAPA

   # = pared
   . = punto
   o = power pellet
   - = espacio
====================================== */

const originalMap = [

"###################",

"#........#........#",

"#.###.###.###.###.#",

"#o###.###.###.###o#",

"#.................#",

"#.###.#.#####.#.###",

"#.....#...#...#...#",

"#####.###-###.#####",

"-----.#-----#.-----",

"#####.#-----#.#####",

"#.................#",

"#.###.###.###.###.#",

"#o..#.....#.....#o#",

"###.#.###.#.###.#.#",

"#.....#...#...#....",

"#.###.#.#####.#.###",

"#........#........#",

"###################"

];


/* ======================================
   VARIABLES
====================================== */

let map;

let tile;

let player;

let ghosts = [];

let score = 0;

let lives = 3;

let best =
    Number(localStorage.getItem(
        "pacmanBest"
    )) || 0;

let playing = false;

let gameLoopId;

let direction = {
    x: 0,
    y: 0
};

let nextDirection = {
    x: 0,
    y: 0
};

let frightenedTime = 0;

let dotsLeft = 0;

let level = 1;


/* ======================================
   ELEMENTOS
====================================== */

const scoreText =
    document.getElementById("score");

const bestText =
    document.getElementById("best");

const livesText =
    document.getElementById("lives");

const menu =
    document.getElementById("menu");

const gameOver =
    document.getElementById("gameOver");

const win =
    document.getElementById("win");

const result =
    document.getElementById("result");


bestText.textContent = best;


/* ======================================
   MAPA
====================================== */

function createMap() {

    map =
        originalMap.map(
            row => row.split("")
        );

    dotsLeft = 0;

    for (
        let y = 0;
        y < map.length;
        y++
    ) {

        for (
            let x = 0;
            x < map[y].length;
            x++
        ) {

            if (
                map[y][x] === "." ||
                map[y][x] === "o"
            ) {

                dotsLeft++;

            }

        }

    }

}


/* ======================================
   POSICIONES
====================================== */

function createCharacters() {

    player = {

        x: 9,

        y: 16,

        startX: 9,

        startY: 16,

        radius: .38

    };


    ghosts = [

        {
            x: 9,
            y: 8,
            color: "#ef4444",
            dir: {x: 1, y: 0}
        },

        {
            x: 8,
            y: 8,
            color: "#ec4899",
            dir: {x: -1, y: 0}
        },

        {
            x: 10,
            y: 8,
            color: "#06b6d4",
            dir: {x: 1, y: 0}
        },

        {
            x: 9,
            y: 9,
            color: "#f97316",
            dir: {x: -1, y: 0}
        }

    ];

}


/* ======================================
   PARED
====================================== */

function isWall(x, y) {

    if (
        y < 0 ||
        y >= map.length ||
        x < 0 ||
        x >= map[0].length
    )
        return true;


    return map[y][x] === "#";

}


/* ======================================
   MOVER JUGADOR
====================================== */

function canMove(x, y, dir) {

    const nx =
        Math.round(x + dir.x);

    const ny =
        Math.round(y + dir.y);

    return !isWall(nx, ny);

}


function movePlayer() {

    if (!playing)
        return;


    /* intentar nueva dirección */

    if (
        canMove(
            player.x,
            player.y,
            nextDirection
        )
    ) {

        direction =
            {...nextDirection};

    }


    const speed =
        0.075 + level * 0.005;


    const nx =
        player.x +
        direction.x * speed;

    const ny =
        player.y +
        direction.y * speed;


    if (
        canMove(
            player.x,
            player.y,
            direction
        )
    ) {

        player.x = nx;
        player.y = ny;

    }


    /* teletransporte lateral */

    if (
        player.x < 0
    )
        player.x =
            map[0].length - 1;

    if (
        player.x >
        map[0].length - 1
    )
        player.x = 0;


    eatDot();

}


/* ======================================
   COMER PUNTOS
====================================== */

function eatDot() {

    const x =
        Math.round(player.x);

    const y =
        Math.round(player.y);


    if (
        map[y] &&
        (
            map[y][x] === "." ||
            map[y][x] === "o"
        )
    ) {

        const power =
            map[y][x] === "o";


        map[y][x] = "-";

        dotsLeft--;


        if (power) {

            score += 50;

            frightenedTime = 600;

        } else {

            score += 10;

        }


        updateHUD();


        if (
            dotsLeft <= 0
        ) {

            winLevel();

        }

    }

}


/* ======================================
   FANTASMAS
====================================== */

function moveGhosts() {

    ghosts.forEach(
        ghost => {

            const speed =
                0.035 +
                level * 0.003;


            /* si llegó al centro
               elegir dirección */

            const gx =
                Math.round(ghost.x);

            const gy =
                Math.round(ghost.y);


            if (
                Math.abs(
                    ghost.x - gx
                ) < .08 &&
                Math.abs(
                    ghost.y - gy
                ) < .08
            ) {

                const possible = [

                    {x: 1, y: 0},

                    {x: -1, y: 0},

                    {x: 0, y: 1},

                    {x: 0, y: -1}

                ].filter(
                    d =>
                        !isWall(
                            gx + d.x,
                            gy + d.y
                        )
                );


                /* evitar regresar
                   inmediatamente */

                const filtered =
                    possible.filter(
                        d =>
                            !(
                                d.x ===
                                -ghost.dir.x &&
                                d.y ===
                                -ghost.dir.y
                            )
                    );


                const choices =
                    filtered.length
                    ? filtered
                    : possible;


                let chosen;


                /* perseguir a Pac-Man
                   de vez en cuando */

                if (
                    Math.random() < .55
                ) {

                    chosen =
                        choices.reduce(
                            (
                                bestChoice,
                                choice
                            ) => {

                                const a =
                                    Math.abs(
                                        gx +
                                        choice.x -
                                        player.x
                                    ) +
                                    Math.abs(
                                        gy +
                                        choice.y -
                                        player.y
                                    );

                                const b =
                                    Math.abs(
                                        gx +
                                        bestChoice.x -
                                        player.x
                                    ) +
                                    Math.abs(
                                        gy +
                                        bestChoice.y -
                                        player.y
                                    );

                                return a < b
                                    ? choice
                                    : bestChoice;

                            },
                            choices[0]
                        );

                } else {

                    chosen =
                        choices[
                            Math.floor(
                                Math.random() *
                                choices.length
                            )
                        ];

                }


                ghost.dir =
                    chosen;

            }


            ghost.x +=
                ghost.dir.x *
                speed;

            ghost.y +=
                ghost.dir.y *
                speed;


            if (
                ghost.x < 0
            )
                ghost.x =
                    map[0].length - 1;

            if (
                ghost.x >
                map[0].length - 1
            )
                ghost.x = 0;


            checkGhostCollision(
                ghost
            );

        }
    );


    if (
        frightenedTime > 0
    )
        frightenedTime--;

}


/* ======================================
   COLISIÓN FANTASMA
====================================== */

function checkGhostCollision(
    ghost
) {

    const distance =
        Math.hypot(
            player.x - ghost.x,
            player.y - ghost.y
        );


    if (
        distance < .65
    ) {

        if (
            frightenedTime > 0
        ) {

            score += 200;

            ghost.x = 9;
            ghost.y = 8;

            updateHUD();

        } else {

            loseLife();

        }

    }

}


/* ======================================
   PERDER VIDA
====================================== */

function loseLife() {

    lives--;

    updateHUD();


    if (
        lives <= 0
    ) {

        endGame();

        return;

    }


    player.x =
        player.startX;

    player.y =
        player.startY;


    direction =
        {x: 0, y: 0};

    nextDirection =
        {x: 0, y: 0};


    ghosts.forEach(
        (ghost, index) => {

            ghost.x =
                index === 0
                ? 9
                : 8 + index;

            ghost.y = 8;

        }
    );

}


/* ======================================
   DIBUJAR
====================================== */

function draw() {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    tile =
        canvas.width /
        map[0].length;


    /* fondo */

    ctx.fillStyle =
        "#000";

    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    /* mapa */

    for (
        let y = 0;
        y < map.length;
        y++
    ) {

        for (
            let x = 0;
            x < map[y].length;
            x++
        ) {

            const cell =
                map[y][x];


            /* paredes */

            if (
                cell === "#"
            ) {

                ctx.fillStyle =
                    "#172554";

                ctx.fillRect(
                    x * tile,
                    y * tile,
                    tile,
                    tile
                );


                ctx.strokeStyle =
                    "#2563eb";

                ctx.lineWidth = 2;

                ctx.strokeRect(
                    x * tile + 2,
                    y * tile + 2,
                    tile - 4,
                    tile - 4
                );

            }


            /* puntos */

            if (
                cell === "."
            ) {

                ctx.fillStyle =
                    "#fef3c7";

                ctx.beginPath();

                ctx.arc(
                    x * tile +
                    tile / 2,

                    y * tile +
                    tile / 2,

                    3,

                    0,
                    Math.PI * 2
                );

                ctx.fill();

            }


            /* power */

            if (
                cell === "o"
            ) {

                ctx.fillStyle =
                    "#fff";

                ctx.beginPath();

                ctx.arc(
                    x * tile +
                    tile / 2,

                    y * tile +
                    tile / 2,

                    8,

                    0,
                    Math.PI * 2
                );

                ctx.fill();

            }

        }

    }


    drawPlayer();


    ghosts.forEach(
        drawGhost
    );

}


/* ======================================
   PACMAN
====================================== */

function drawPlayer() {

    const px =
        player.x * tile +
        tile / 2;

    const py =
        player.y * tile +
        tile / 2;


    let angle = 0;


    if (
        direction.x === 1
    )
        angle = 0;

    if (
        direction.x === -1
    )
        angle = Math.PI;

    if (
        direction.y === 1
    )
        angle = Math.PI / 2;

    if (
        direction.y === -1
    )
        angle = -Math.PI / 2;


    const mouth =
        .18 +
        Math.abs(
            Math.sin(
                Date.now() / 100
            )
        ) * .22;


    ctx.save();

    ctx.translate(
        px,
        py
    );

    ctx.rotate(angle);


    ctx.fillStyle =
        "#facc15";


    ctx.beginPath();

    ctx.moveTo(
        0,
        0
    );


    ctx.arc(
        0,
        0,

        tile * .39,

        mouth,

        Math.PI * 2 -
        mouth
    );


    ctx.closePath();

    ctx.fill();

    ctx.restore();

}


/* ======================================
   FANTASMA
====================================== */

function drawGhost(
    ghost
) {

    const x =
        ghost.x * tile +
        tile / 2;

    const y =
        ghost.y * tile +
        tile / 2;


    const r =
        tile * .36;


    let color =
        ghost.color;


    if (
        frightenedTime > 0
    ) {

        color =
            frightenedTime < 120 &&
            Math.floor(
                frightenedTime / 10
            ) % 2 === 0
            ? "#fff"
            : "#2563eb";

    }


    ctx.fillStyle =
        color;


    ctx.beginPath();

    ctx.arc(
        x,
        y - r * .1,
        r,
        Math.PI,
        0
    );


    ctx.lineTo(
        x + r,
        y + r
    );


    ctx.lineTo(
        x + r * .5,
        y + r * .65
    );


    ctx.lineTo(
        x,
        y + r
    );


    ctx.lineTo(
        x - r * .5,
        y + r * .65
    );


    ctx.lineTo(
        x - r,
        y + r
    );


    ctx.closePath();

    ctx.fill();


    /* ojos */

    ctx.fillStyle =
        "white";


    ctx.beginPath();

    ctx.arc(
        x - r * .38,
        y - r * .12,
        r * .25,
        0,
        Math.PI * 2
    );

    ctx.arc(
        x + r * .38,
        y - r * .12,
        r * .25,
        0,
        Math.PI * 2
    );

    ctx.fill();


    ctx.fillStyle =
        "#111827";


    ctx.beginPath();

    ctx.arc(
        x - r * .38,
        y - r * .12,
        r * .11,
        0,
        Math.PI * 2
    );

    ctx.arc(
        x + r * .38,
        y - r * .12,
        r * .11,
        0,
        Math.PI * 2
    );

    ctx.fill();

}


/* ======================================
   HUD
====================================== */

function updateHUD() {

    scoreText.textContent =
        Math.floor(score);

    bestText.textContent =
        best;

    livesText.textContent =
        lives;

}


/* ======================================
   INICIAR
====================================== */

function startGame() {

    createMap();

    createCharacters();


    score = 0;

    lives = 3;

    level = 1;

    direction =
        {x: 0, y: 0};

    nextDirection =
        {x: 0, y: 0};

    frightenedTime = 0;


    playing = true;


    menu.style.display =
        "none";

    gameOver.style.display =
        "none";

    win.style.display =
        "none";


    updateHUD();


    gameLoop();

}


/* ======================================
   GAME LOOP
====================================== */

function gameLoop() {

    if (!playing)
        return;


    movePlayer();

    moveGhosts();

    draw();


    gameLoopId =
        requestAnimationFrame(
            gameLoop
        );

}


/* ======================================
   GAME OVER
====================================== */

function endGame() {

    playing = false;


    cancelAnimationFrame(
        gameLoopId
    );


    if (
        Math.floor(score) >
        best
    ) {

        best =
            Math.floor(score);

        localStorage.setItem(
            "pacmanBest",
            best
        );

    }


    result.innerHTML = `
        Puntuación:
        <strong>${Math.floor(score)}</strong>
        <br><br>
        ${
            Math.floor(score) >= best
            ? "🔥 ¡NUEVO RÉCORD!"
            : "😎 ¡Buen intento!"
        }
    `;


    bestText.textContent =
        best;


    gameOver.style.display =
        "flex";

}


/* ======================================
   GANAR NIVEL
====================================== */

function winLevel() {

    playing = false;


    cancelAnimationFrame(
        gameLoopId
    );


    win.style.display =
        "flex";

}


/* ======================================
   SIGUIENTE NIVEL
====================================== */

function nextLevel() {

    level++;

    win.style.display =
        "none";


    createMap();

    createCharacters();


    player.x =
        player.startX;

    player.y =
        player.startY;


    direction =
        {x: 0, y: 0};

    nextDirection =
        {x: 0, y: 0};


    playing = true;


    gameLoop();

}


/* ======================================
   TECLADO
====================================== */

document.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "ArrowUp" ||
            event.key.toLowerCase() === "w"
        ) {

            nextDirection =
                {x: 0, y: -1};

        }


        if (
            event.key === "ArrowDown" ||
            event.key.toLowerCase() === "s"
        ) {

            nextDirection =
                {x: 0, y: 1};

        }


        if (
            event.key === "ArrowLeft" ||
            event.key.toLowerCase() === "a"
        ) {

            nextDirection =
                {x: -1, y: 0};

        }


        if (
            event.key === "ArrowRight" ||
            event.key.toLowerCase() === "d"
        ) {

            nextDirection =
                {x: 1, y: 0};

        }

    }
);


/* ======================================
   BOTONES
====================================== */

document.getElementById(
    "start"
).addEventListener(
    "click",
    startGame
);


document.getElementById(
    "restart"
).addEventListener(
    "click",
    startGame
);


document.getElementById(
    "next"
).addEventListener(
    "click",
    nextLevel
);


document.querySelectorAll(
    ".control"
).forEach(
    button => {

        button.addEventListener(
            "click",
            () => {

                const dir =
                    button.dataset.dir;


                if (
                    dir === "up"
                )
                    nextDirection =
                        {x: 0, y: -1};

                if (
                    dir === "down"
                )
                    nextDirection =
                        {x: 0, y: 1};

                if (
                    dir === "left"
                )
                    nextDirection =
                        {x: -1, y: 0};

                if (
                    dir === "right"
                )
                    nextDirection =
                        {x: 1, y: 0};

            }
        );

    }
);


/* ======================================
   DIBUJO INICIAL
====================================== */

createMap();

createCharacters();

draw();

updateHUD();

</script>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)