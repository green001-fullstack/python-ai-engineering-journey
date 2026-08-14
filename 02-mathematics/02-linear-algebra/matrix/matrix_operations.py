A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]


def add_matrices(A, B):
    if len(A) != len(B):
        raise ValueError("Matrices must have the same shape")

    for row_a, row_b in zip(A, B):
        if len(row_a) != len(row_b):
            raise ValueError("Matrices must have the same shape")

    result = []

    for row_a, row_b in zip(A, B):
        row = []

        for x, y in zip(row_a, row_b):
            row.append(x + y)

        result.append(row)

    return result


print(add_matrices(A, B))