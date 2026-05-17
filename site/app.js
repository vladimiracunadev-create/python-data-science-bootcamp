const studentLink = document.getElementById("studentLink");
const copyLinkBtn = document.getElementById("copyLinkBtn");

if (copyLinkBtn && studentLink) {
  copyLinkBtn.addEventListener("click", async () => {
    const value = studentLink.textContent.trim();
    try {
      await navigator.clipboard.writeText(value);
      copyLinkBtn.textContent = "Copiado";
      window.setTimeout(() => {
        copyLinkBtn.textContent = "Copiar";
      }, 1600);
    } catch {
      copyLinkBtn.textContent = "Copia manual";
    }
  });
}
