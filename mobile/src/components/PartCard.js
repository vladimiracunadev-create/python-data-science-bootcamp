// ============================================================
// COMPONENTE: PartCard
// Tarjeta de una de las 9 partes del programa, en el HomeScreen
// ============================================================

import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { colors, spacing, radius, fontSize, fontWeight, levelColor } from '../theme';

/**
 * PartCard — tarjeta de parte para el HomeScreen.
 *
 * Props:
 *   part      {object}   - Objeto de parte de classes.js (PARTS)
 *   completed {number}   - Clases completadas dentro de esta parte
 *   onPress   {function} - Callback al tocar la tarjeta
 */
const PartCard = ({ part, completed, onPress }) => {
  const { number, title, subtitle, level, classCount, firstClass, lastClass } = part;

  const percent = classCount > 0 ? (completed / classCount) * 100 : 0;
  const isDone = classCount > 0 && completed === classCount;
  const lvlColor = levelColor(level);

  return (
    <TouchableOpacity
      style={[styles.card, isDone && styles.cardCompleted]}
      onPress={onPress}
      activeOpacity={0.85}
    >
      <View style={styles.headerRow}>
        {/* Badge con el numero de parte */}
        <View style={[styles.numberBadge, isDone && styles.numberBadgeCompleted]}>
          <Text style={[styles.numberText, isDone && styles.numberTextCompleted]}>{number}</Text>
        </View>

        <View style={styles.titleArea}>
          <Text style={styles.title} numberOfLines={1}>
            {title}
          </Text>
          <Text style={styles.subtitle} numberOfLines={2}>
            {subtitle}
          </Text>
        </View>
      </View>

      {/* Badges: nivel y rango de clases */}
      <View style={styles.badgesRow}>
        <View style={[styles.levelBadge, { borderColor: lvlColor }]}>
          <Text style={[styles.levelText, { color: lvlColor }]}>{level}</Text>
        </View>
        <View style={styles.rangeBadge}>
          <Text style={styles.rangeText}>
            {classCount} clases · {firstClass}–{lastClass}
          </Text>
        </View>
      </View>

      {/* Progreso dentro de la parte */}
      <View style={styles.progressTrack}>
        <View style={[styles.progressFill, { width: `${percent}%` }]} />
      </View>
      <Text style={styles.progressText}>
        {completed}/{classCount} completadas
      </Text>
    </TouchableOpacity>
  );
};

// ─── Estilos ─────────────────────────────────────────────────
const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.bgCard,
    borderRadius: radius.lg,
    padding: spacing.md,
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
    borderWidth: 1,
    borderColor: colors.border,
    elevation: 2,
  },
  cardCompleted: {
    borderColor: `${colors.accent}55`,
    backgroundColor: '#1a2e1a',
  },

  headerRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.md,
    marginBottom: spacing.sm,
  },
  numberBadge: {
    width: 44,
    height: 44,
    borderRadius: radius.md,
    backgroundColor: `${colors.accent}22`,
    borderWidth: 1.5,
    borderColor: colors.accent,
    alignItems: 'center',
    justifyContent: 'center',
    flexShrink: 0,
  },
  numberBadgeCompleted: {
    backgroundColor: colors.accent,
  },
  numberText: {
    color: colors.accent,
    fontSize: fontSize.lg,
    fontWeight: fontWeight.bold,
    fontFamily: 'monospace',
  },
  numberTextCompleted: {
    color: '#000',
  },
  titleArea: {
    flex: 1,
  },
  title: {
    color: colors.text,
    fontSize: fontSize.lg,
    fontWeight: fontWeight.bold,
    marginBottom: 2,
  },
  subtitle: {
    color: colors.textMuted,
    fontSize: fontSize.sm,
    lineHeight: 18,
  },

  badgesRow: {
    flexDirection: 'row',
    gap: spacing.sm,
    flexWrap: 'wrap',
    marginBottom: spacing.md,
  },
  levelBadge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: 2,
    borderRadius: radius.full,
    borderWidth: 1,
  },
  levelText: {
    fontSize: fontSize.xs,
    fontWeight: fontWeight.medium,
  },
  rangeBadge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: 2,
    borderRadius: radius.full,
    backgroundColor: colors.bgMuted,
  },
  rangeText: {
    color: colors.textMuted,
    fontSize: fontSize.xs,
  },

  progressTrack: {
    height: 6,
    backgroundColor: colors.bgMuted,
    borderRadius: radius.sm,
    overflow: 'hidden',
    marginBottom: spacing.xs,
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: radius.sm,
  },
  progressText: {
    color: colors.textMuted,
    fontSize: fontSize.xs,
  },
});

export default PartCard;
