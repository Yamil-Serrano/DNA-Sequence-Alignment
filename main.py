import csv

def score_matrix_generator(sec1, sec2):
    # Generating the score matrix with dimensions (len(sec1) + 1) x (len(sec2) + 1)
    score_matrix = [[0 for _ in range(len(sec2) + 1)] for _ in range(len(sec1) + 1)]

    # Filling the first column with gap penalties (-2 for each gap)
    for i in range(1, len(sec1) + 1):
        score_matrix[i][0] = -i * 2

    # Filling the first row with gap penalties (-2 for each gap)
    for j in range(1, len(sec2) + 1):
        score_matrix[0][j] = -j * 2

    return score_matrix

def scoring_phase(matrix, sec1, sec2):
    # Iterate through the matrix starting from index (1, 1)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            # Current characters being compared from each sequence
            letter1 = sec1[i - 1]
            letter2 = sec2[j - 1]

            # Calculate the score for diagonal movement (match/mismatch)
            if letter1 == letter2:
                diagonal = matrix[i - 1][j - 1] + 1  # +1 for a match
            else:
                diagonal = matrix[i - 1][j - 1] - 1  # -1 for a mismatch

            # Calculate scores for left (gap in sec2) and up (gap in sec1)
            left = matrix[i][j - 1] - 2  # -2 for introducing a gap in sec2
            up = matrix[i - 1][j] - 2     # -2 for introducing a gap in sec1

            # Determine the maximum score among diagonal, left, and up
            score = max(diagonal, left, up)
            matrix[i][j] = score  # Store the calculated score in the matrix

    return matrix

def backtrack(matrix, sec1, sec2):
    i, j = len(sec1), len(sec2)  # Start from the bottom-right of the matrix
    aligned_sec1, aligned_sec2 = [], []  # Lists to hold aligned sequences

    # Backtracking through the matrix
    while i > 0 or j > 0:
        current_score = matrix[i][j]  # Current score at matrix[i][j]

        # Check if coming from diagonal
        if i > 0 and j > 0 and (current_score == matrix[i - 1][j - 1] + (1 if sec1[i - 1] == sec2[j - 1] else -1)):
            aligned_sec1.append(sec1[i - 1])
            aligned_sec2.append(sec2[j - 1])
            i -= 1
            j -= 1
        # Check if coming from left (gap in sec2)
        elif j > 0 and current_score == matrix[i][j - 1] - 2:
            aligned_sec1.append(sec1[i - 1])
            aligned_sec2.append('-')  # Indicate a gap in sec2
            j -= 1
        # Check if coming from up (gap in sec1)
        elif i > 0 and current_score == matrix[i - 1][j] - 2:
            aligned_sec1.append('-')  # Indicate a gap in sec1
            aligned_sec2.append(sec2[j - 1])
            i -= 1

    # Reverse the aligned sequences to get them in the correct order
    return ''.join(reversed(aligned_sec1)), ''.join(reversed(aligned_sec2))

def align_sequences_from_csv(input_file):
    # Read sequences from CSV file
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        results = []  # List to store results

        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that do not contain exactly two sequences
            sec1, sec2 = row  # Unpack sequences from the row

            # Generate score matrix, fill it, and backtrack to find aligned sequences
            score_matrix = score_matrix_generator(sec1, sec2)
            filled_matrix = scoring_phase(score_matrix, sec1, sec2)
            aligned_sec1, aligned_sec2 = backtrack(filled_matrix, sec1, sec2)
            score = filled_matrix[-1][-1]  # Get the final score from the matrix

            # Format the output as required and store it in results
            results.append(f"{aligned_sec1} {aligned_sec2} {score}")

    return results

# Example usage of the function to align sequences from the CSV file
output = align_sequences_from_csv('sequences.csv')
for line in output:
    print(line)
