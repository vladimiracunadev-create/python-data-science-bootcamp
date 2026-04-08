/**
 * HomeScreen.js — Pantalla principal: lista de 12 clases con progreso
 *
 * Muestra:
 *   - Header con nombre del bootcamp
 *   - Barra de progreso: X/12 clases completadas
 *   - Lista de ClassCards navegables
 *   - Nota de uso al pie
 */

import React, { useState, useCallback } from 'react';
import {
  View,
  Text,
  FlatList,
  StyleSheet,
  SafeAreaView,
  TouchableOpacity,
} from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { CLASSES } from '../data/classes';
import ClassCard from '../components/ClassCard';
import { getProgress, clearProgress } from '../utils/progress';

// ── Constantes de diseño ─────────────────────────────────────
const colors = {
  bg: '#0f0f1a',
  bgCard: '#1a1a2e',
  accent: '#22c55e',
  text: '#f1f5f9',
  textMuted: '#94a3b8',
  border: '#334155',
};

export default function HomeScreen({ navigation }) {
  // Set con los IDs de clases completadas por el alumno
  const [completedIds, setCompletedIds] = useState(new Set());

  /**
   * useFocusEffect se ejecuta cada vez que la pantalla recibe el foco.
   * Esto actualiza el progreso cuando el alumno vuelve de una clase.
   */
  useFocusEffect(
    useCallback(() => {
      let active = true;
      getProgress().then((progress) => {
        if (active) setCompletedIds(progress);
      });
      return () => { active = false; };
    }, [])
  );

  // Porcentaje de avance (0-100)
  const completedCount = completedIds.size;
  const totalClasses = CLASSES.length;
  const progressPercent = totalClasses > 0 ? (completedCount / totalClasses) * 100 : 0;
  const nextClass = CLASSES.find((item) => !completedIds.has(item.id));

  /**
   * Navega a la pantalla de detalle de una clase.
   * Pasa el objeto clase completo como parámetro de ruta.
   */
  const handleClassPress = (classItem) => {
    navigation.navigate('Class', {
      classData: classItem,
      classTitle: `Clase ${classItem.number}: ${classItem.title}`,
    });
  };

  /**
   * Limpia todo el progreso tras confirmación implícita (tap en el badge).
   */
  const handleResetProgress = () => {
    clearProgress().then(() => setCompletedIds(new Set()));
  };

  // ── Render ───────────────────────────────────────────────

  const renderHeader = () => (
    <View style={styles.headerContainer}>
      {/* Titulo principal */}
      <Text style={styles.mainTitle}>Bootcamp Python DS</Text>
      <Text style={styles.subtitle}>
        Clase 0 diagnostica + 12 clases troncales
      </Text>

      {/* Barra de progreso */}
      <View style={styles.progressContainer}>
        <View style={styles.progressLabelRow}>
          <Text style={styles.progressLabel}>Tu progreso</Text>
          <TouchableOpacity onPress={handleResetProgress}>
            <Text style={styles.progressCount}>
              {completedCount}/{totalClasses} clases
            </Text>
          </TouchableOpacity>
        </View>

        {/* Track de la barra */}
        <View style={styles.progressTrack}>
          {/* Relleno verde proporcional al avance */}
          <View style={[styles.progressFill, { width: `${progressPercent}%` }]} />
        </View>

        <Text style={styles.progressHint}>
          {completedCount === 0
            ? 'Comienza con la Clase 0'
            : completedCount === totalClasses
            ? 'Bootcamp completado'
            : `Siguiente: Clase ${nextClass?.number ?? 0}`}
        </Text>
      </View>

      {/* Nota de uso */}
      <View style={styles.tipBox}>
        <Text style={styles.tipText}>
          Toca una clase para leer teoria, materiales y codigo documentado. Si el modulo tiene
          notebook, usa <Text style={styles.tipAccent}>Abrir en Colab</Text> para practicarlo.
        </Text>
      </View>
    </View>
  );

  const renderFooter = () => (
    <View style={styles.footer}>
      <Text style={styles.footerText}>
        El contenido esta disponible sin conexion. Google Colab requiere internet.
      </Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <FlatList
        data={CLASSES}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <ClassCard
            classData={item}
            completed={completedIds.has(item.id)}
            onPress={() => handleClassPress(item)}
          />
        )}
        ListHeaderComponent={renderHeader}
        ListFooterComponent={renderFooter}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
      />
    </SafeAreaView>
  );
}

// ── Estilos ──────────────────────────────────────────────────
const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.bg,
  },
  listContent: {
    paddingBottom: 32,
  },

  // Header
  headerContainer: {
    paddingHorizontal: 16,
    paddingTop: 20,
    paddingBottom: 8,
  },
  mainTitle: {
    color: colors.text,
    fontSize: 24,
    fontWeight: '800',
    marginBottom: 4,
  },
  subtitle: {
    color: colors.textMuted,
    fontSize: 13,
    marginBottom: 20,
  },

  // Progreso
  progressContainer: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: colors.border,
  },
  progressLabelRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  progressLabel: {
    color: colors.text,
    fontSize: 14,
    fontWeight: '600',
  },
  progressCount: {
    color: colors.accent,
    fontSize: 14,
    fontWeight: '700',
  },
  progressTrack: {
    height: 8,
    backgroundColor: '#1e293b',
    borderRadius: 4,
    overflow: 'hidden',
    marginBottom: 8,
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: 4,
  },
  progressHint: {
    color: colors.textMuted,
    fontSize: 12,
  },

  // Tip
  tipBox: {
    backgroundColor: '#1e293b',
    borderRadius: 8,
    padding: 12,
    marginBottom: 8,
    borderLeftWidth: 3,
    borderLeftColor: colors.accent,
  },
  tipText: {
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 19,
  },
  tipAccent: {
    color: colors.accent,
    fontWeight: '600',
  },

  // Footer
  footer: {
    paddingHorizontal: 16,
    paddingTop: 16,
    alignItems: 'center',
  },
  footerText: {
    color: '#475569',
    fontSize: 11,
    textAlign: 'center',
  },
});
