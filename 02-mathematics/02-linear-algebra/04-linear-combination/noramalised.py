import math

def normalize_vector(vector):
    # 1. Calculate the magnitude (square, sum, then square root)
    magnitude = math.sqrt(sum(x * x for x in vector))
    
    # Avoid DivisionByZero error if the vector is empty or [0, 0]
    if magnitude == 0:
        return vector
        
    # 2. Divide every element by the magnitude
    return [x / magnitude for x in vector]

# Test the function
vector = [3, 4]
normalized_pure = normalize_vector(vector)
print("Pure Python Normalized:", normalized_pure)
# Output: [0.6, 0.8]

# Numpy implementation

import numpy as np

def normalize_vector_np(vector):
    vec_array = np.array(vector)
    
    # 1. Calculate magnitude using NumPy's built-in tool
    magnitude = np.linalg.norm(vec_array)
    
    if magnitude == 0:
        return vec_array
        
    # 2. Divide every element by the magnitude (array broadcasting)
    return vec_array / magnitude

# Test the function
vector = [3, 4]
normalized_np = normalize_vector_np(vector)
print("NumPy Normalized:", normalized_np)
# Output: [0.6 0.8]


# Calculating the magnitude of the normalized vector [0.6, 0.8]
bonus_magnitude = math.sqrt(sum(x * x for x in normalized_pure))
print("Normalized Vector Magnitude:", bonus_magnitude)
# Output: 1.0
