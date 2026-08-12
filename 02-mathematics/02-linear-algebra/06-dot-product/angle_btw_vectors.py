import math

A = [3, 4]
B = [-3, -4]

def magnitude(Vector):
    return math.sqrt(sum(x*x for x in Vector))

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions must match: {len(a)} != {len(b)}"
        )

    return sum(x * y for x, y in zip(a, b))
    
def angle_between_vectors(a, b):
    dot_prod = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Cannot calculate the angle with a zero vector.")
        
    cos_theta = dot_prod / (mag_a * mag_b)
    angle_radians = math.acos(cos_theta)
    return math.degrees(angle_radians)

# print(dot_product(A,B))
# print(magnitude(A))
# print(magnitude(B))
print(f"Angle between {A} and {B}: {angle_between_vectors(A, B):.2f}°")