# =========================
# PURE PYTHON
# =========================

# Applicant vector

applicant = [29, 700000, 1500000, 82]

print(applicant)
print(len(applicant))

print(applicant[0])
print(applicant[1])
print(applicant[2])
print(applicant[3])


# Vector addition

def add_vectors(a, b):
    result = [x + y for x, y in zip(a, b)]
    return result


a = [1, 2, 3]
b = [4, 5, 6]

print(add_vectors(a, b))


# Vector subtraction

def subtract_vectors(a, b):
    result = [x - y for x, y in zip(a, b)]
    return result


print(subtract_vectors(a, b))


# Scalar multiplication

def scale_vector(vector, scalar):
    result = [scalar * x for x in vector]
    return result


vector = [2, 4, 6]
scalar = 3

print(scale_vector(vector, scalar))


# =========================
# NUMPY
# =========================

import numpy as np


# Vector addition

def add_vectors_numpy(a, b):
    result = a + b
    return result


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(add_vectors_numpy(a, b))


# Vector subtraction

def subtract_vectors_numpy(a, b):
    result = a - b
    return result


print(subtract_vectors_numpy(a, b))


# Scalar multiplication

def scale_vector_numpy(vector, scalar):
    result = scalar * vector
    return result


vector = np.array([2, 4, 6])
scalar = 3

print(scale_vector_numpy(vector, scalar))


# Applicant NumPy vector

applicant = np.array([
    29,
    700000,
    1500000,
    82
])

print("Applicant:", applicant)
print("Shape:", applicant.shape)
print("Dimensions:", applicant.ndim)