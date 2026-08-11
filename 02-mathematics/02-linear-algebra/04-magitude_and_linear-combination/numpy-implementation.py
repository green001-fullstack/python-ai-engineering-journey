import numpy as np

numpy_c = np.array([1, 2, 3])
numpy_d = np.array([4, 5, 6])

scalar_a = 2
scalar_b = 3

numpy_a= np.array([2,4,6])
numpy_b= np.array([1,3,5])

new_scalar_a = 4
new_scalar_b = 2

def linear_combination(a, b, scalar_a, scalar_b):
    result = scalar_a * a - scalar_b * b
    return result
print(linear_combination(numpy_a,numpy_b, new_scalar_a, new_scalar_b))