import numpy as np

scalar = np.array(5)

vector = np.array([2, 4, 6])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

tensor = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("Scalar shape:", scalar.shape)
print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)
print("Tensor shape:", tensor.shape)