import math
import numpy as np

def vector_magnitude(vector):
    square = [x * x  for x in vector]
    result = math.sqrt(sum(square))
    return result 

vector = [6, 8]
print(vector_magnitude(vector))

# Numpy implementation

numpy_vector = np.array([6, 8])

def vector_magnitude(vector):
    result = np.linalg.norm(vector)
    return result

print(vector_magnitude(numpy_vector))