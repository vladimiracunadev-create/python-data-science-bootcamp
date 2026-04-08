import React, { useEffect, useState } from "react";
import {
  Alert,
  Linking,
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";

import DiagnosticQuiz from "../components/DiagnosticQuiz";
import CodeBlock from "../components/CodeBlock";
import { isClassCompleted, removeProgress, saveProgress } from "../utils/progress";

const colors = {
  bg: "#0f0f1a",
  bgCard: "#1a1a2e",
  bgMuted: "#0f172a",
  accent: "#22c55e",
  accentBlue: "#3b82f6",
  text: "#f1f5f9",
  textMuted: "#94a3b8",
  border: "#334155",
};

const LEVEL_COLORS = {
  Diagnostico: "#38bdf8",
  Basico: "#22c55e",
  Intermedio: "#f59e0b",
  "Intermedio-Avanzado": "#8b5cf6",
  Avanzado: "#ef4444",
  Integrador: "#f59e0b",
};

export default function ClassScreen({ route }) {
  const { classData } = route.params;
  const hasQuiz = Boolean(classData.quiz?.questions?.length);
  const hasColab = Boolean(classData.colabUrl);

  const [activeTab, setActiveTab] = useState(hasQuiz ? "quiz" : "theory");
  const [completed, setCompleted] = useState(false);

  useEffect(() => {
    setActiveTab(hasQuiz ? "quiz" : "theory");
  }, [classData.id, hasQuiz]);

  useEffect(() => {
    isClassCompleted(classData.id).then(setCompleted);
  }, [classData.id]);

  const handleOpenColab = async () => {
    if (!classData.colabUrl) {
      return;
    }

    const canOpen = await Linking.canOpenURL(classData.colabUrl);
    if (canOpen) {
      await Linking.openURL(classData.colabUrl);
      return;
    }

    Alert.alert(
      "No se pudo abrir Colab",
      "Verifica que tengas conexion a internet y un navegador disponible.",
      [{ text: "OK" }]
    );
  };

  const handleToggleCompleted = async () => {
    if (completed) {
      await removeProgress(classData.id);
      setCompleted(false);
      return;
    }

    await saveProgress(classData.id);
    setCompleted(true);
  };

  const TheoryTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Enfoque del modulo</Text>
        <Text style={styles.cardText}>{classData.theory}</Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Resultados esperados</Text>
        {classData.outcomes.map((item) => (
          <View key={item} style={styles.rowItem}>
            <View style={styles.bullet} />
            <Text style={styles.rowText}>{item}</Text>
          </View>
        ))}
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Temas de esta clase</Text>
        {classData.topics.map((item) => (
          <View key={item} style={styles.rowItem}>
            <View style={[styles.bullet, styles.bulletBlue]} />
            <Text style={styles.rowText}>{item}</Text>
          </View>
        ))}
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Materiales del modulo</Text>
        <View style={styles.materialsWrap}>
          {classData.materials.map((item) => (
            <View key={item} style={styles.materialChip}>
              <Text style={styles.materialChipText}>{item}</Text>
            </View>
          ))}
        </View>
      </View>

      <Text style={styles.sectionTitle}>Bloques de codigo documentados</Text>
      {classData.codeExamples.length > 0 ? (
        classData.codeExamples.map((example) => (
          <View key={example.id} style={styles.exampleCard}>
            <Text style={styles.exampleTitle}>{example.title}</Text>
            <Text style={styles.exampleExplanation}>{example.explanation}</Text>
            <View style={styles.schemaBox}>
              <Text style={styles.schemaText}>{example.schema}</Text>
            </View>
            <CodeBlock
              code={example.code}
              language={example.language ?? "python"}
              title={example.title}
            />
          </View>
        ))
      ) : (
        <View style={styles.card}>
          <Text style={styles.cardText}>
            Este modulo pone el foco en lectura, diagnostico o planificacion. Revisa la teoria y el
            diagnostico para interpretar el contenido.
          </Text>
        </View>
      )}

      <View style={styles.bottomSpacer} />
    </ScrollView>
  );

  const ExercisesTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Como practicar</Text>
        <Text style={styles.cardText}>
          Lee la pregunta del modulo, ejecuta o revisa el bloque principal y deja comentarios breves
          sobre que hace cada paso y para que sirve.
        </Text>
      </View>

      {classData.codeExamples.length > 0 ? (
        classData.codeExamples.map((example, index) => (
          <View key={example.id} style={styles.exerciseCard}>
            <Text style={styles.exerciseNumber}>Ejercicio {index + 1}</Text>
            <Text style={styles.exampleTitle}>{example.title}</Text>
            <Text style={styles.exampleExplanation}>{example.explanation}</Text>
            <View style={styles.schemaBox}>
              <Text style={styles.schemaText}>{example.schema}</Text>
            </View>
            <CodeBlock code={example.code} language={example.language ?? "python"} />
          </View>
        ))
      ) : (
        <View style={styles.card}>
          <Text style={styles.cardText}>
            En esta clase la practica principal esta en el tab Diagnostico. Responde todo el quiz y
            revisa por pregunta donde acertaste y donde necesitas refuerzo.
          </Text>
        </View>
      )}

      <View style={styles.bottomSpacer} />
    </ScrollView>
  );

  const QuizTab = () => (
    <ScrollView style={styles.tabContent} showsVerticalScrollIndicator={false}>
      <DiagnosticQuiz quiz={classData.quiz} />
    </ScrollView>
  );

  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.headerCard}>
        <View style={styles.headerRow}>
          <View style={styles.numberBadge}>
            <Text style={styles.numberBadgeText}>{classData.number}</Text>
          </View>

          <View style={styles.headerTextBlock}>
            <Text style={styles.title}>{classData.title}</Text>
            <Text style={styles.description}>{classData.description}</Text>
            <View style={styles.badgesRow}>
              <View
                style={[
                  styles.levelBadge,
                  { backgroundColor: LEVEL_COLORS[classData.level] ?? colors.accent },
                ]}
              >
                <Text style={styles.levelBadgeText}>{classData.level}</Text>
              </View>
              <View style={styles.durationBadge}>
                <Text style={styles.durationText}>{classData.duration}</Text>
              </View>
            </View>
          </View>
        </View>
      </View>

      <View style={styles.tabBar}>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === "theory" && styles.tabButtonActive]}
          onPress={() => setActiveTab("theory")}
        >
          <Text style={[styles.tabButtonText, activeTab === "theory" && styles.tabButtonTextActive]}>
            Teoria
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.tabButton, activeTab === "exercises" && styles.tabButtonActive]}
          onPress={() => setActiveTab("exercises")}
        >
          <Text
            style={[styles.tabButtonText, activeTab === "exercises" && styles.tabButtonTextActive]}
          >
            Practica
          </Text>
        </TouchableOpacity>

        {hasQuiz ? (
          <TouchableOpacity
            style={[styles.tabButton, activeTab === "quiz" && styles.tabButtonActive]}
            onPress={() => setActiveTab("quiz")}
          >
            <Text style={[styles.tabButtonText, activeTab === "quiz" && styles.tabButtonTextActive]}>
              Diagnostico
            </Text>
          </TouchableOpacity>
        ) : null}
      </View>

      <View style={styles.contentArea}>
        {activeTab === "theory" ? <TheoryTab /> : null}
        {activeTab === "exercises" ? <ExercisesTab /> : null}
        {activeTab === "quiz" && hasQuiz ? <QuizTab /> : null}
      </View>

      <View style={styles.bottomBar}>
        <TouchableOpacity
          style={[styles.completeButton, completed && styles.completeButtonDone]}
          onPress={handleToggleCompleted}
        >
          <Text style={styles.completeButtonText}>
            {completed ? "Completada" : "Marcar completada"}
          </Text>
        </TouchableOpacity>

        {hasColab ? (
          <TouchableOpacity style={styles.colabButton} onPress={handleOpenColab}>
            <Text style={styles.colabButtonText}>Abrir en Colab</Text>
          </TouchableOpacity>
        ) : null}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.bg,
  },
  headerCard: {
    backgroundColor: colors.bgCard,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
    paddingHorizontal: 16,
    paddingVertical: 14,
  },
  headerRow: {
    flexDirection: "row",
    gap: 12,
    alignItems: "flex-start",
  },
  numberBadge: {
    width: 46,
    height: 46,
    borderRadius: 23,
    backgroundColor: colors.accent,
    alignItems: "center",
    justifyContent: "center",
  },
  numberBadgeText: {
    color: "#04110a",
    fontSize: 18,
    fontWeight: "800",
  },
  headerTextBlock: {
    flex: 1,
  },
  title: {
    color: colors.text,
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 4,
  },
  description: {
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 19,
    marginBottom: 8,
  },
  badgesRow: {
    flexDirection: "row",
    gap: 8,
    flexWrap: "wrap",
  },
  levelBadge: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  levelBadgeText: {
    color: "#04110a",
    fontSize: 11,
    fontWeight: "800",
  },
  durationBadge: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    backgroundColor: colors.bgMuted,
  },
  durationText: {
    color: colors.textMuted,
    fontSize: 11,
    fontWeight: "600",
  },
  tabBar: {
    flexDirection: "row",
    backgroundColor: colors.bgCard,
    borderBottomWidth: 1,
    borderBottomColor: colors.border,
  },
  tabButton: {
    flex: 1,
    paddingVertical: 12,
    alignItems: "center",
  },
  tabButtonActive: {
    borderBottomWidth: 2,
    borderBottomColor: colors.accent,
  },
  tabButtonText: {
    color: colors.textMuted,
    fontSize: 14,
    fontWeight: "600",
  },
  tabButtonTextActive: {
    color: colors.accent,
  },
  contentArea: {
    flex: 1,
  },
  tabContent: {
    flex: 1,
    paddingHorizontal: 16,
    paddingTop: 16,
  },
  card: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
    marginBottom: 16,
  },
  cardTitle: {
    color: colors.text,
    fontSize: 15,
    fontWeight: "700",
    marginBottom: 10,
  },
  cardText: {
    color: colors.textMuted,
    fontSize: 14,
    lineHeight: 22,
  },
  rowItem: {
    flexDirection: "row",
    alignItems: "flex-start",
    gap: 10,
    marginBottom: 8,
  },
  bullet: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: colors.accent,
    marginTop: 6,
  },
  bulletBlue: {
    backgroundColor: colors.accentBlue,
  },
  rowText: {
    flex: 1,
    color: colors.textMuted,
    lineHeight: 21,
  },
  materialsWrap: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 8,
  },
  materialChip: {
    backgroundColor: colors.bgMuted,
    borderRadius: 999,
    borderWidth: 1,
    borderColor: colors.border,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  materialChipText: {
    color: colors.text,
    fontSize: 12,
  },
  sectionTitle: {
    color: colors.text,
    fontSize: 16,
    fontWeight: "700",
    marginBottom: 12,
  },
  exampleCard: {
    marginBottom: 20,
  },
  exampleTitle: {
    color: colors.text,
    fontSize: 15,
    fontWeight: "700",
    marginBottom: 6,
  },
  exampleExplanation: {
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 20,
    marginBottom: 8,
  },
  schemaBox: {
    backgroundColor: colors.bgMuted,
    borderRadius: 8,
    borderLeftWidth: 3,
    borderLeftColor: colors.accentBlue,
    padding: 12,
    marginBottom: 10,
  },
  schemaText: {
    color: "#93c5fd",
    fontFamily: "monospace",
    fontSize: 11,
    lineHeight: 17,
  },
  exerciseCard: {
    marginBottom: 24,
  },
  exerciseNumber: {
    color: colors.accentBlue,
    fontSize: 11,
    fontWeight: "700",
    marginBottom: 4,
    textTransform: "uppercase",
  },
  bottomBar: {
    flexDirection: "row",
    gap: 10,
    padding: 12,
    backgroundColor: colors.bgCard,
    borderTopWidth: 1,
    borderTopColor: colors.border,
  },
  completeButton: {
    flex: 1,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: colors.bgMuted,
    paddingVertical: 13,
    alignItems: "center",
  },
  completeButtonDone: {
    backgroundColor: "#0b1d12",
    borderColor: colors.accent,
  },
  completeButtonText: {
    color: colors.text,
    fontWeight: "700",
  },
  colabButton: {
    flex: 1,
    borderRadius: 10,
    backgroundColor: colors.accent,
    paddingVertical: 13,
    alignItems: "center",
  },
  colabButtonText: {
    color: "#04110a",
    fontWeight: "800",
  },
  bottomSpacer: {
    height: 96,
  },
});
