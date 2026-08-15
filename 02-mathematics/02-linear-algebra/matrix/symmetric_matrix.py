def is_symmetric(matrix):

    rows = len(matrix)

    # Must be square
    if any(len(row) != rows for row in matrix):
        return False

    for i in range(rows):
        for j in range(rows):

            if matrix[i][j] != matrix[j][i]:
                return False

    return True