let notebookState = { notebookId: 'python_basics_lab', title: 'Notebook de práctica', description: '', cells: [] };
let autoSaveTimer = null;
let activeClass = '01-python-fundamentos';

// ── Tab navigation ─────────────────────────────────────────────────────────

function showTab(name) {
  document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
  document.getElementById(`tab-${name}`).classList.add('active');
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('tab-active'));
  const btn = document.getElementById(`tabBtn-${name}`);
  if (btn) btn.classList.add('tab-active');
}

// ── Clase viewer ───────────────────────────────────────────────────────────

async function loadClass(slug) {
  activeClass = slug;
  document.querySelectorAll('.class-list-btn').forEach(b => b.classList.remove('active'));
  const btn = document.querySelector(`[data-slug="${slug}"]`);
  if (btn) btn.classList.add('active');

  const container = document.getElementById('class-content');
  container.innerHTML = '<div class="loading-spinner">Cargando clase…</div>';

  const res = await fetch(`/api/class/${slug}`);
  if (!res.ok) { container.innerHTML = '<p class="output-error">Error cargando la clase.</p>'; return; }
  const data = await res.json();

  container.innerHTML = `
    <div class="class-section markdown-body">${data.html['README.md']}</div>
    <details class="class-section collapsible" open>
      <summary><strong>Slides / Pauta de la clase</strong></summary>
      <div class="markdown-body">${data.html['slides.md'] || '<em>Sin slides.</em>'}</div>
    </details>
    <details class="class-section collapsible" open>
      <summary><strong>Ejercicios</strong></summary>
      <div class="markdown-body">${data.html['ejercicios.md'] || '<em>Sin ejercicios.</em>'}</div>
    </details>
    <details class="class-section collapsible">
      <summary><strong>Tarea / Homework</strong></summary>
      <div class="markdown-body">${data.html['homework.md'] || '<em>Sin tarea.</em>'}</div>
    </details>`;
}

// ── Notebook / Lab ─────────────────────────────────────────────────────────

function createCellElement(cell, index) {
  const wrapper = document.createElement('div');
  wrapper.className = 'cell';
  wrapper.dataset.index = index;
  wrapper.innerHTML = `
    <div class="cell-header">
      <span class="cell-label">In [${index + 1}]</span>
      <div class="actions">
        <button class="btn-run" onclick="runCell(${index})" title="Ejecutar (Ctrl+Enter)">▶ Ejecutar</button>
        <button onclick="moveCell(${index}, -1)" title="Subir celda">↑</button>
        <button onclick="moveCell(${index}, 1)" title="Bajar celda">↓</button>
        <button class="btn-danger" onclick="removeCell(${index})" title="Eliminar celda">✕</button>
      </div>
    </div>
    <div class="cell-body">
      <textarea data-index="${index}" spellcheck="false" rows="6">${escapeHtml(cell.code || '')}</textarea>
      <div id="cell-output-${index}" class="cell-output">${cell.lastOutput || '<span class="muted">Sin salida aún.</span>'}</div>
    </div>`;

  // Ctrl+Enter ejecuta la celda
  const ta = wrapper.querySelector('textarea');
  ta.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      runCell(index);
    }
  });
  ta.addEventListener('input', scheduleAutoSave);
  return wrapper;
}

function renderCells() {
  const container = document.getElementById('cells');
  container.innerHTML = '';
  notebookState.cells.forEach((cell, index) => container.appendChild(createCellElement(cell, index)));
}

function syncCellsFromDom() {
  document.querySelectorAll('#cells textarea').forEach(textarea => {
    const index = Number(textarea.dataset.index);
    if (notebookState.cells[index]) notebookState.cells[index].code = textarea.value;
  });
  notebookState.title = document.getElementById('notebook-title').value;
}

function addCell() {
  syncCellsFromDom();
  notebookState.cells.push({ code: '# Escribe tu código aquí\n', lastOutput: '' });
  renderCells();
  // Hacer scroll a la última celda
  const cells = document.querySelectorAll('.cell');
  if (cells.length) cells[cells.length - 1].scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function removeCell(index) {
  syncCellsFromDom();
  notebookState.cells.splice(index, 1);
  renderCells();
}

function moveCell(index, direction) {
  syncCellsFromDom();
  const target = index + direction;
  if (target < 0 || target >= notebookState.cells.length) return;
  [notebookState.cells[index], notebookState.cells[target]] = [notebookState.cells[target], notebookState.cells[index]];
  renderCells();
}

function formatOutput(data) {
  let html = '';
  if (data.stdout) html += `<div class="output-success"><pre>${escapeHtml(data.stdout)}</pre></div>`;
  if (data.result) html += `<div class="output-result"><span class="output-label">Out:</span> <code>${escapeHtml(data.result)}</code></div>`;
  if (data.error) html += `<div class="output-error"><pre>${escapeHtml(data.error)}</pre></div>`;
  if (!data.stdout && !data.result && !data.error && !data.images?.length) {
    html += '<span class="muted">Celda ejecutada sin salida visible.</span>';
  }
  if (data.images) {
    data.images.forEach(img => { html += `<img class="output-image" src="data:image/png;base64,${img}" alt="gráfico">`; });
  }
  return html;
}

async function runCell(index) {
  syncCellsFromDom();
  const cell = notebookState.cells[index];
  const outputEl = document.getElementById(`cell-output-${index}`);
  const btn = document.querySelector(`.cell[data-index="${index}"] .btn-run`);

  outputEl.innerHTML = '<span class="loading-inline">⏳ Ejecutando…</span>';
  if (btn) { btn.disabled = true; btn.textContent = '⏳'; }

  const res = await fetch('/api/execute', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ notebook_id: notebookState.notebookId, code: cell.code })
  });
  const data = await res.json();
  const formatted = formatOutput(data);
  outputEl.innerHTML = formatted;
  cell.lastOutput = formatted;

  if (btn) { btn.disabled = false; btn.textContent = '▶ Ejecutar'; }
}

async function runAllCells() {
  syncCellsFromDom();
  const btn = document.getElementById('btn-run-all');
  if (btn) { btn.disabled = true; btn.textContent = '⏳ Ejecutando todo…'; }
  for (let i = 0; i < notebookState.cells.length; i++) { await runCell(i); }
  if (btn) { btn.disabled = false; btn.textContent = '▶ Ejecutar todo'; }
}

async function loadNotebook(templateId) {
  const res = await fetch(`/api/notebook/${templateId}`);
  const data = await res.json();
  notebookState = { notebookId: templateId, title: data.title, description: data.description || '', cells: (data.cells || []).map(c => ({ ...c, lastOutput: '' })) };
  document.getElementById('notebook-title').value = data.title;
  document.getElementById('notebook-description').textContent = data.description || '';
  renderCells();
  showTab('lab');
  showToast(`Notebook "${data.title}" cargado`);
}

async function saveNotebook() {
  syncCellsFromDom();
  const name = notebookState.title.toLowerCase().replace(/[^a-z0-9]+/gi, '_');
  const payload = { name, title: notebookState.title, description: notebookState.description, cells: notebookState.cells };
  const res = await fetch('/api/notebook/save', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  const data = await res.json();
  showToast(`Notebook guardado: ${data.saved_to}`);
}

function scheduleAutoSave() {
  clearTimeout(autoSaveTimer);
  autoSaveTimer = setTimeout(() => {
    syncCellsFromDom();
    showToast('Auto-guardado…', 1500);
    saveNotebook();
  }, 30000); // 30 segundos de inactividad
}

async function resetRuntime() {
  const res = await fetch('/api/reset', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: notebookState.notebookId }) });
  const data = await res.json();
  showToast(data.message);
}

// ── Runner rápido ──────────────────────────────────────────────────────────

async function runRunner() {
  const code = document.getElementById('runner-code').value;
  const outputEl = document.getElementById('runner-output');
  const btn = document.getElementById('btn-runner-run');
  outputEl.innerHTML = '<span class="loading-inline">⏳ Ejecutando…</span>';
  if (btn) { btn.disabled = true; btn.textContent = '⏳'; }

  const res = await fetch('/api/execute', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ notebook_id: 'quick_runner', code })
  });
  const data = await res.json();
  outputEl.innerHTML = formatOutput(data);
  if (btn) { btn.disabled = false; btn.textContent = '▶ Ejecutar'; }
}

async function resetRunner() {
  const res = await fetch('/api/reset', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: 'quick_runner' }) });
  const data = await res.json();
  document.getElementById('runner-output').innerHTML = `<span class="muted">${data.message}</span>`;
}

// Runner también responde a Ctrl+Enter
document.addEventListener('DOMContentLoaded', () => {
  const runnerTextarea = document.getElementById('runner-code');
  if (runnerTextarea) {
    runnerTextarea.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); runRunner(); }
    });
  }
});

// ── Toast notifications ────────────────────────────────────────────────────

function showToast(message, duration = 3000) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add('toast-visible');
  setTimeout(() => toast.classList.remove('toast-visible'), duration);
}

// ── Utilities ──────────────────────────────────────────────────────────────

function escapeHtml(value) {
  if (typeof value !== 'string') return '';
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}

// ── Init ───────────────────────────────────────────────────────────────────

window.addEventListener('DOMContentLoaded', async () => {
  await loadClass('01-python-fundamentos');
  await loadNotebook('python_basics_lab');
  showTab('curriculum');
});
