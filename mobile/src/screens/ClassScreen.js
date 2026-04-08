/**
 * ClassScreen.js — Pantalla de detalle de una clase
 *
 * Muestra:
 *   - Header: numero, titulo, nivel, duración
 *   - Pestañas: Teoria | Ejercicios
 *   - Botón flotante "▶ Colab" que abre el notebook en Google Colab
 *   - Boton "Marcar como completada" al pie
 *
 * La clase recibe el objeto completo via route.params.classData
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
  Linking,
  Alert,
} from 'react-native';
import CodeBlock from '../components/CodeBlock';
import { saveProgress, removeProgress, isClassCompleted } from '../utils/progress';

// ── Constantes de diseño ─────────────────────────────────────
const colors = {
  bg: '#0f0f1a',
  bgCard: '#1a1a2e',
  bgCode: '#0d1117',
  accent: '#22c55e',
  accentBlue: '#3b82f6',
  text: '#f1f5f9',
  textMuted: '#94a3b8',
  border: '#334155',
  warning: '#f59e0b',
};

// ── Badges de nivel ──────────────────────────────────────────
const LEVEL_COLORS = {
  Basico: '#22c55e',
  Intermedio: '#3b82f6',
  'Intermedio-Avanzado': '#8b5cf6',
  Avanzado: '#ef4444',
  Integrador: '#f59e0b',
};

export default function ClassScreen({ route }) {
  // Extraer los datos de la clase de los parámetros de navegación
  const { classData } = route.params;

  // Pestaña activa: 'theory' o 'exercises'
  const [activeTab, setActiveTab] = useState('theory');

  // Estado de completado de la clase
  const [completed, setCompleted] = useState(false);

  // Al montar la pantalla, verificar si la clase ya está completada
  useEffect(() => {
    isClassCompleted(classData.id).then(setCompleted);
  }, [classData.id]);

  /**
   * Abre el notebook de la clase en Google Colab usando el URL del navegador.
   * Requiere conexión a internet.
   */
  const handleOpenColab = async () => {
    const url = classData.colabUrl;
    const canOpen = await Linking.canOpenURL(url);
    if (canOpen) {
      await Linking.openURL(url);
    } else {
      Alert.alert(
        'No se pudo abrir Colab',
        'Verifica que tengas conexion a internet y un navegador instalado.',
        [{ text: 'OK' }]
      );
    }
  };

  /**
   * Alterna el estado de completado de la clase.
   * Guarda/elimina del almacenamiento local.
   */
  const handleToggleCompleted = async () => {
    if (completed) {
      await removeProgress(classData.id);
      setCompleted(false);
    } else {
      await saveProgress(classData.id);
      setCompleted(true);
    }
  };

  // ── Componentes internos ─────────────────────────────────

  /**
   * Renderiza la pestaña de teoría: texto explicativo + ejemplos de código
   */
  const TheoryTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      {/* Texto de teoría introductoria */}
      {classData.theory ? (
        <View style={styles.theoryCard}>
          <Text style={styles.theoryText}>{classData.theory}</Text>
        </View>
      ) : null}

      {/* Lista de temas */}
      <View style={styles.topicsContainer}>
        <Text style={styles.sectionTitle}>Temas de esta clase</Text>
        {classData.topics.map((topic, index) => (
          <View key={index} style={styles.topicRow}>
            {/* Punto verde como bullet */}
            <View style={styles.topicBullet} />
            <Text style={styles.topicText}>{topic}</Text>
          </View>
        ))}
      </View>

      {/* Ejemplos de código documentados */}
      <Text style={styles.sectionTitle}>Ejemplos de codigo</Text>
      {classData.codeExamples.map((example) => (
        <View key={example.id} style={styles.exampleContainer}>
          {/* Título del ejemplo */}
          <View style={styles.exampleHeader}>
            <Text style={styles.exampleTitle}>{example.title}</Text>
          </View>

          {/* Explicación textual del concepto */}
          <Text style={styles.exampleExplanation}>{example.explanation}</Text>

          {/* Esquema ASCII del concepto (si existe) */}
          {example.schema ? (
            <View style={styles.schemaBox}>
              <Text style={styles.schemaText}>{example.schema}</Text>
            </View>
          ) : null}

          {/* Bloque de código con syntax highlighting */}
          <CodeBlock
            code={example.code}
            language={example.language ?? 'python'}
            title={example.title}
          />
        </View>
      ))}

      {/* Padding inferior para no tapar el botón flotante */}
      <View style={{ height: 100 }} />
    </ScrollView>
  );

  /**
   * Renderiza la pestaña de ejercicios
   */
  const ExercisesTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <View style={styles.exercisesIntro}>
        <Text style={styles.exercisesIntroText}>
          Practica con los ejercicios de esta clase. Puedes:
        </Text>
        <View style={styles.exerciseOption}>
          <Text style={styles.exerciseOptionBullet}>①</Text>
          <Text style={styles.exerciseOptionText}>
            Leer el codigo aqui y copiarlo para practicar en tu entorno local.
          </Text>
        </View>
        <View style={styles.exerciseOption}>
          <Text style={styles.exerciseOptionBullet}>②</Text>
          <Text style={styles.exerciseOptionText}>
            Tocar <Text style={styles.accentText}>▶ Colab</Text> para abrir el
            notebook completo en Google Colab y ejecutar celda a celda.
          </Text>
        </View>
      </View>

      {/* Mostrar ejemplos de código como ejercicios */}
      {classData.codeExamples.map((example, index) => (
        <View key={example.id} style={styles.exerciseBlock}>
          <Text style={styles.exerciseNumber}>Ejercicio {index + 1}</Text>
          <Text style={styles.exerciseTitle}>{example.title}</Text>
          <Text style={styles.exerciseDescription}>{example.explanation}</Text>

          {example.schema ? (
            <View style={styles.schemaBox}>
              <Text style={styles.schemaText}>{example.schema}</Text>
            </View>
          ) : null}

          <CodeBlock
            code={example.code}
            language={example.language ?? 'python'}
          />
        </View>
      ))}

      <View style={{ height: 100 }} />
    </ScrollView>
  );

  // ── Render principal ─────────────────────────────────────

  return (
    <SafeAreaView style={styles.safeArea}>
      {/* ── Información de la clase ── */}
      <View style={styles.classInfo}>
        <View style={styles.classInfoRow}>
          {/* Numero de clase en circulo verde */}
          <View style={styles.classNumber}>
            <Text style={styles.classNumberText}>{classData.number}</Text>
          </View>

          <View style={styles.classInfoText}>
            <Text style={styles.classTitle}>{classData.title}</Text>
            <View style={styles.badgesRow}>
              {/* Badge de nivel */}
              <View style={[
                styles.levelBadge,
                { backgroundColor: LEVEL_COLORS[classData.level] ?? colors.accent }
              ]}>
                <Text style={styles.levelBadgeText}>{classData.level}</Text>
              </View>
              {/* Badge de duración */}
              <View style={styles.durationBadge}>
                <Text style={styles.durationText}>⏱ {classData.duration}</Text>
              </View>
            </View>
          </View>
        </View>
      </View>

      {/* ── Pestañas de navegación ── */}
      <View style={styles.tabBar}>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'theory' && styles.tabActive]}
          onPress={() => setActiveTab('theory')}
        >
          <Text style={[styles.tabText, activeTab === 'theory' && styles.tabTextActive]}>
            Teoria y Codigo
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.tab, activeTab === 'exercises' && styles.tabActive]}
          onPress={() => setActiveTab('exercises')}
        >
          <Text style={[styles.tabText, activeTab === 'exercises' && styles.tabTextActive]}>
            Ejercicios
          </Text>
        </TouchableOpacity>
      </View>

      {/* ── Contenido de la pestaña activa ── */}
      <View style={styles.contentArea}>
        {activeTab === 'theory' ? <TheoryTab /> : <ExercisesTab />}
      </View>

      {/* ── Botones flotantes ── */}
      <View style={styles.floatingBar}>
        {/* Marcar como completada */}
        <TouchableOpacity
          style={[styles.completeButton, completed && styles.completeButtonDone]}
          onPress={handleToggleCompleted}
        >
          <Text style={styles.completeButtonText}>
            {completed ? '✓ Completada' : 'Marcar completada'}
          </Text>
        </TouchableOpacity>

        {/* Abrir en Colab */}
        <TouchableOpacity style={styles.colabButton} onPress={handleOpenColab}>
          <Text style={styles.colabButtonText}>▶ Colab</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

// ── Estilos ──────────────────────────────────────────────────
const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.bg,
  },

  // Información de clase
  classInfo: {
    backgroundColor: colors.bgCard,
    paddingHorizontal: 16,
    paddingVertical: 14,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  classInfoRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  classNumber: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
  },
  classNumberText: {
    color: '#000',
    fontSize: 18,
    fontWeight: '800',
  },
  classInfoText: {
    flex: 1,
  },
  classTitle: {
    color: colors.text,
    fontSize: 17,
    fontWeight: '700',
    marginBottom: 6,
  },
  badgesRow: {
    flexDirection: 'row',
    gap: 8,
  },
  levelBadge: {
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 4,
  },
  levelBadgeText: {
    color: '#000',
    fontSize: 11,
    fontWeight: '700',
  },
  durationBadge: {
    backgroundColor: '#1e293b',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 4,
  },
  durationText: {
    color: colors.textMuted,
    fontSize: 11,
  },

  // Tab bar
  tabBar: {
    flexDirection: 'row',
    backgroundColor: colors.bgCard,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  tab: {
    flex: 1,
    paddingVertical: 12,
    alignItems: 'center',
  },
  tabActive: {
    borderBottomWidth: 2,
    borderBottomColor: colors.accent,
  },
  tabText: {
    color: colors.textMuted,
    fontSize: 14,
    fontWeight: '500',
  },
  tabTextActive: {
    color: colors.accent,
    fontWeight: '700',
  },

  // Content
  contentArea: {
    flex: 1,
  },
  tabContent: {
    flex: 1,
    paddingHorizontal: 16,
    paddingTop: 16,
  },

  // Theory
  theoryCard: {
    backgroundColor: colors.bgCard,
    borderRadius: 10,
    padding: 14,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: colors.border,
  },
  theoryText: {
    color: colors.text,
    fontSize: 14,
    lineHeight: 22,
  },

  // Topics
  topicsContainer: {
    marginBottom: 20,
  },
  sectionTitle: {
    color: colors.text,
    fontSize: 16,
    fontWeight: '700',
    marginBottom: 10,
    marginTop: 4,
  },
  topicRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 7,
    gap: 10,
  },
  topicBullet: {
    width: 7,
    height: 7,
    borderRadius: 3.5,
    backgroundColor: colors.accent,
  },
  topicText: {
    color: colors.textMuted,
    fontSize: 14,
  },

  // Code examples
  exampleContainer: {
    marginBottom: 24,
  },
  exampleHeader: {
    backgroundColor: '#134e2a',
    borderRadius: 6,
    paddingHorizontal: 12,
    paddingVertical: 6,
    marginBottom: 8,
  },
  exampleTitle: {
    color: colors.accent,
    fontSize: 13,
    fontWeight: '700',
  },
  exampleExplanation: {
    color: colors.text,
    fontSize: 14,
    lineHeight: 21,
    marginBottom: 8,
  },

  // Schema box
  schemaBox: {
    backgroundColor: '#0f172a',
    borderRadius: 6,
    padding: 12,
    marginBottom: 10,
    borderLeftWidth: 3,
    borderLeftColor: colors.accentBlue,
  },
  schemaText: {
    color: '#93c5fd',
    fontFamily: 'monospace',
    fontSize: 11,
    lineHeight: 17,
  },

  // Exercises
  exercisesIntro: {
    backgroundColor: colors.bgCard,
    borderRadius: 10,
    padding: 14,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: colors.border,
  },
  exercisesIntroText: {
    color: colors.textMuted,
    fontSize: 13,
    marginBottom: 10,
  },
  exerciseOption: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 6,
  },
  exerciseOptionBullet: {
    color: colors.accent,
    fontSize: 15,
    fontWeight: '700',
  },
  exerciseOptionText: {
    flex: 1,
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 19,
  },
  accentText: {
    color: colors.accent,
    fontWeight: '600',
  },
  exerciseBlock: {
    marginBottom: 24,
  },
  exerciseNumber: {
    color: colors.accentBlue,
    fontSize: 11,
    fontWeight: '700',
    textTransform: 'uppercase',
    letterSpacing: 0.5,
    marginBottom: 4,
  },
  exerciseTitle: {
    color: colors.text,
    fontSize: 15,
    fontWeight: '700',
    marginBottom: 6,
  },
  exerciseDescription: {
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 19,
    marginBottom: 8,
  },

  // Floating bar
  floatingBar: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    flexDirection: 'row',
    gap: 10,
    padding: 12,
    backgroundColor: colors.bgCard,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  completeButton: {
    flex: 1,
    backgroundColor: '#1e293b',
    borderRadius: 10,
    paddingVertical: 13,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  completeButtonDone: {
    backgroundColor: '#134e2a',
    borderColor: colors.accent,
  },
  completeButtonText: {
    color: colors.text,
    fontSize: 14,
    fontWeight: '600',
  },
  colabButton: {
    flex: 1,
    backgroundColor: colors.accent,
    borderRadius: 10,
    paddingVertical: 13,
    alignItems: 'center',
  },
  colabButtonText: {
    color: '#000',
    fontSize: 14,
    fontWeight: '800',
  },
});
