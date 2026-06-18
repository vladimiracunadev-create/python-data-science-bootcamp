/* ============================================================
   Python Data Science Program — Lab UI client
   Vanilla JS. No modules, no CDNs (CSP-friendly).
   ============================================================ */

(function () {
  "use strict";

  // ── Global state ───────────────────────────────────────────
  const LS_KEYS = {
    expanded: "pdsp_lab.expandedParts",
    theme: "pdsp_lab.theme",
    rightCollapsed: "pdsp_lab.rightCollapsed",
    lastClass: "pdsp_lab.lastClass",
  };

  window._lab = {
    kernelId: null,
    kernelStatus: "stopped", // stopped | starting | idle | busy | dead
    currentClass: null,
    curriculum: [],
    flatClasses: [],
    expandedParts: loadJSON(LS_KEYS.expanded, {}),
    theme: localStorage.getItem(LS_KEYS.theme) || "dark",
    rightCollapsed: localStorage.getItem(LS_KEYS.rightCollapsed) === "1",
    execCount: 0,
    cells: [], // {id, type, source, el, editorEl, outputsEl, executionCount}
  };

  // ── Utils ──────────────────────────────────────────────────
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.from((ctx || document).querySelectorAll(sel)); }
  function el(tag, attrs, children) {
    const e = document.createElement(tag);
    if (attrs) {
      for (const k in attrs) {
        if (k === "class") e.className = attrs[k];
        else if (k === "text") e.textContent = attrs[k];
        else if (k === "html") e.innerHTML = attrs[k];
        else if (k.startsWith("on") && typeof attrs[k] === "function") {
          e.addEventListener(k.slice(2).toLowerCase(), attrs[k]);
        } else if (attrs[k] != null) {
          e.setAttribute(k, attrs[k]);
        }
      }
    }
    if (children) {
      (Array.isArray(children) ? children : [children]).forEach(c => {
        if (c == null) return;
        e.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
      });
    }
    return e;
  }
  function loadJSON(key, fallback) {
    try { return JSON.parse(localStorage.getItem(key)) || fallback; }
    catch { return fallback; }
  }
  function saveJSON(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch {}
  }
  function stripAnsi(s) { return String(s || "").replace(/\x1b\[[\d;]*m/g, ""); }

  async function api(path, opts) {
    opts = opts || {};
    opts.headers = Object.assign({ "Content-Type": "application/json" }, opts.headers || {});
    if (opts.body && typeof opts.body !== "string") opts.body = JSON.stringify(opts.body);
    const res = await fetch(path, opts);
    if (res.status === 204) return null;
    if (!res.ok) {
      let detail = "";
      try { detail = (await res.json()).error || ""; } catch {}
      throw new Error("HTTP " + res.status + (detail ? " · " + detail : ""));
    }
    return res.json();
  }

  // ── Toast ──────────────────────────────────────────────────
  function toast(msg, kind) {
    const container = $("#toast-container");
    const t = el("div", { class: "toast toast-" + (kind || "info") }, msg);
    container.appendChild(t);
    requestAnimationFrame(() => t.classList.add("visible"));
    setTimeout(() => {
      t.classList.remove("visible");
      setTimeout(() => t.remove(), 250);
    }, 4000);
  }

  // ── Theme ──────────────────────────────────────────────────
  function applyTheme(theme) {
    document.body.setAttribute("data-theme", theme);
    $("#theme-select").value = theme;
    window._lab.theme = theme;
    localStorage.setItem(LS_KEYS.theme, theme);
  }

  // ── Kernel badge ───────────────────────────────────────────
  function setKernelStatus(status) {
    window._lab.kernelStatus = status;
    const badge = $("#kernel-badge");
    const text = $("#kernel-badge-text");
    badge.className = "kernel-badge kernel-" + status;
    const labels = {
      stopped: "kernel: detenido",
      starting: "kernel: iniciando…",
      idle: "kernel: listo",
      busy: "kernel: ejecutando…",
      dead: "kernel: caído",
    };
    text.textContent = labels[status] || status;
    $("#rp-kernel-status").textContent = status;
  }

  // ── Curriculum ─────────────────────────────────────────────
  async function loadCurriculum() {
    try {
      const data = await api("/api/curriculum");
      window._lab.curriculum = data;
      window._lab.flatClasses = [];
      data.forEach(part => {
        (part.classes || []).forEach(c => {
          window._lab.flatClasses.push(Object.assign({ part_slug: part.part_slug }, c));
        });
      });
      renderSidebar();
    } catch (e) {
      $("#curriculum-tree").innerHTML =
        '<div class="tree-loading" style="color:var(--danger)">Error: ' + e.message + "</div>";
      toast("No se pudo cargar el currículo", "error");
    }
  }

  function renderSidebar(filter) {
    const tree = $("#curriculum-tree");
    tree.innerHTML = "";
    const q = (filter || "").toLowerCase().trim();

    window._lab.curriculum.forEach(part => {
      const classes = (part.classes || []).filter(c => {
        if (!q) return true;
        return (c.title || "").toLowerCase().includes(q) ||
               (c.slug || "").toLowerCase().includes(q);
      });
      if (q && classes.length === 0) return;

      const isExpanded = q ? true : !!window._lab.expandedParts[part.part_slug];
      const partEl = el("div", { class: "tree-part" + (isExpanded ? " expanded" : "") });

      const header = el("button", { class: "tree-part-header", type: "button" }, [
        el("span", { class: "tree-caret", text: "▶" }),
        el("span", { class: "tree-part-num", text: "P" + (part.part_number || "?") }),
        el("span", { class: "tree-part-title", text: part.part_title || part.part_slug }),
      ]);
      header.addEventListener("click", () => {
        const willExpand = !partEl.classList.contains("expanded");
        partEl.classList.toggle("expanded", willExpand);
        window._lab.expandedParts[part.part_slug] = willExpand;
        saveJSON(LS_KEYS.expanded, window._lab.expandedParts);
      });
      partEl.appendChild(header);

      const list = el("div", { class: "tree-classes" });
      classes.forEach(c => {
        const slug = c.slug;
        const btn = el("button", {
          class: "tree-class-btn" + (window._lab.currentClass === slug ? " active" : ""),
          type: "button",
          "data-slug": slug,
        }, [
          el("span", { class: "tree-class-num", text: String(c.number || "").padStart(3, "0") }),
          el("span", { class: "tree-class-title", text: c.title || slug }),
        ]);
        btn.addEventListener("click", () => loadClass(slug));
        list.appendChild(btn);
      });
      partEl.appendChild(list);
      tree.appendChild(partEl);
    });
  }

  function highlightActiveClass() {
    $$(".tree-class-btn").forEach(b => {
      b.classList.toggle("active", b.dataset.slug === window._lab.currentClass);
    });
  }

  // ── Load class / notebook ──────────────────────────────────
  async function loadClass(slug) {
    if (!slug) return;
    window._lab.currentClass = slug;
    saveJSON(LS_KEYS.lastClass, slug);
    highlightActiveClass();

    $("#empty-state").classList.add("hidden");
    $("#notebook-view").classList.remove("hidden");
    $("#cells-container").innerHTML =
      '<div class="tree-loading">Cargando notebook…</div>';

    try {
      const nb = await api("/api/notebook/" + slug);
      renderNotebook(nb);
    } catch (e) {
      $("#cells-container").innerHTML =
        '<div class="tree-loading" style="color:var(--danger)">No se pudo cargar el notebook: ' +
        e.message + "</div>";
    }
  }

  function findFlatIndex(slug) {
    return window._lab.flatClasses.findIndex(c => c.slug === slug);
  }

  function renderNotebook(nb) {
    const slug = nb.slug || window._lab.currentClass;
    const flat = window._lab.flatClasses;
    const idx = findFlatIndex(slug);
    const meta = idx >= 0 ? flat[idx] : null;

    $("#notebook-class-number").textContent =
      meta ? "Clase " + String(meta.number).padStart(3, "0") : "Clase";
    $("#notebook-class-title").textContent = nb.title || (meta && meta.title) || slug;

    const prevBtn = $("#prev-class");
    const nextBtn = $("#next-class");
    prevBtn.disabled = idx <= 0;
    nextBtn.disabled = idx < 0 || idx >= flat.length - 1;
    prevBtn.onclick = () => idx > 0 && loadClass(flat[idx - 1].slug);
    nextBtn.onclick = () => idx >= 0 && idx < flat.length - 1 && loadClass(flat[idx + 1].slug);

    $("#readme-link").onclick = (ev) => {
      ev.preventDefault();
      openReadme(slug, nb.title || slug);
    };

    const container = $("#cells-container");
    container.innerHTML = "";
    window._lab.cells = [];

    (nb.cells || []).forEach((cell, i) => {
      const rendered = renderCell(cell, i);
      container.appendChild(rendered.el);
      window._lab.cells.push(rendered);
    });

    if (!nb.cells || nb.cells.length === 0) {
      container.appendChild(el("div", {
        class: "tree-loading",
        text: "Este notebook no tiene celdas.",
      }));
    }
  }

  // ── Cell rendering ─────────────────────────────────────────
  function renderCell(cell, index) {
    const type = cell.type || cell.cell_type || "code";
    const cellId = cell.id || ("cell-" + index);

    if (type === "markdown" || type === "raw") {
      const wrap = el("div", { class: "cell cell-markdown" });
      const body = el("div", { class: "markdown-body" });
      if (cell.rendered_html) {
        body.innerHTML = cell.rendered_html;
      } else {
        const pre = el("pre");
        pre.textContent = sourceToString(cell.source);
        body.appendChild(pre);
      }
      wrap.appendChild(body);
      return { id: cellId, type: "markdown", el: wrap };
    }

    // code cell
    const source = sourceToString(cell.source);
    const wrap = el("div", { class: "cell cell-code" });

    const runBtn = el("button", { class: "cell-run-btn", type: "button", title: "Ejecutar (Ctrl+Enter)" }, "▶ Ejecutar");
    const execLabel = el("span", { class: "cell-exec-count", text: "[ ]" });
    const header = el("div", { class: "cell-code-header" }, [runBtn, execLabel]);

    const editor = el("textarea", {
      class: "cell-editor",
      spellcheck: "false",
      wrap: "off",
    });
    editor.value = source;
    const gutter = el("div", { class: "cell-gutter" });
    const editorWrap = el("div", { class: "cell-editor-wrap" }, [gutter, editor]);

    const outputs = el("div", { class: "cell-outputs" });
    // Pre-render any saved outputs (from the notebook file)
    if (Array.isArray(cell.outputs)) {
      cell.outputs.forEach(o => renderOutput(o, outputs));
    }
    if (cell.execution_count != null) {
      execLabel.textContent = "[" + cell.execution_count + "]";
    }

    wrap.appendChild(header);
    wrap.appendChild(editorWrap);
    wrap.appendChild(outputs);

    const cellObj = {
      id: cellId,
      type: "code",
      el: wrap,
      editorEl: editor,
      outputsEl: outputs,
      execLabelEl: execLabel,
      runBtnEl: runBtn,
      gutterEl: gutter,
    };

    runBtn.addEventListener("click", () => executeCell(cellObj));
    editor.addEventListener("input", () => {
      autoSizeEditor(editor, gutter);
    });
    editor.addEventListener("keydown", (ev) => {
      if (ev.key === "Enter" && (ev.ctrlKey || ev.metaKey)) {
        ev.preventDefault();
        executeCell(cellObj);
      } else if (ev.key === "Enter" && ev.shiftKey) {
        ev.preventDefault();
        executeCell(cellObj).then(() => focusNextCell(cellObj));
      } else if (ev.key === "Tab") {
        ev.preventDefault();
        const s = editor.selectionStart, e = editor.selectionEnd;
        editor.value = editor.value.slice(0, s) + "    " + editor.value.slice(e);
        editor.selectionStart = editor.selectionEnd = s + 4;
        autoSizeEditor(editor, gutter);
      }
    });

    // Initial sizing — defer to after the cell is in the DOM
    requestAnimationFrame(() => autoSizeEditor(editor, gutter));

    return cellObj;
  }

  function sourceToString(src) {
    if (src == null) return "";
    if (Array.isArray(src)) return src.join("");
    return String(src);
  }

  function autoSizeEditor(editor, gutter) {
    editor.style.height = "auto";
    const h = Math.max(editor.scrollHeight, 38);
    editor.style.height = h + "px";
    const lines = (editor.value.match(/\n/g) || []).length + 1;
    let g = "";
    for (let i = 1; i <= lines; i++) g += i + "\n";
    if (gutter) gutter.textContent = g;
  }

  function focusNextCell(currentCell) {
    const idx = window._lab.cells.indexOf(currentCell);
    for (let i = idx + 1; i < window._lab.cells.length; i++) {
      const c = window._lab.cells[i];
      if (c.type === "code") { c.editorEl.focus(); return; }
    }
  }

  // ── Outputs ────────────────────────────────────────────────
  function renderOutput(output, container) {
    const type = output.type || output.output_type || "stream";

    if (type === "stream") {
      const name = output.name || "stdout";
      const item = el("div", { class: "output-item output-stream-" + name });
      const pre = el("pre");
      pre.textContent = sourceToString(output.text);
      item.appendChild(pre);
      container.appendChild(item);
      return;
    }

    if (type === "error") {
      const item = el("div", { class: "output-item output-error" });
      const trace = Array.isArray(output.traceback)
        ? output.traceback.map(stripAnsi).join("\n")
        : (output.ename + ": " + output.evalue);
      const pre = el("pre");
      pre.textContent = trace;
      item.appendChild(pre);
      container.appendChild(item);
      return;
    }

    // execute_result / display_data
    const data = output.data || {};
    const item = el("div", { class: "output-item output-" + (type === "execute_result" ? "execute-result" : "display-data") });

    if (data["text/html"]) {
      const wrap = el("div", { class: "output-html" });
      wrap.innerHTML = Array.isArray(data["text/html"])
        ? data["text/html"].join("")
        : data["text/html"];
      item.appendChild(wrap);
    } else if (data["image/png"]) {
      const img = el("img");
      img.src = "data:image/png;base64," + data["image/png"];
      item.appendChild(img);
    } else if (data["image/jpeg"]) {
      const img = el("img");
      img.src = "data:image/jpeg;base64," + data["image/jpeg"];
      item.appendChild(img);
    } else if (data["text/plain"]) {
      const pre = el("pre");
      pre.textContent = sourceToString(data["text/plain"]);
      item.appendChild(pre);
    } else {
      const pre = el("pre");
      pre.textContent = JSON.stringify(output, null, 2);
      item.appendChild(pre);
    }
    container.appendChild(item);
  }

  // ── Kernel ─────────────────────────────────────────────────
  async function startKernel() {
    if (window._lab.kernelId) return window._lab.kernelId;
    setKernelStatus("starting");
    toast("Iniciando kernel…", "info");
    try {
      const data = await api("/api/kernel/start", { method: "POST" });
      window._lab.kernelId = data.kernel_id;
      $("#rp-kernel-id").textContent = (data.kernel_id || "").slice(0, 8) || "—";
      setKernelStatus("idle");
      toast("Kernel listo", "success");
      return data.kernel_id;
    } catch (e) {
      setKernelStatus("dead");
      toast("Error iniciando kernel: " + e.message, "error");
      throw e;
    }
  }

  async function executeCell(cellObj) {
    if (cellObj.type !== "code") return;
    try {
      if (!window._lab.kernelId) await startKernel();
    } catch { return; }

    setKernelStatus("busy");
    cellObj.runBtnEl.disabled = true;
    cellObj.execLabelEl.innerHTML = '<span class="cell-spinner"></span>';
    cellObj.outputsEl.innerHTML = "";

    const code = cellObj.editorEl.value;
    try {
      const data = await api("/api/kernel/" + window._lab.kernelId + "/execute", {
        method: "POST",
        body: { code: code },
      });
      (data.outputs || []).forEach(o => renderOutput(o, cellObj.outputsEl));
      const ec = data.execution_count != null ? data.execution_count : "*";
      cellObj.execLabelEl.textContent = "[" + ec + "]";
      window._lab.execCount += 1;
      $("#rp-exec-count").textContent = window._lab.execCount;
      setKernelStatus(data.status === "error" ? "idle" : "idle");
    } catch (e) {
      cellObj.execLabelEl.textContent = "[!]";
      const errItem = el("div", { class: "output-item output-error" }, el("pre", { text: "Error de red: " + e.message }));
      cellObj.outputsEl.appendChild(errItem);
      setKernelStatus("dead");
      toast("Fallo al ejecutar: " + e.message, "error");
    } finally {
      cellObj.runBtnEl.disabled = false;
    }
  }

  async function runAll() {
    for (const c of window._lab.cells) {
      if (c.type === "code") {
        await executeCell(c);
        if (window._lab.kernelStatus === "dead") break;
      }
    }
  }

  async function interruptKernel() {
    if (!window._lab.kernelId) { toast("No hay kernel activo", "info"); return; }
    try {
      await api("/api/kernel/" + window._lab.kernelId + "/interrupt", { method: "POST" });
      toast("Kernel interrumpido", "info");
      setKernelStatus("idle");
    } catch (e) { toast("Error: " + e.message, "error"); }
  }

  async function restartKernel() {
    if (!window._lab.kernelId) {
      await startKernel();
      return;
    }
    try {
      await api("/api/kernel/" + window._lab.kernelId + "/restart", { method: "POST" });
      toast("Kernel reiniciado", "success");
      window._lab.execCount = 0;
      $("#rp-exec-count").textContent = "0";
      setKernelStatus("idle");
    } catch (e) { toast("Error: " + e.message, "error"); }
  }

  async function shutdownKernel() {
    if (!window._lab.kernelId) return;
    try {
      await api("/api/kernel/" + window._lab.kernelId, { method: "DELETE" });
      window._lab.kernelId = null;
      $("#rp-kernel-id").textContent = "—";
      setKernelStatus("stopped");
      toast("Kernel apagado", "info");
    } catch (e) { toast("Error: " + e.message, "error"); }
  }

  // ── README overlay ─────────────────────────────────────────
  async function openReadme(slug, title) {
    const overlay = $("#readme-overlay");
    $("#readme-title").textContent = title || slug;
    $("#readme-body").innerHTML = '<div class="tree-loading">Cargando…</div>';
    overlay.classList.remove("hidden");
    try {
      const data = await api("/api/class/" + slug);
      $("#readme-body").innerHTML = data.html || data.content_html || "<p>Sin contenido.</p>";
    } catch (e) {
      $("#readme-body").innerHTML = '<p style="color:var(--danger)">No se pudo cargar: ' + e.message + "</p>";
    }
  }
  function closeReadme() { $("#readme-overlay").classList.add("hidden"); }

  // ── Right panel toggle ─────────────────────────────────────
  function applyRightPanel() {
    const shell = $(".shell");
    shell.classList.toggle("rightpanel-collapsed", window._lab.rightCollapsed);
  }

  // ── Init ───────────────────────────────────────────────────
  function bindEvents() {
    $("#theme-select").addEventListener("change", (e) => applyTheme(e.target.value));

    $("#right-toggle").addEventListener("click", () => {
      window._lab.rightCollapsed = !window._lab.rightCollapsed;
      localStorage.setItem(LS_KEYS.rightCollapsed, window._lab.rightCollapsed ? "1" : "0");
      applyRightPanel();
    });

    $("#search-input").addEventListener("input", (e) => renderSidebar(e.target.value));

    $("#run-all-btn").addEventListener("click", runAll);
    $("#restart-btn").addEventListener("click", restartKernel);
    $("#interrupt-btn").addEventListener("click", interruptKernel);

    $("#rp-restart").addEventListener("click", restartKernel);
    $("#rp-interrupt").addEventListener("click", interruptKernel);
    $("#rp-shutdown").addEventListener("click", shutdownKernel);

    $("#readme-close").addEventListener("click", closeReadme);

    $("#quick-first").addEventListener("click", () => {
      const f = window._lab.flatClasses[0];
      if (f) loadClass(f.slug);
    });
    $("#quick-last").addEventListener("click", () => {
      const arr = window._lab.flatClasses;
      if (arr.length) loadClass(arr[arr.length - 1].slug);
    });
    $("#quick-random").addEventListener("click", () => {
      const arr = window._lab.flatClasses;
      if (arr.length) loadClass(arr[Math.floor(Math.random() * arr.length)].slug);
    });

    // Global shortcuts: Esc closes README overlay
    document.addEventListener("keydown", (ev) => {
      if (ev.key === "Escape" && !$("#readme-overlay").classList.contains("hidden")) {
        closeReadme();
      }
    });
  }

  async function initApp() {
    applyTheme(window._lab.theme);
    applyRightPanel();
    setKernelStatus("stopped");
    bindEvents();
    await loadCurriculum();

    // Auto-load last opened class if still present
    const last = loadJSON(LS_KEYS.lastClass, null);
    if (last && window._lab.flatClasses.some(c => c.slug === last)) {
      // Ensure its part is expanded
      const meta = window._lab.flatClasses.find(c => c.slug === last);
      if (meta && meta.part_slug) {
        window._lab.expandedParts[meta.part_slug] = true;
        saveJSON(LS_KEYS.expanded, window._lab.expandedParts);
        renderSidebar($("#search-input").value);
      }
      loadClass(last);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initApp);
  } else {
    initApp();
  }
})();
