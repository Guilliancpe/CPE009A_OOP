<h1 align="center"><mark>Hi 👋, I'm Guillian Carlo V. Ignacio</mark></h1>
<h3 align="center">A CPE12S1 STUDENT</h3>

- Email: **qgcignacio@tip.edu.ph**
- 


<h3 align="left">Languages and Tools:</h3>
<p align="left">
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
</p>



```diff
- CRAMMER
- Procrastinator
```

<p align="center">
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWlvMm13dTYwdzc1OWIybGMzOG03eGpiZnhiOWM1czJvaHU3dHgwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ekGDkpNdG0LUOIN2We/giphy.gif" alt="python" width="400" height="400"/>
  </a>
</p>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Tic Tac Toe</title>
  <style>
    :root { --bg:#f8f5e7; --board:#fff; --line:#333; --x:#0f766e; --o:#b91c1c; --text:#1f2937; }
    body { margin:0; font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,'Helvetica Neue',Arial; background:var(--bg); color:var(--text); display:grid; place-items:center; min-height:100vh; }
    .wrap { width:min(420px, 92vw); }
    h1 { text-align:center; margin:18px 0; font-weight:700; }
    .status { text-align:center; margin:8px 0 16px; min-height:24px; }
    .board { display:grid; grid-template-columns:repeat(3,1fr); gap:8px; background:#0000; }
    button.cell { aspect-ratio:1/1; border:2px solid var(--line); background:var(--board); font-size:clamp(2.2rem, 8vw, 3.4rem); font-weight:800; cursor:pointer; border-radius:10px; transition:transform .08s ease; }
    button.cell:hover { transform:scale(1.03); }
    .x { color:var(--x); }
    .o { color:var(--o); }
    .controls { display:flex; gap:10px; justify-content:center; margin-top:14px; }
    .btn { padding:10px 14px; border-radius:10px; border:2px solid var(--line); background:#fff; cursor:pointer; font-weight:700; }
    .btn.secondary { background:#eee; }
    .footer { text-align:center; margin-top:14px; font-size:.9rem; opacity:.7; }
  </style>
</head>
<body>
  <div class="wrap">
    <h1>Tic Tac Toe</h1>
    <div id="status" class="status">Player X’s turn</div>
    <div id="board" class="board" aria-label="Tic tac toe board"></div>
    <div class="controls">
      <button id="reset" class="btn">Reset</button>
      <button id="ai" class="btn secondary">Play vs AI: Off</button>
    </div>
    <div class="footer">Made with GitHub Pages</div>
  </div>
  <script>
    const boardEl = document.getElementById('board');
    const statusEl = document.getElementById('status');
    const resetBtn = document.getElementById('reset');
    const aiBtn = document.getElementById('ai');

    let board = Array(9).fill(null);
    let xTurn = true;
    let gameOver = false;
    let vsAI = false;

    const lines = [
      [0,1,2],[3,4,5],[6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]
    ];

    function winner(b=board) {
      for (const [a,c,d] of lines) {
        if (b[a] && b[a] === b[c] && b[a] === b[d]) return b[a];
      }
      return b.every(v => v) ? 'draw' : null;
    }

    function render() {
      boardEl.innerHTML = '';
      board.forEach((val, i) => {
        const btn = document.createElement('button');
        btn.className = 'cell' + (val ? ' ' + val.toLowerCase() : '');
        btn.setAttribute('aria-label', `Cell ${i+1}`);
        btn.textContent = val || '';
        btn.disabled = !!val || gameOver;
        btn.onclick = () => move(i);
        boardEl.appendChild(btn);
      });
      const w = winner();
      if (w === 'draw') { statusEl.textContent = 'It’s a draw.'; gameOver = true; }
      else if (w) { statusEl.textContent = `Player ${w} wins!`; gameOver = true; }
      else { statusEl.textContent = `Player ${xTurn ? 'X' : 'O'}’s turn`; }
    }

    function move(i) {
      if (board[i] || gameOver) return;
      board[i] = xTurn ? 'X' : 'O';
      xTurn = !xTurn;
      render();
      if (vsAI && !gameOver && !xTurn) {
        setTimeout(aiMove, 220);
      }
    }

    function aiMove() {
      // Simple AI: win -> block -> center -> corner -> random
      const empty = board.map((v, i) => v ? null : i).filter(v => v !== null);

      function tryLine(player) {
        for (const [a,c,d] of lines) {
          const line = [a,c,d];
          const vals = line.map(i => board[i]);
          if (vals.filter(v => v === player).length === 2 && vals.includes(null)) {
            return line[vals.indexOf(null)];
          }
        }
        return null;
      }

      let i = tryLine('O') ?? tryLine('X');
      if (i === null && board[4] === null) i = 4;
      if (i === null) {
        const corners = [0,2,6,8].filter(k => board[k] === null);
        i = (corners[0] ?? empty[0]);
      }
      move(i);
    }

    resetBtn.onclick = () => { board = Array(9).fill(null); xTurn = true; gameOver = false; render(); };
    aiBtn.onclick = () => { vsAI = !vsAI; aiBtn.textContent = `Play vs AI: ${vsAI ? 'On' : 'Off'}`; if (vsAI && !gameOver && !xTurn) setTimeout(aiMove, 220); };
    render();
  </script>
</body>
</html>

<p align="center">
  <a href="https://yourname.github.io/tic-tac-toe" target="_blank">
    <img src="https://img.shields.io/badge/Play%20Tic%20Tac%20Toe-Click%20Here-2ea44f?style=for-the-badge" alt="Play Tic Tac Toe">
  </a>
</p>

<details>
  <summary>Preview</summary>

  <p align="center">
    <img src="https://raw.githubusercontent.com/yourname/tic-tac-toe/main/preview.png" alt="Tic Tac Toe Preview" width="420">
  </p>
</details>
