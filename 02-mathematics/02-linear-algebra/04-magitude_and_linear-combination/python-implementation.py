c = [1, 2, 3]
d = [4, 5, 6]

a=[2,4,6]
b=[1,3,5]

scalar_a = 2
scalar_b = 3

new_scalar_a = 4
new_scalar_b = 2

def linear_combination(a, b, new_scalar_a, new_scalar_b):
    result = [new_scalar_a * x - new_scalar_b * y for x, y in zip(a,b)]
    return result
print(linear_combination(a,b, new_scalar_a, new_scalar_b))