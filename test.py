from repetition import check_threefold_repetition

sequences_with_repetition = [
    "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O h3",
    # Add your other sequences here...
]

sequences_without_repetition = [
    "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 Re1 b5 Bb3 d6 c3 O-O",
    # Add your other sequences here...
]

def evaluate_system(sequences_with_rep, sequences_without_rep, detection_func):
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for sequence in sequences_with_rep:
        if detection_func(sequence):
            true_positives += 1
        else:
            false_negatives += 1

    for sequence in sequences_without_rep:
        if detection_func(sequence):
            false_positives += 1

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1_score

precision, recall, f1_score = evaluate_system(sequences_with_repetition, sequences_without_repetition, check_threefold_repetition)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)
