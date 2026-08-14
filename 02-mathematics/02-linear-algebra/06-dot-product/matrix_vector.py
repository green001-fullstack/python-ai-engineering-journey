import numpy as np

applicants = np.array([
    [30, 5, 2, 85],
    [25, 3, 1, 71],
    [40, 8, 4, 90]
])

weights = np.array([0.1, 0.5, -0.3, 0.8])

score = np.dot(applicants, weights)

print(score)


# Loop version

applicants = [
    [30, 5, 2, 85],
    [25, 3, 1, 71],
    [40, 8, 4, 90]
]

weights = [0.1, 0.5, -0.3, 0.8]
result = []

def vector_matrix_multiplication(applicants, weights):
    for applicant in applicants:
        result.append(sum(x * y for x, y in zip(applicant, weights)))
    return result
print(vector_matrix_multiplication(applicants, weights))

