def oblique(matrix):
    """slices a matrix into diagonals"""
    n = len(matrix)
    i = 0
    while i < n:
        print [matrix[j][i-j] for j in range(i+1)]
        i += 1

    k = 1
    while k < n:
        print [matrix[n-1-l][k + l] for l in range(n-k)]
        k += 1

def de_oblique(matrix):
    """converts an oblique matrix back into square form"""
    oblique_pointer = 0
    matrix_row = 0
    matrix_column = 0
    start_row = 0
    n = len(matrix) / 2 + 1
    output = list([['' for _ in range(n)]  for _ in range(n)])

    # Still haven't completed the matrix
    while matrix[-1] != []:
        # Reached the end go back to the beginning
        if oblique_pointer == len(matrix):
            oblique_pointer = int(start_row)

        # No item move to the next row
        if matrix[oblique_pointer] == []: 
            start_row += 1 
            oblique_pointer = int(start_row)
            continue

        # Reached the final column of the output row
        if matrix_column == n:
            matrix_row += 1
            matrix_column = 0
            # Start a new row at the first column
            oblique_pointer = int(start_row)
            continue

        output[matrix_row][matrix_column] = matrix[oblique_pointer].pop(0)
        oblique_pointer += 1
        matrix_column += 1

    return output


oblique_test = [[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13],[14,15],[16]]
oblique_test2 = [[1],[2,3],[4,5,6],[7,8],[9]]

test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
test_matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print de_oblique(oblique_test)