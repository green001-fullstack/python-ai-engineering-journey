# PURE PYTHON IMPLEMENTATION OF IDENTITY MATRIX 
def identity_matrix(size):
    result = []

    for i in range(size):
        row = []

        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        result.append(row)

    return result

    # OOP IMPLEMENTATION OF IDENTITY MATRIX

    def identity_matrix(size):
    result = []

    for i in range(size):
        row = []

        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        result.append(row)

    return result

# NUMPY IMPLEMENTATION OF IDENTITY MATRIX
import numpy as np

I = np.eye(3)

print(I)