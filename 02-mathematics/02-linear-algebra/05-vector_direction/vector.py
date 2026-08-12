import math

def describe_vector(vector):
    # calculate magnitude
    magnitude = math.sqrt(sum(x * x for x in vector))
    # calculate direction
    direction = math.degrees(math.atan2(vector[1], vector[0]))
    # return both
    return magnitude, direction
    
A = [3, 4]
print(describe_vector(A))

# NB: Vectors that are positive scalar multiples of each other point in the same direction.