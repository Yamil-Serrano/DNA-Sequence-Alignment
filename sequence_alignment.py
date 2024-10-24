import csv

# Global variable for gap penalty, used in sequence alignment scoring
gap_penalty = -2

#------------------------------------------------------- Initializing the Scores Matrix ----------------------------------------------------------
def score_matrix_generator(sec1, sec2):
    """
    Generates and initializes the scoring matrix for two sequences (sec1 and sec2) to be aligned.
    
    The matrix is initialized with dimensions (len(sec2)+1) x (len(sec1)+1), where each cell represents 
    the alignment score between substrings of sec1 and sec2 up to that position.
    
    The first row and column are filled with multiples of the gap penalty to account for gaps at the 
    beginning of either sequence.

    Args:
    sec1 (str): The first sequence to be aligned.
    sec2 (str): The second sequence to be aligned.

    Returns:
    list: A 2D list (matrix) initialized with gap penalties in the first row and column.
    """
    # Create a matrix of size (len(sec2)+1) x (len(sec1)+1) initialized to zero
    score_matrix = [[0 for _ in range(len(sec1) + 1)] for _ in range(len(sec2) + 1)]

    # Initialize first column (representing gaps in sec1)
    for i in range(1, len(sec2) + 1):
        score_matrix[i][0] = i * gap_penalty
    
    # Initialize first row (representing gaps in sec2)
    for j in range(1, len(sec1) + 1):
        score_matrix[0][j] = j * gap_penalty
    
    return score_matrix

#----------------------------------------------- Populating the Score Matrix with Alignment Scores ------------------------------------------------
def scoring_phase(matrix, sec1, sec2):
    """
    Fills the scoring matrix using dynamic programming based on match, mismatch, and gap penalties.
    
    The matrix is filled cell by cell where each cell is determined by the maximum score from 
    aligning the current characters from sec1 and sec2 (diagonal movement), inserting a gap in sec1 
    (leftward movement), or inserting a gap in sec2 (upward movement).

    Args:
    matrix (list): The initialized scoring matrix.
    sec1 (str): The first sequence.
    sec2 (str): The second sequence.

    Returns:
    list: The filled scoring matrix with optimal alignment scores.
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            letter1 = sec1[j - 1]  # Current letter from sec1
            letter2 = sec2[i - 1]  # Current letter from sec2
            
            # Scoring based on match/mismatch
            if letter1 == letter2:
                diagonal = matrix[i - 1][j - 1] + 1  # Match score (+1)
            else:
                diagonal = matrix[i - 1][j - 1] - 1  # Mismatch penalty (-1)
            
            # Score for gap in sec2 (move left) or sec1 (move up)
            left = matrix[i][j - 1] + gap_penalty
            up = matrix[i - 1][j] + gap_penalty
            
            # Choose the maximum score from diagonal, left, or up
            score = max(diagonal, left, up)
            matrix[i][j] = score
    
    return matrix

#--------------------------------------------------- Backtracking for Optimal Sequence Alignment ---------------------------------------------------
def backtrack(matrix, sec1, sec2):
    """
    Performs backtracking to determine the optimal alignment between sec1 and sec2 based on the 
    filled scoring matrix.

    Starting from the bottom-right of the matrix, the function reconstructs the optimal aligned 
    sequences by tracing the maximum scores back to the top-left.

    Args:
    matrix (list): The filled scoring matrix.
    sec1 (str): The first sequence.
    sec2 (str): The second sequence.

    Returns:
    tuple: Two aligned sequences (aligned_sec1, aligned_sec2) where gaps ('-') may be introduced.
    """
    i, j = len(sec2), len(sec1)
    aligned_sec1, aligned_sec2 = [], []

    # Trace back from the bottom-right corner of the matrix
    while i > 0 or j > 0:
        current_score = matrix[i][j]
        
        # Case: gap in sec2 (move left)
        if j > 0 and current_score == matrix[i][j - 1] + gap_penalty:
            aligned_sec1.append(sec1[j - 1])
            aligned_sec2.append('-')
            j -= 1
        
        # Case: gap in sec1 (move up)
        elif i > 0 and current_score == matrix[i - 1][j] + gap_penalty:
            aligned_sec1.append('-')
            aligned_sec2.append(sec2[i - 1])
            i -= 1
        
        # Case: match/mismatch (diagonal move)
        elif i > 0 and j > 0:
            aligned_sec1.append(sec1[j - 1])
            aligned_sec2.append(sec2[i - 1])
            i -= 1
            j -= 1

    # Reverse to get the correct alignment order
    return ''.join(reversed(aligned_sec1)), ''.join(reversed(aligned_sec2))

#-------------------------------------------------- Reading and Aligning Sequences from a CSV ------------------------------------------------------
def align_sequences_from_csv(input_file):
    """
    Reads a CSV file containing pairs of sequences, performs sequence alignment on each pair, 
    and returns the aligned sequences and their scores.

    The CSV is expected to have two columns where each row contains two sequences to be aligned. 
    The function processes each pair of sequences, generates the score matrix, performs the alignment, 
    and stores the results including the alignment score.

    Args:
    input_file (str): The path to the input CSV file.

    Returns:
    list: A list of formatted strings containing the aligned sequences and their alignment scores.
    """
    results = []
    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row if present

            # Process each pair of sequences in the CSV
            for row in reader:
                if len(row) != 2:
                    continue  # Skip invalid rows
                
                sec1, sec2 = row  # Extract sequences
                score_matrix = score_matrix_generator(sec1, sec2)  # Initialize matrix
                filled_matrix = scoring_phase(score_matrix, sec1, sec2)  # Fill matrix with scores
                aligned_sec1, aligned_sec2 = backtrack(filled_matrix, sec1, sec2)  # Perform backtracking
                
                # Retrieve the final score (bottom-right of matrix)
                score = filled_matrix[-1][-1]
                
                # Store the result with alignment and score
                results.append(f"-----------------------------------\n{aligned_sec1} {aligned_sec2} Score: {score}")

    except Exception as e:
        # Handle errors such as file not found or read errors
        results.append(f"Error processing file: {e}")
    
    return results
