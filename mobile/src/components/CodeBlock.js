// ============================================================
// COMPONENTE: CodeBlock
// Muestra un bloque de codigo con syntax highlighting,
// boton de copiar y scroll horizontal
// ============================================================

import React, { useState, useCallback } from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  Platform,
} from 'react-native';
import * as Clipboard from 'expo-clipboard';
import SyntaxHighlighter from 'react-native-syntax-highlighter';
import { atomOneDark } from 'react-native-syntax-highlighter';
import { colors, spacing, radius, fontSize } from '../theme';

/**
 * CodeBlock — componente de codigo con syntax highlighting.
 *
 * Props:
 *   code     {string}  - Codigo fuente a mostrar (requerido)
 *   language {string}  - Lenguaje para el highlighting (default: "python")
 *   title    {string}  - Titulo opcional sobre el bloque
 *   style    {object}  - Estilos adicionales para el contenedor
 */
const CodeBlock = ({ code, language = 'python', title, style }) => {
  // Estado para el feedback visual del boton "Copiar"
  const [copied, setCopied] = useState(false);

  /**
   * Copia el codigo al portapapeles.
   * Muestra "Copiado!" durante 2 segundos y luego vuelve a "Copiar".
   */
  const handleCopy = useCallback(async () => {
    try {
      await Clipboard.setStringAsync(code);
      setCopied(true);

      // Despues de 2 segundos, volver al estado original
      setTimeout(() => {
        setCopied(false);
      }, 2000);
    } catch (err) {
      console.warn('No se pudo copiar:', err);
    }
  }, [code]);

  return (
    <View style={[styles.container, style]}>
      {/* Barra superior: lenguaje + boton copiar */}
      <View style={styles.header}>
        <View style={styles.languageBadge}>
          {/* Indicador de punto verde (estilo terminal) */}
          <View style={styles.dot} />
          <Text style={styles.languageText}>{language}</Text>
        </View>

        {/* Boton de copiar */}
        <TouchableOpacity
          style={[styles.copyButton, copied && styles.copyButtonSuccess]}
          onPress={handleCopy}
          activeOpacity={0.7}
        >
          <Text style={[styles.copyButtonText, copied && styles.copyButtonTextSuccess]}>
            {copied ? 'Copiado' : 'Copiar'}
          </Text>
        </TouchableOpacity>
      </View>

      {/* Bloque de codigo con scroll horizontal */}
      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        style={styles.codeScroll}
        contentContainerStyle={styles.codeScrollContent}
      >
        <SyntaxHighlighter
          language={language}
          style={atomOneDark}
          customStyle={styles.syntaxHighlighter}
          fontSize={fontSize.sm}
          fontFamily={Platform.OS === 'ios' ? 'Menlo' : 'monospace'}
          highlighter="hljs"
        >
          {code}
        </SyntaxHighlighter>
      </ScrollView>
    </View>
  );
};

// ─── Estilos ─────────────────────────────────────────────────
const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.bgCode,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.border,
    overflow: 'hidden',
    marginVertical: spacing.sm,
  },

  // Barra de encabezado
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    backgroundColor: '#161b22',  // un poco mas claro que el fondo del codigo
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },

  // Badge con el nombre del lenguaje
  languageBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
  },
  dot: {
    width: 8,
    height: 8,
    borderRadius: radius.full,
    backgroundColor: colors.accent,  // punto verde
  },
  languageText: {
    color: colors.textMuted,
    fontSize: fontSize.xs,
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    letterSpacing: 0.5,
    textTransform: 'uppercase',
  },

  // Boton de copiar
  copyButton: {
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: radius.sm,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: 'transparent',
  },
  copyButtonSuccess: {
    borderColor: colors.accent,
    backgroundColor: `${colors.accent}22`,  // 22 = ~13% opacidad en hex
  },
  copyButtonText: {
    color: colors.textMuted,
    fontSize: fontSize.xs,
    fontWeight: '500',
  },
  copyButtonTextSuccess: {
    color: colors.accent,
  },

  // Area del codigo
  codeScroll: {
    minHeight: 50,
  },
  codeScrollContent: {
    minWidth: '100%',
  },
  syntaxHighlighter: {
    margin: 0,
    padding: spacing.md,
    backgroundColor: colors.bgCode,
    minWidth: '100%',
  },
});

export default CodeBlock;
