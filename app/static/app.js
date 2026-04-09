let notebookState = {
  notebookId: "python_basics_lab",
  title: "Notebook de práctica",
  description: "",
  cells: [],
};
let autoSaveTimer = null;
let activeClass = "00-diagnostico-inicial";
let quizState = {
  quiz: null,
  answers: {},
  submitted: false,
};

function showTab(name) {
  document.querySelectorAll(".tab").forEach((tab) => tab.classList.remove("active"));
  document.getElementById(`tab-${name}`).classList.add("active");
  document.querySelectorAll(".tab-btn").forEach((button) => button.classList.remove("tab-active"));
  const button = document.getElementById(`tabBtn-${name}`);
  if (button) {
    button.classList.add("tab-active");
  }
}

function escapeHtml(value) {
  if (typeof value !== "string") {
    return "";
  }
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function buildClassSection(title, body, { open = false } = {}) {
  if (!body) {
    return "";
  }

  return `
    <details class="class-section collapsible"${open ? " open" : ""}>
      <summary><strong>${escapeHtml(title)}</strong></summary>
      <div class="markdown-body">${body}</div>
    </details>
  `;
}

function buildAssetSection(assets) {
  const entries = Object.entries(assets || {}).filter(([, asset]) => asset?.url);
  if (!entries.length) {
    return "";
  }

  const labels = {
    pdf: "Abrir guia PDF",
    pptx: "Descargar presentacion PPTX",
  };

  const descriptions = {
    pdf: "Guia completa derivada del contenido real del modulo.",
    pptx: "Presentacion editable lista para exponer la clase.",
  };

  const items = entries
    .map(
      ([kind, asset]) => `
        <a class="asset-link-card" href="${escapeHtml(asset.url)}" target="_blank" rel="noopener">
          <span class="asset-link-kind">${escapeHtml(kind.toUpperCase())}</span>
          <strong>${escapeHtml(labels[kind] || asset.filename)}</strong>
          <span class="asset-link-description">${escapeHtml(descriptions[kind] || asset.path)}</span>
          <span class="asset-link-path">${escapeHtml(asset.path)}</span>
        </a>
      `
    )
    .join("");

  return `
    <section class="class-section class-assets-panel">
      <div class="class-assets-header">
        <div>
          <h3>Materiales derivados de esta clase</h3>
          <p class="muted">Estos archivos salen del contenido real del modulo y quedan listos para compartir o presentar.</p>
        </div>
      </div>
      <div class="class-assets-grid">${items}</div>
    </section>
  `;
}

function renderQuizSection() {
  const host = document.getElementById("quiz-host");
  if (!host || !quizState.quiz) {
    return;
  }

  const { quiz, answers, submitted } = quizState;
  const answeredCount = Object.keys(answers).length;
  const result = submitted ? scoreQuiz() : null;

  const summaryHtml = submitted
    ? buildQuizSummary(result)
    : `
        <div class="quiz-summary-box">
          <strong>Diagnóstico de entrada</strong>
          <p>${escapeHtml(quiz.description)}</p>
          <p>Respondidas: ${answeredCount}/${quiz.questions.length}</p>
        </div>
      `;

  const questionsHtml = quiz.questions
    .map((question, index) => buildQuizQuestion(question, index, answers[index], submitted))
    .join("");

  host.innerHTML = `
    <div class="class-section quiz-section">
      <div class="quiz-header">
        <div>
          <h3>${escapeHtml(quiz.title)}</h3>
          <p class="muted">Duración sugerida: ${escapeHtml(quiz.duration)}</p>
        </div>
        <div class="actions">
          <button onclick="submitQuiz()">Enviar respuestas</button>
          <button onclick="resetQuiz()" class="btn-secondary">Reiniciar quiz</button>
        </div>
      </div>
      ${summaryHtml}
      <div class="quiz-questions">${questionsHtml}</div>
    </div>
  `;
}

function buildQuizSummary(result) {
  const categoryRows = Object.entries(result.byCategory)
    .sort(([left], [right]) => left.localeCompare(right))
    .map(([category, data]) => {
      return `
        <tr>
          <td>${escapeHtml(category)}</td>
          <td>${data.correct}</td>
          <td>${data.total}</td>
        </tr>
      `;
    })
    .join("");

  return `
    <div class="quiz-summary-box quiz-summary-box-graded">
      <strong>Resultado final</strong>
      <p>${result.correct}/${result.total} respuestas correctas.</p>
      <table class="quiz-summary-table">
        <thead>
          <tr>
            <th>Categoría</th>
            <th>Correctas</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          ${categoryRows}
        </tbody>
      </table>
    </div>
  `;
}

function buildQuizQuestion(question, index, selectedIndex, submitted) {
  const optionsHtml = question.options
    .map((option, optionIndex) => {
      const isSelected = selectedIndex === optionIndex;
      const isCorrect = question.correctIndex === optionIndex;
      const buttonClasses = ["quiz-option"];

      if (isSelected) {
        buttonClasses.push("quiz-option-selected");
      }
      if (submitted && isCorrect) {
        buttonClasses.push("quiz-option-correct");
      }
      if (submitted && isSelected && !isCorrect) {
        buttonClasses.push("quiz-option-wrong");
      }

      return `
        <button
          type="button"
          class="${buttonClasses.join(" ")}"
          onclick="selectQuizOption(${index}, ${optionIndex})"
          ${submitted ? "disabled" : ""}
        >
          <span class="quiz-option-label">${String.fromCharCode(65 + optionIndex)}.</span>
          <span>${escapeHtml(option)}</span>
        </button>
      `;
    })
    .join("");

  const feedbackHtml = submitted
    ? buildQuizFeedback(question, selectedIndex)
    : '<p class="quiz-feedback muted">Selecciona una alternativa y envía el quiz para ver la corrección.</p>';

  return `
    <article class="quiz-question-card">
      <div class="quiz-question-header">
        <span class="quiz-question-number">Pregunta ${index + 1}</span>
        <span class="quiz-question-category">${escapeHtml(question.category)}</span>
      </div>
      <p class="quiz-question-text">${escapeHtml(question.prompt)}</p>
      <div class="quiz-options">${optionsHtml}</div>
      ${feedbackHtml}
    </article>
  `;
}

function buildQuizFeedback(question, selectedIndex) {
  if (selectedIndex === question.correctIndex) {
    return `
      <p class="quiz-feedback quiz-feedback-correct">
        Correcta. ${escapeHtml(question.explanation)}
      </p>
    `;
  }

  if (selectedIndex === undefined) {
    return `
      <p class="quiz-feedback quiz-feedback-missing">
        Sin responder. La correcta era: <strong>${escapeHtml(question.options[question.correctIndex])}</strong>.
        ${escapeHtml(question.explanation)}
      </p>
    `;
  }

  return `
    <p class="quiz-feedback quiz-feedback-wrong">
      Marcaste: <strong>${escapeHtml(question.options[selectedIndex])}</strong>. La correcta era:
      <strong>${escapeHtml(question.options[question.correctIndex])}</strong>. ${escapeHtml(question.explanation)}
    </p>
  `;
}

function scoreQuiz() {
  const byCategory = {};
  let correct = 0;

  quizState.quiz.questions.forEach((question, index) => {
    const selectedIndex = quizState.answers[index];
    const isCorrect = selectedIndex === question.correctIndex;
    if (isCorrect) {
      correct += 1;
    }

    if (!byCategory[question.category]) {
      byCategory[question.category] = { correct: 0, total: 0 };
    }
    byCategory[question.category].total += 1;
    if (isCorrect) {
      byCategory[question.category].correct += 1;
    }
  });

  return {
    correct,
    total: quizState.quiz.questions.length,
    byCategory,
  };
}

function selectQuizOption(questionIndex, optionIndex) {
  if (!quizState.quiz || quizState.submitted) {
    return;
  }
  quizState.answers[questionIndex] = optionIndex;
  renderQuizSection();
}

function submitQuiz() {
  if (!quizState.quiz) {
    return;
  }

  if (Object.keys(quizState.answers).length < quizState.quiz.questions.length) {
    showToast("Responde las 30 preguntas antes de enviar.");
    return;
  }

  quizState.submitted = true;
  renderQuizSection();
  showToast("Diagnóstico corregido. Revisa aciertos y errores por pregunta.");
}

function resetQuiz() {
  if (!quizState.quiz) {
    return;
  }
  quizState.answers = {};
  quizState.submitted = false;
  renderQuizSection();
}

async function loadClass(slug) {
  activeClass = slug;
  document.querySelectorAll(".class-list-btn").forEach((button) => button.classList.remove("active"));
  const activeButton = document.querySelector(`[data-slug="${slug}"]`);
  if (activeButton) {
    activeButton.classList.add("active");
  }

  const container = document.getElementById("class-content");
  container.innerHTML = '<div class="loading-spinner">Cargando clase...</div>';

  try {
    const response = await fetch(`/api/class/${slug}`);
    if (!response.ok) {
      container.innerHTML = '<p class="output-error">No fue posible cargar la clase.</p>';
      return;
    }

    const data = await response.json();
    quizState = {
      quiz: data.quiz,
      answers: {},
      submitted: false,
    };

    container.innerHTML = `
      <div class="class-section markdown-body">${data.html["README.md"] || ""}</div>
      ${buildAssetSection(data.assets)}
      ${buildClassSection("Base teórica", data.html["teoria.md"], { open: true })}
      ${buildClassSection("Slides y pauta", data.html["slides.md"], { open: true })}
      ${buildClassSection("Ejercicios", data.html["ejercicios.md"], { open: true })}
      ${buildClassSection("Homework", data.html["homework.md"])}
      ${data.quiz ? '<div id="quiz-host"></div>' : ""}
    `;

    if (data.quiz) {
      renderQuizSection();
    }
  } catch (error) {
    container.innerHTML = '<p class="output-error">No fue posible cargar la clase.</p>';
  }
}

function createCellElement(cell, index) {
  const wrapper = document.createElement("div");
  wrapper.className = "cell";
  wrapper.dataset.index = index;
  wrapper.innerHTML = `
    <div class="cell-header">
      <span class="cell-label">In [${index + 1}]</span>
      <div class="actions">
        <button class="btn-run" onclick="runCell(${index})" title="Ejecutar (Ctrl+Enter)">Ejecutar</button>
        <button onclick="moveCell(${index}, -1)" title="Subir celda">Subir</button>
        <button onclick="moveCell(${index}, 1)" title="Bajar celda">Bajar</button>
        <button class="btn-danger" onclick="removeCell(${index})" title="Eliminar celda">Eliminar</button>
      </div>
    </div>
    <div class="cell-body">
      <textarea data-index="${index}" spellcheck="false" rows="6">${escapeHtml(cell.code || "")}</textarea>
      <div id="cell-output-${index}" class="cell-output">${cell.lastOutput || '<span class="muted">Sin salida aún.</span>'}</div>
    </div>
  `;

  const textarea = wrapper.querySelector("textarea");
  textarea.addEventListener("keydown", (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
      event.preventDefault();
      runCell(index);
    }
  });
  textarea.addEventListener("input", scheduleAutoSave);
  return wrapper;
}

function renderCells() {
  const container = document.getElementById("cells");
  container.innerHTML = "";
  notebookState.cells.forEach((cell, index) => container.appendChild(createCellElement(cell, index)));
}

function syncCellsFromDom() {
  document.querySelectorAll("#cells textarea").forEach((textarea) => {
    const index = Number(textarea.dataset.index);
    if (notebookState.cells[index]) {
      notebookState.cells[index].code = textarea.value;
    }
  });
  notebookState.title = document.getElementById("notebook-title").value;
}

function addCell() {
  syncCellsFromDom();
  notebookState.cells.push({ code: "# Escribe tu código aquí\n", lastOutput: "" });
  renderCells();
}

function removeCell(index) {
  syncCellsFromDom();
  notebookState.cells.splice(index, 1);
  renderCells();
}

function moveCell(index, direction) {
  syncCellsFromDom();
  const target = index + direction;
  if (target < 0 || target >= notebookState.cells.length) {
    return;
  }

  [notebookState.cells[index], notebookState.cells[target]] = [
    notebookState.cells[target],
    notebookState.cells[index],
  ];
  renderCells();
}

function formatOutput(data) {
  let html = "";
  if (data.stdout) {
    html += `<div class="output-success"><pre>${escapeHtml(data.stdout)}</pre></div>`;
  }
  if (data.result) {
    html += `<div class="output-result"><span class="output-label">Out:</span> <code>${escapeHtml(data.result)}</code></div>`;
  }
  if (data.error) {
    html += `<div class="output-error"><pre>${escapeHtml(data.error)}</pre></div>`;
  }
  if (!data.stdout && !data.result && !data.error && !data.images?.length) {
    html += '<span class="muted">Celda ejecutada sin salida visible.</span>';
  }
  if (data.images) {
    data.images.forEach((image) => {
      html += `<img class="output-image" src="data:image/png;base64,${image}" alt="gráfico">`;
    });
  }
  return html;
}

async function runCell(index) {
  syncCellsFromDom();
  const cell = notebookState.cells[index];
  const output = document.getElementById(`cell-output-${index}`);
  const button = document.querySelector(`.cell[data-index="${index}"] .btn-run`);

  output.innerHTML = '<span class="loading-inline">Ejecutando...</span>';
  if (button) {
    button.disabled = true;
  }

  const response = await fetch("/api/execute", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ notebook_id: notebookState.notebookId, code: cell.code }),
  });
  const data = await response.json();
  const formatted = formatOutput(data);
  output.innerHTML = formatted;
  cell.lastOutput = formatted;

  if (button) {
    button.disabled = false;
  }
}

async function runAllCells() {
  syncCellsFromDom();
  const button = document.getElementById("btn-run-all");
  if (button) {
    button.disabled = true;
    button.textContent = "Ejecutando...";
  }

  for (let index = 0; index < notebookState.cells.length; index += 1) {
    // eslint-disable-next-line no-await-in-loop
    await runCell(index);
  }

  if (button) {
    button.disabled = false;
    button.textContent = "Ejecutar todo";
  }
}

async function loadNotebook(templateId) {
  const response = await fetch(`/api/notebook/${templateId}`);
  const data = await response.json();
  notebookState = {
    notebookId: templateId,
    title: data.title,
    description: data.description || "",
    cells: (data.cells || []).map((cell) => ({ ...cell, lastOutput: "" })),
  };
  document.getElementById("notebook-title").value = data.title;
  document.getElementById("notebook-description").textContent = data.description || "";
  renderCells();
  showTab("lab");
  showToast(`Notebook cargado: ${data.title}`);
}

async function saveNotebook() {
  syncCellsFromDom();
  const name = notebookState.title.toLowerCase().replace(/[^a-z0-9]+/gi, "_");
  const payload = {
    name,
    title: notebookState.title,
    description: notebookState.description,
    cells: notebookState.cells,
  };
  const response = await fetch("/api/notebook/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  showToast(`Notebook guardado: ${data.saved_to}`);
}

function scheduleAutoSave() {
  clearTimeout(autoSaveTimer);
  autoSaveTimer = setTimeout(() => {
    syncCellsFromDom();
    saveNotebook();
    showToast("Auto-guardado completado.", 1500);
  }, 30000);
}

async function resetRuntime() {
  const response = await fetch("/api/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ notebook_id: notebookState.notebookId }),
  });
  const data = await response.json();
  showToast(data.message);
}

async function runRunner() {
  const code = document.getElementById("runner-code").value;
  const output = document.getElementById("runner-output");
  const button = document.getElementById("btn-runner-run");

  output.innerHTML = '<span class="loading-inline">Ejecutando...</span>';
  if (button) {
    button.disabled = true;
  }

  const response = await fetch("/api/execute", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ notebook_id: "quick_runner", code }),
  });
  const data = await response.json();
  output.innerHTML = formatOutput(data);

  if (button) {
    button.disabled = false;
  }
}

async function resetRunner() {
  const response = await fetch("/api/reset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ notebook_id: "quick_runner" }),
  });
  const data = await response.json();
  document.getElementById("runner-output").innerHTML = `<span class="muted">${escapeHtml(data.message)}</span>`;
}

function showToast(message, duration = 3000) {
  let toast = document.getElementById("toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "toast";
    document.body.appendChild(toast);
  }

  toast.textContent = message;
  toast.classList.add("toast-visible");
  setTimeout(() => toast.classList.remove("toast-visible"), duration);
}

window.addEventListener("DOMContentLoaded", async () => {
  const runnerTextarea = document.getElementById("runner-code");
  if (runnerTextarea) {
    runnerTextarea.addEventListener("keydown", (event) => {
      if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
        event.preventDefault();
        runRunner();
      }
    });
  }

  await loadClass(activeClass);
  await loadNotebook("python_basics_lab");
  showTab("curriculum");
});
