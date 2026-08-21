matrix = [
    [1, 1, 1, 6],
    [2, 3, 1, 10],
    [1, 2, 3, 13]
]

matrix = [
    [1, 1, 1, 6],
    [2, 3, 1, 10],
    [1, 2, 3, 13]
]

def subtract_multiple(target_row, pivot_row, factor):
    for i in range (len(target_row)):
        target_row[i] -= factor * pivot_row[i]

# To perform R2 = R2 - 2*R1
factor = matrix[1][0] / matrix[0][0]
subtract_multiple(matrix[1], matrix[0], factor)

# Perform R3 = R3 - R1
factor = matrix[2][0] / matrix[0][0]
subtract_multiple(matrix[2], matrix[0], factor)
print(matrix)
