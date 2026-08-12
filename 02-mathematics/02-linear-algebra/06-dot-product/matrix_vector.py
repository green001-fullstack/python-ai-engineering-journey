import numpy as np

applicants = np.array([
    [30, 5, 2, 85],
    [25, 3, 1, 71],
    [40, 8, 4, 90]
])

weights = np.array([0.1, 0.5, -0.3, 0.8])

# applicants is a 2D array (matrix) and weights is a 1D array (vector)
score = np.dot(applicants, weights)

print(score)