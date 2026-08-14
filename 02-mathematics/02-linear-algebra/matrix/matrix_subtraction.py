A = [
    [10, 20, 30],
    [40, 50, 60]
]

B = [
    [1, 2, 3],
    [4, 5, 6]
]


def subtract_matrices(A, B):
    if len(A) != len(B):
        raise ValueError("Matrices must have the same dimension")
    for row_a, row_b in zip(A,B):
        if len(row_a) != len(row_b):
            raise ValueError("Matrices must have the same dimension")

    result = []

    for row_a, row_b in zip(A,B):
        row = [x-y for x,y in zip(row_a, row_b)]
        result.append(row)
    return result

print(subtract_matrices(A, B))