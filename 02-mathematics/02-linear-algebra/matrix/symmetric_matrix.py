# Pure python version

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


    A = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

print(is_symmetric(A))

# Numpy version
import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
])

print(np.array_equal(A, A.T))