import React, { useState } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

const colors = {
  bgCard: "#1a1a2e",
  bgMuted: "#0f172a",
  border: "#334155",
  text: "#f1f5f9",
  textMuted: "#94a3b8",
  accent: "#22c55e",
  accentBlue: "#3b82f6",
  danger: "#ef4444",
};

function scoreQuiz(quiz, answers) {
  const byCategory = {};
  let correct = 0;

  quiz.questions.forEach((question, index) => {
    const selectedIndex = answers[index];
    const isCorrect = selectedIndex === question.correctIndex;
    if (isCorrect) {
      correct += 1;
    }

    if (!byCategory[question.category]) {
      byCategory[question.category] = { correct: 0, total: 0 };
    }
    byCategory[question.category].total += 1;
    if (isCorrect) {
      byCategory[question.category].correct += 1;
    }
  });

  return { correct, total: quiz.questions.length, byCategory };
}

export default function DiagnosticQuiz({ quiz }) {
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const result = submitted ? scoreQuiz(quiz, answers) : null;
  const answeredCount = Object.keys(answers).length;

  const handleSelect = (questionIndex, optionIndex) => {
    if (submitted) {
      return;
    }
    setAnswers((current) => ({ ...current, [questionIndex]: optionIndex }));
  };

  const handleSubmit = () => {
    if (answeredCount < quiz.questions.length) {
      return;
    }
    setSubmitted(true);
  };

  const handleReset = () => {
    setAnswers({});
    setSubmitted(false);
  };

  return (
    <View style={styles.wrapper}>
      <View style={styles.headerCard}>
        <Text style={styles.title}>{quiz.title}</Text>
        <Text style={styles.description}>{quiz.description}</Text>
        <Text style={styles.meta}>
          Duración sugerida: {quiz.duration} · Respondidas: {answeredCount}/{quiz.questions.length}
        </Text>
      </View>

      {submitted ? (
        <View style={styles.summaryCard}>
          <Text style={styles.summaryTitle}>
            Resultado: {result.correct}/{result.total} correctas
          </Text>
          {Object.entries(result.byCategory)
            .sort(([left], [right]) => left.localeCompare(right))
            .map(([category, data]) => (
              <Text key={category} style={styles.summaryRow}>
                {category}: {data.correct}/{data.total}
              </Text>
            ))}
        </View>
      ) : null}

      <View style={styles.buttonRow}>
        <TouchableOpacity
          style={[
            styles.primaryButton,
            answeredCount < quiz.questions.length && styles.buttonDisabled,
          ]}
          onPress={handleSubmit}
          disabled={answeredCount < quiz.questions.length}
        >
          <Text style={styles.primaryButtonText}>Enviar respuestas</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.secondaryButton} onPress={handleReset}>
          <Text style={styles.secondaryButtonText}>Reiniciar</Text>
        </TouchableOpacity>
      </View>

      {quiz.questions.map((question, index) => {
        const selectedIndex = answers[index];
        const selectedText = selectedIndex !== undefined ? question.options[selectedIndex] : null;

        return (
          <View key={question.id} style={styles.questionCard}>
            <View style={styles.questionHeader}>
              <Text style={styles.questionNumber}>Pregunta {index + 1}</Text>
              <Text style={styles.questionCategory}>{question.category}</Text>
            </View>

            <Text style={styles.questionPrompt}>{question.prompt}</Text>

            {question.options.map((option, optionIndex) => {
              const selected = selectedIndex === optionIndex;
              const correct = question.correctIndex === optionIndex;
              const optionStyles = [styles.option];

              if (selected) {
                optionStyles.push(styles.optionSelected);
              }
              if (submitted && correct) {
                optionStyles.push(styles.optionCorrect);
              }
              if (submitted && selected && !correct) {
                optionStyles.push(styles.optionWrong);
              }

              return (
                <TouchableOpacity
                  key={`${question.id}-${optionIndex}`}
                  style={optionStyles}
                  onPress={() => handleSelect(index, optionIndex)}
                  disabled={submitted}
                >
                  <Text style={styles.optionLabel}>{String.fromCharCode(65 + optionIndex)}.</Text>
                  <Text style={styles.optionText}>{option}</Text>
                </TouchableOpacity>
              );
            })}

            {submitted ? (
              <Text
                style={[
                  styles.feedback,
                  selectedIndex === question.correctIndex
                    ? styles.feedbackCorrect
                    : styles.feedbackWrong,
                ]}
              >
                {selectedIndex === question.correctIndex
                  ? `Correcta. ${question.explanation}`
                  : selectedIndex === undefined
                  ? `Sin responder. La correcta era: ${question.options[question.correctIndex]}. ${question.explanation}`
                  : `Marcaste: ${selectedText}. La correcta era: ${question.options[question.correctIndex]}. ${question.explanation}`}
              </Text>
            ) : (
              <Text style={styles.feedbackPending}>
                Selecciona una alternativa y envía para ver la corrección.
              </Text>
            )}
          </View>
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    gap: 16,
    paddingBottom: 100,
  },
  headerCard: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
  },
  title: {
    color: colors.text,
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 6,
  },
  description: {
    color: colors.textMuted,
    fontSize: 13,
    lineHeight: 19,
    marginBottom: 6,
  },
  meta: {
    color: colors.accentBlue,
    fontSize: 12,
    fontWeight: "600",
  },
  summaryCard: {
    backgroundColor: "#0b1d12",
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.accent,
    padding: 14,
  },
  summaryTitle: {
    color: colors.text,
    fontSize: 15,
    fontWeight: "700",
    marginBottom: 8,
  },
  summaryRow: {
    color: "#bbf7d0",
    fontSize: 13,
    marginBottom: 4,
  },
  buttonRow: {
    flexDirection: "row",
    gap: 10,
  },
  primaryButton: {
    flex: 1,
    backgroundColor: colors.accent,
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: "center",
  },
  buttonDisabled: {
    opacity: 0.45,
  },
  primaryButtonText: {
    color: "#04110a",
    fontWeight: "800",
  },
  secondaryButton: {
    flex: 1,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: colors.bgCard,
    paddingVertical: 12,
    alignItems: "center",
  },
  secondaryButtonText: {
    color: colors.text,
    fontWeight: "600",
  },
  questionCard: {
    backgroundColor: colors.bgCard,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
  },
  questionHeader: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 8,
  },
  questionNumber: {
    color: colors.textMuted,
    fontSize: 12,
    fontWeight: "700",
  },
  questionCategory: {
    color: colors.accentBlue,
    fontSize: 12,
    fontWeight: "700",
  },
  questionPrompt: {
    color: colors.text,
    fontSize: 14,
    lineHeight: 20,
    marginBottom: 12,
  },
  option: {
    flexDirection: "row",
    gap: 10,
    alignItems: "flex-start",
    borderRadius: 10,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: colors.bgMuted,
    padding: 12,
    marginBottom: 8,
  },
  optionSelected: {
    borderColor: colors.accentBlue,
  },
  optionCorrect: {
    borderColor: colors.accent,
    backgroundColor: "#0b1d12",
  },
  optionWrong: {
    borderColor: colors.danger,
    backgroundColor: "#271215",
  },
  optionLabel: {
    color: colors.textMuted,
    fontWeight: "700",
  },
  optionText: {
    flex: 1,
    color: colors.text,
    lineHeight: 20,
  },
  feedback: {
    marginTop: 4,
    fontSize: 13,
    lineHeight: 19,
  },
  feedbackCorrect: {
    color: "#bbf7d0",
  },
  feedbackWrong: {
    color: "#fecaca",
  },
  feedbackPending: {
    marginTop: 4,
    color: colors.textMuted,
    fontSize: 12,
  },
});
