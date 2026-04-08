let notebookState = { notebookId: 'python_basics_lab', title: 'Notebook de práctica', description: '', cells: [] };

function showTab(name) {
  document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
  document.getElementById(`tab-${name}`).classList.add('active');
}

async function loadClass(slug) {
  const res = await fetch(`/api/class/${slug}`);
  const data = await res.json();
  const container = document.getElementById('class-content');
  container.innerHTML = `
    <div class="markdown-body">${data.html['README.md']}</div>
    <hr>
    <h3>Slides / pauta</h3>
    <div class="markdown-body">${data.html['slides.md']}</div>
    <h3>Ejercicios</h3>
    <div class="markdown-body">${data.html['ejercicios.md']}</div>
    <h3>Tarea</h3>
    <div class="markdown-body">${data.html['homework.md']}</div>`;
}

function createCellElement(cell, index) {
  const wrapper = document.createElement('div');
  wrapper.className = 'cell';
  wrapper.innerHTML = `
    <div class="cell-header">
      <strong>Celda ${index + 1}</strong>
      <div class="actions">
        <button onclick="runCell(${index})">Ejecutar</button>
        <button onclick="removeCell(${index})">Eliminar</button>
      </div>
    </div>
    <div class="cell-body">
      <textarea data-index="${index}">${cell.code || ''}</textarea>
      <div id="cell-output-${index}" class="cell-output">Salida pendiente.</div>
    </div>`;
  return wrapper;
}

function renderCells() {
  const container = document.getElementById('cells');
  container.innerHTML = '';
  notebookState.cells.forEach((cell, index) => container.appendChild(createCellElement(cell, index)));
}

function syncCellsFromDom() {
  document.querySelectorAll('#cells textarea').forEach((textarea) => {
    const index = Number(textarea.dataset.index);
    notebookState.cells[index].code = textarea.value;
  });
  notebookState.title = document.getElementById('notebook-title').value;
}

function addCell() {
  syncCellsFromDom();
  notebookState.cells.push({ code: '# Escribe tu código aquí\nprint("Nueva celda")' });
  renderCells();
}

function removeCell(index) {
  syncCellsFromDom();
  notebookState.cells.splice(index, 1);
  renderCells();
}

function formatOutput(data) {
  let html = '';
  if (data.stdout) html += `<div class="output-success">${escapeHtml(data.stdout)}</div>`;
  if (data.result) html += `<div><strong>Resultado:</strong> ${escapeHtml(data.result)}</div>`;
  if (data.error) html += `<div class="output-error">${escapeHtml(data.error)}</div>`;
  if (!data.stdout && !data.result && !data.error) html += '<div>Celda ejecutada sin salida visible.</div>';
  if (data.images) {
    data.images.forEach(img => { html += `<img class="output-image" src="data:image/png;base64,${img}" alt="gráfico">`; });
  }
  return html;
}

async function runCell(index) {
  syncCellsFromDom();
  const cell = notebookState.cells[index];
  const res = await fetch('/api/execute', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: notebookState.notebookId, code: cell.code }) });
  const data = await res.json();
  document.getElementById(`cell-output-${index}`).innerHTML = formatOutput(data);
}

async function runAllCells() {
  syncCellsFromDom();
  for (let i = 0; i < notebookState.cells.length; i += 1) { await runCell(i); }
}

async function loadNotebook(templateId) {
  const res = await fetch(`/api/notebook/${templateId}`);
  const data = await res.json();
  notebookState = { notebookId: templateId, title: data.title, description: data.description || '', cells: data.cells || [] };
  document.getElementById('notebook-title').value = data.title;
  document.getElementById('notebook-description').textContent = data.description || '';
  renderCells();
  showTab('lab');
}

async function saveNotebook() {
  syncCellsFromDom();
  const name = notebookState.title.toLowerCase().replace(/[^a-z0-9]+/gi, '_');
  const payload = { name, title: notebookState.title, description: notebookState.description, cells: notebookState.cells };
  const res = await fetch('/api/notebook/save', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
  const data = await res.json();
  alert(`Notebook guardado en ${data.saved_to}`);
}

async function resetRuntime() {
  const res = await fetch('/api/reset', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: notebookState.notebookId }) });
  const data = await res.json();
  alert(data.message);
}

async function runRunner() {
  const code = document.getElementById('runner-code').value;
  const res = await fetch('/api/execute', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: 'quick_runner', code }) });
  const data = await res.json();
  document.getElementById('runner-output').innerHTML = formatOutput(data);
}

async function resetRunner() {
  const res = await fetch('/api/reset', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ notebook_id: 'quick_runner' }) });
  const data = await res.json();
  document.getElementById('runner-output').textContent = data.message;
}

function escapeHtml(value) {
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}

window.addEventListener('DOMContentLoaded', async () => {
  await loadClass('01-python-fundamentos');
  await loadNotebook('python_basics_lab');
});
