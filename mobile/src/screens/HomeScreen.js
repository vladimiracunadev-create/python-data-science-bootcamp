/**
 * HomeScreen.js — Pantalla principal: las 9 partes del programa
 *
 * Con 232 clases, una lista plana es inmanejable, asi que el Home muestra las
 * partes y el detalle de cada una vive en PartScreen.
 *
 * Muestra:
 *   - Header con el nombre del programa
 *   - Barra de progreso global: X/232 clases completadas
 *   - Lista de PartCards navegables, cada una con su propio progreso
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
import { PARTS, CLASSES, TOTAL_CLASSES, TOTAL_PARTS } from '../data/classes';
import PartCard from '../components/PartCard';
import { getProgress, clearProgress } from '../utils/progress';
import { colors, spacing, radius, fontSize, fontWeight } from '../theme';

export default function HomeScreen({ navigation }) {
  // Set con los IDs de clases completadas por el alumno
  const [completedIds, setCompletedIds] = useState(new Set());

  /**
   * useFocusEffect se ejecuta cada vez que la pantalla recibe el foco.
   * Esto refresca el progreso cuando el alumno vuelve de una parte o clase.
   */
  useFocusEffect(
    useCallback(() => {
      let active = true;
      getProgress().then((progress) => {
        if (active) setCompletedIds(progress);
      });
      return () => {
        active = false;
      };
    }, [])
  );

  const completedCount = completedIds.size;
  const progressPercent = TOTAL_CLASSES > 0 ? (completedCount / TOTAL_CLASSES) * 100 : 0;

  // Primera clase pendiente en orden de numeracion — el "seguir donde quedaste".
  const nextClass = CLASSES.find((item) => !completedIds.has(item.id));

  /** Cuenta cuantas clases de una parte estan completadas. */
  const completedInPart = (partId) =>
    CLASSES.reduce(
      (total, item) =>
        item.partSlug === partId && completedIds.has(item.id) ? total + 1 : total,
      0
    );

  /** Navega al listado de clases de una parte. */
  const handlePartPress = (part) => {
    navigation.navigate('Part', { partId: part.id, partTitle: `Parte ${part.number}` });
  };

  /** Salta directo a la siguiente clase pendiente. */
  const handleContinue = () => {
    if (!nextClass) return;
    navigation.navigate('Class', {
      classData: nextClass,
      classTitle: `Clase ${nextClass.number}`,
    });
  };

  /** Limpia todo el progreso tras tocar el contador. */
  const handleResetProgress = () => {
    clearProgress().then(() => setCompletedIds(new Set()));
  };

  // ── Render ───────────────────────────────────────────────

  const renderHeader = () => (
    <View style={styles.headerContainer}>
      <Text style={styles.mainTitle}>Python Data Science Program</Text>
      <Text style={styles.subtitle}>
        {TOTAL_CLASSES} clases en {TOTAL_PARTS} partes
      </Text>

      {/* Barra de progreso global */}
      <View style={styles.progressContainer}>
        <View style={styles.progressLabelRow}>
          <Text style={styles.progressLabel}>Tu progreso</Text>
          <TouchableOpacity onPress={handleResetProgress}>
            <Text style={styles.progressCount}>
              {completedCount}/{TOTAL_CLASSES} clases
            </Text>
          </TouchableOpacity>
        </View>

        <View style={styles.progressTrack}>
          <View style={[styles.progressFill, { width: `${progressPercent}%` }]} />
        </View>

        <Text style={styles.progressHint}>
          {completedCount === TOTAL_CLASSES
            ? 'Programa completado'
            : `${Math.round(progressPercent)}% · siguiente: clase ${nextClass?.number ?? 1}`}
        </Text>

        {/* Atajo a la siguiente clase pendiente */}
        {nextClass ? (
          <TouchableOpacity style={styles.continueButton} onPress={handleContinue}>
            <Text style={styles.continueButtonText} numberOfLines={1}>
              Continuar: {nextClass.title}
            </Text>
          </TouchableOpacity>
        ) : null}
      </View>

      <View style={styles.tipBox}>
        <Text style={styles.tipText}>
          Toca una parte para ver sus clases. Cada clase trae objetivo, resultados, temas,
          materiales y practica, y se abre en{' '}
          <Text style={styles.tipAccent}>Colab</Text> si necesitas ejecutarla.
        </Text>
      </View>
    </View>
  );

  const renderFooter = () => (
    <View style={styles.footer}>
      <Text style={styles.footerText}>
        El contenido está disponible sin conexión. Google Colab requiere internet.
      </Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <FlatList
        data={PARTS}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <PartCard
            part={item}
            completed={completedInPart(item.id)}
            onPress={() => handlePartPress(item)}
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
    paddingBottom: spacing.xl,
  },

  // Header
  headerContainer: {
    paddingHorizontal: spacing.md,
    paddingTop: spacing.lg,
    paddingBottom: spacing.sm,
  },
  mainTitle: {
    color: colors.text,
    fontSize: 24,
    fontWeight: fontWeight.bold,
    marginBottom: 4,
  },
  subtitle: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
    marginBottom: spacing.lg,
  },

  // Progreso global
  progressContainer: {
    backgroundColor: colors.bgCard,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
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
    fontSize: fontSize.md,
    fontWeight: fontWeight.medium,
  },
  progressCount: {
    color: colors.accent,
    fontSize: fontSize.md,
    fontWeight: fontWeight.bold,
  },
  progressTrack: {
    height: 8,
    backgroundColor: colors.bgMuted,
    borderRadius: radius.sm,
    overflow: 'hidden',
    marginBottom: spacing.sm,
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: radius.sm,
  },
  progressHint: {
    color: colors.textMuted,
    fontSize: fontSize.xs,
  },
  continueButton: {
    marginTop: spacing.md,
    backgroundColor: colors.accent,
    borderRadius: radius.md,
    paddingVertical: 10,
    paddingHorizontal: spacing.md,
    alignItems: 'center',
  },
  continueButtonText: {
    color: '#000',
    fontSize: fontSize.sm,
    fontWeight: fontWeight.bold,
  },

  // Tip
  tipBox: {
    backgroundColor: colors.bgMuted,
    borderRadius: radius.sm,
    padding: spacing.sm + 4,
    marginBottom: spacing.sm,
    borderLeftWidth: 3,
    borderLeftColor: colors.accent,
  },
  tipText: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
    lineHeight: 19,
  },
  tipAccent: {
    color: colors.accent,
    fontWeight: fontWeight.medium,
  },

  // Footer
  footer: {
    paddingHorizontal: spacing.md,
    paddingTop: spacing.md,
    alignItems: 'center',
  },
  footerText: {
    color: '#475569',
    fontSize: fontSize.xs,
    textAlign: 'center',
  },
});
