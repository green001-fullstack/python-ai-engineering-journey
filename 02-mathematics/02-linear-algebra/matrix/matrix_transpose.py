def transpose(matrix):

    result = []

    rows = len(matrix)
    columns = len(matrix[0])

    for j in range(columns):

        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result

    # List comprehension version
    transpose = [ list(row) for row in zip(*matrix)]


    # Numpy version

    import numpy as np

# Create a 3x3 matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Method 1: Using the .T attribute (most common)
transpose_T = A.T

# Method 2: Using the np.transpose() function
transpose_func = np.transpose(A)

print("Original Matrix A:")
print(A)

print("\nTransposed using A.T:")
print(transpose_T)