matrix = [
    [1, 1, 1, 6],
    [2, 3, 1, 10],
    [1, 2, 3, 13]
]


def subtract_multiple(target_row, pivot_row, factor):
    for i in range(len(target_row)):
        target_row[i] -= factor * pivot_row[i]


def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


for col in range(len(matrix)):

    pivot = matrix[col][col]

    # If pivot is zero, search for a non-zero value below it
    if pivot == 0:
        for row in range(col + 1, len(matrix)):

            if matrix[row][col] != 0:
                swap_rows(matrix, col, row)
                pivot = matrix[col][col]
                break

    # If we still don't have a pivot, move to the next column
    if pivot == 0:
        continue

    # Eliminate values below the pivot
    for row in range(col + 1, len(matrix)):

        target = matrix[row][col]
        factor = target / pivot

        subtract_multiple(matrix[row], matrix[col], factor)


print(matrix)