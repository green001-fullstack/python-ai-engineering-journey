

def vector_between_points(a, b):
    return [x-y for x, y in zip(b,a)]

A = [1, 2]
B = [4, 6]

print(vector_between_points(A, B))



# Distance between two points

import math

def distance_between_points(a, b):
    return [x-y for x, y in zip(b,a)]

A = [1, 2]
B = [4, 6]

vector = distance_between_points(A,B)

magnitude = math.sqrt(x*x for x in vector)

print(distance_between_points(A, B))