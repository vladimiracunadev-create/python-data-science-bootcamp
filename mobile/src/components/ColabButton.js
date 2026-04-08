// ============================================================
// COMPONENTE: ColabButton
// Boton flotante para abrir el notebook en Google Colab
// ============================================================

import React, { useState } from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
  Linking,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { colors, spacing, radius, fontSize, fontWeight } from '../theme';

/**
 * ColabButton — boton de accion para abrir Google Colab.
 *
 * Props:
 *   url      {string}  - URL del notebook en Colab
 *   style    {object}  - Estilos adicionales
 *   compact  {boolean} - Version pequeña (sin texto, solo icono)
 */
const ColabButton = ({ url, style, compact = false }) => {
  const [loading, setLoading] = useState(false);

  const handlePress = async () => {
    if (!url) {
      Alert.alert(
        'Notebook no disponible',
        'El enlace a este notebook no esta configurado aun.',
        [{ text: 'OK' }]
      );
      return;
    }

    try {
      setLoading(true);

      // Verificar si se puede abrir la URL
      const canOpen = await Linking.canOpenURL(url);

      if (canOpen) {
        await Linking.openURL(url);
      } else {
        Alert.alert(
          'No se puede abrir',
          'No se pudo abrir Google Colab. Asegurate de tener conexion a internet.',
          [{ text: 'OK' }]
        );
      }
    } catch (error) {
      Alert.alert(
        'Error',
        'Ocurrio un error al intentar abrir Colab. Intenta de nuevo.',
        [{ text: 'OK' }]
      );
      console.error('Error al abrir Colab:', error);
    } finally {
      setLoading(false);
    }
  };

  if (compact) {
    return (
      <TouchableOpacity
        style={[styles.compactButton, style]}
        onPress={handlePress}
        activeOpacity={0.8}
        disabled={loading}
      >
        {loading ? (
          <ActivityIndicator size="small" color="#000" />
        ) : (
          <Text style={styles.compactIcon}>▶</Text>
        )}
      </TouchableOpacity>
    );
  }

  return (
    <TouchableOpacity
      style={[styles.button, style]}
      onPress={handlePress}
      activeOpacity={0.85}
      disabled={loading}
    >
      {loading ? (
        <ActivityIndicator size="small" color="#000" />
      ) : (
        <Text style={styles.buttonText}>▶  Abrir en Colab</Text>
      )}
    </TouchableOpacity>
  );
};

// ─── Estilos ─────────────────────────────────────────────────
const styles = StyleSheet.create({
  // Boton normal
  button: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.sm + 2,
    borderRadius: radius.md,
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'row',
    gap: spacing.xs,
    // Sombra en Android
    elevation: 4,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.4,
    shadowRadius: 8,
    minWidth: 160,
  },
  buttonText: {
    color: '#000',
    fontSize: fontSize.md,
    fontWeight: fontWeight.bold,
    letterSpacing: 0.5,
  },

  // Boton compacto (solo icono)
  compactButton: {
    backgroundColor: colors.accent,
    width: 44,
    height: 44,
    borderRadius: radius.full,
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 4,
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.4,
    shadowRadius: 6,
  },
  compactIcon: {
    color: '#000',
    fontSize: fontSize.md,
    fontWeight: fontWeight.bold,
  },
});

export default ColabButton;
