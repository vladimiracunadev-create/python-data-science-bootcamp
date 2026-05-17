// ============================================================
// UTILIDADES PARA GOOGLE COLAB
// Genera URLs para abrir notebooks directamente en Colab
// ============================================================

/**
 * Genera una URL de Google Colab a partir de un notebook en GitHub.
 *
 * @param {string} githubUser - Usuario de GitHub
 * @param {string} repo - Nombre del repositorio
 * @param {string} branch - Nombre de la rama (ej: 'master', 'main')
 * @param {string} notebookPath - Ruta relativa al notebook dentro del repo
 * @returns {string} URL completa de Google Colab
 *
 * @example
 * getColabUrl('usuario', 'repo', 'master', 'classes/01/notebook.ipynb')
 * // → 'https://colab.research.google.com/github/usuario/repo/blob/master/classes/01/notebook.ipynb'
 */
export const getColabUrl = (githubUser, repo, branch, notebookPath) => {
  const base = 'https://colab.research.google.com/github';
  return `${base}/${githubUser}/${repo}/blob/${branch}/${notebookPath}`;
};

/**
 * Configuracion del repositorio GitHub del bootcamp.
 * Cambiar aqui si el repo cambia de nombre o usuario.
 */
export const GITHUB_CONFIG = {
  user: 'vladimiracunadev-create',
  repo: 'python-data-science-bootcamp',
  branch: 'master',
};

/**
 * Genera la URL de Colab para una clase especifica usando la configuracion global.
 *
 * @param {string} classFolder - Carpeta de la clase (ej: '01-python-fundamentos')
 * @returns {string} URL de Colab
 */
export const getClassColabUrl = (classFolder) => {
  const { user, repo, branch } = GITHUB_CONFIG;
  const notebookPath = `classes/${classFolder}/notebook.ipynb`;
  return getColabUrl(user, repo, branch, notebookPath);
};
