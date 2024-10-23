import csv

gap_penalty = -2

#-------------------------------------------------------Initializing the Scores matrix----------------------------------------------------------

def score_matrix_generator(sec1, sec2):
    score_matrix = [[0 for _ in range(len(sec1) + 1)] for _ in range(len(sec2) + 1)]
    for i in range(1, len(sec2) + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(1, len(sec1) + 1):
        score_matrix[0][j] = j * gap_penalty
    return score_matrix

#-----------------------------------------------phase of populating the entire matrix with scores------------------------------------------------

def scoring_phase(matrix, sec1, sec2):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            letter1 = sec1[j - 1]
            letter2 = sec2[i - 1]
            if letter1 == letter2:
                diagonal = matrix[i - 1][j - 1] + 1
            else:
                diagonal = matrix[i - 1][j - 1] - 1
            left = matrix[i][j - 1] + gap_penalty
            up = matrix[i - 1][j] + gap_penalty
            score = max(diagonal, left, up)
            matrix[i][j] = score
    return matrix

#--------------------------------------------------------Backtracking for sequence alignment------------------------------------------------------
def backtrack(matrix, sec1, sec2):
    i, j = len(sec2), len(sec1)
    aligned_sec1, aligned_sec2 = [], []
    while i > 0 or j > 0:
        current_score = matrix[i][j]
        if j > 0 and current_score == matrix[i][j - 1] + gap_penalty:
            aligned_sec1.append(sec1[j - 1])
            aligned_sec2.append('-')
            j -= 1
        elif i > 0 and current_score == matrix[i - 1][j] + gap_penalty:
            aligned_sec1.append('-')
            aligned_sec2.append(sec2[i - 1])
            i -= 1
        elif i > 0 and j > 0:
            aligned_sec1.append(sec1[j - 1])
            aligned_sec2.append(sec2[i - 1])
            i -= 1
            j -= 1
    return ''.join(reversed(aligned_sec1)), ''.join(reversed(aligned_sec2))

#-------------------------------------------------Reading the .csv file for processing--------------------------------------------------------------

def align_sequences_from_csv(input_file):
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        results = []
        for row in reader:
            if len(row) != 2:
                continue
            sec1, sec2 = row
            score_matrix = score_matrix_generator(sec1, sec2)
            filled_matrix = scoring_phase(score_matrix, sec1, sec2)
            aligned_sec1, aligned_sec2 = backtrack(filled_matrix, sec1, sec2)
            score = filled_matrix[-1][-1]
            results.append(f"--------------------------\n{aligned_sec1} {aligned_sec2} {score}")
    return results

output = align_sequences_from_csv('sequences.csv')
for line in output:
    print(line)
