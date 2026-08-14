import numpy as np

python_a = np.array([2, 4, 6])
python_b = np.array([1, 3, 5])

numpy_a = [2, 4, 6]
numpy_b = [1, 3, 5]

def add_vectors(a, b):
    result = [x + y for x,y in zip(python_a,python_b)]
    return result


def subtract_vectors(a, b):
    result = [x - y for x,y in zip(python_a,python_b)]
    return result


def scale_vector(vector, scalar):
    result = [scalar * value for value in vector]
    return result


print(add_vectors(a,b))
print(subtract_vectors(a,b))
print(scale_vectors(vector,scalar))


# NumPy implementation

def add_vectors(numpy_a, numpy_b):
    result = numpy_a + numpy_b
    return result


def subtract_vectors(numpy_a, numpy_b):
    result = numpy_a - numpy_b
    return result


def scale_vector(vector, scalar):
    result = scalar * vector
    return result


print(add_vectors(numpy_a,numpy_b))
print(subtract_vectors(numpy_a,numpy_b))
print(scale_vector(numpy_a, 2))


# Mini challenge

c = [1, 2, 3]
d = [4, 5, 6]
def vector_addition(a, b):
    if len (a) != len(b):
        raise ValueError(f"Vector dimensions must match. Found{len(a)} and {len(b)}")
    return [x+y for x,y in zip(a, b)]

try:
    result = vector_addition(c, d)
    print("Success", result)
except ValueError as e:
    print("Error: ", e)
