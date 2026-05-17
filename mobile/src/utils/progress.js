// ============================================================
// UTILIDADES DE PROGRESO DEL ESTUDIANTE
// Usa AsyncStorage para persistir el progreso localmente
// Los datos sobreviven al cierre de la app
// ============================================================

import AsyncStorage from '@react-native-async-storage/async-storage';

// Clave de AsyncStorage donde guardamos el progreso
const PROGRESS_KEY = '@bootcamp_python_ds:progress';

/**
 * Marca una clase como completada y la persiste en AsyncStorage.
 *
 * @param {string} classId - ID de la clase (ej: '01-python-fundamentos')
 * @returns {Promise<Set<string>>} - Set actualizado de clases completadas
 */
export const saveProgress = async (classId) => {
  try {
    // Obtener el progreso actual
    const current = await getProgress();

    // Agregar la nueva clase al Set
    current.add(classId);

    // Convertir Set a Array para poder guardarlo como JSON
    // (AsyncStorage solo guarda strings)
    const progressArray = Array.from(current);
    await AsyncStorage.setItem(PROGRESS_KEY, JSON.stringify(progressArray));

    console.log(`Progreso guardado: clase ${classId} completada`);
    return current;
  } catch (error) {
    console.error('Error al guardar progreso:', error);
    // Devuelve el Set con la clase nueva aunque falle el guardado
    return new Set([classId]);
  }
};

/**
 * Obtiene el progreso guardado del estudiante.
 *
 * @returns {Promise<Set<string>>} - Set con los IDs de clases completadas
 *                                   (Set vacio si no hay progreso guardado)
 */
export const getProgress = async () => {
  try {
    // Obtener el string JSON guardado
    const jsonValue = await AsyncStorage.getItem(PROGRESS_KEY);

    if (jsonValue === null) {
      // No hay progreso guardado todavia: devolver Set vacio
      return new Set();
    }

    // Parsear el JSON y convertir de Array a Set
    const progressArray = JSON.parse(jsonValue);
    return new Set(progressArray);
  } catch (error) {
    console.error('Error al leer progreso:', error);
    return new Set(); // En caso de error, devolver Set vacio
  }
};

/**
 * Elimina el progreso de una clase especifica (des-marcar como completada).
 *
 * @param {string} classId - ID de la clase a des-marcar
 * @returns {Promise<Set<string>>} - Set actualizado
 */
export const removeProgress = async (classId) => {
  try {
    const current = await getProgress();
    current.delete(classId); // .delete() elimina del Set si existe

    const progressArray = Array.from(current);
    await AsyncStorage.setItem(PROGRESS_KEY, JSON.stringify(progressArray));

    return current;
  } catch (error) {
    console.error('Error al eliminar progreso:', error);
    return await getProgress();
  }
};

/**
 * Verifica si una clase especifica esta marcada como completada.
 *
 * @param {string} classId - ID de la clase a verificar
 * @returns {Promise<boolean>} - true si esta completada, false si no
 */
export const isClassCompleted = async (classId) => {
  const progress = await getProgress();
  return progress.has(classId);
};

/**
 * Limpia todo el progreso del estudiante.
 * Util para reiniciar el bootcamp.
 *
 * @returns {Promise<void>}
 */
export const clearProgress = async () => {
  try {
    await AsyncStorage.removeItem(PROGRESS_KEY);
    console.log('Progreso eliminado completamente');
  } catch (error) {
    console.error('Error al limpiar progreso:', error);
  }
};

/**
 * Obtiene el conteo de clases completadas.
 *
 * @returns {Promise<number>} - Numero de clases completadas
 */
export const getCompletedCount = async () => {
  const progress = await getProgress();
  return progress.size;
};
