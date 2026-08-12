A = [3, 4]
B = [2, 1]

def dot_product(A, B):
    if len(A) != len(B):
        raise ValueError
    return sum(x * y for x,y in zip(A,B))

try:
    print(dot_product(A, B))
except ValueError:
    print(f"Length of A has to be same with B but found {len(A)} and {len(B)}")
    

# Another method

A = [1, 2, 3]
B = [4, 5]

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions must match: {len(a)} != {len(b)}"
        )

    return sum(x * y for x, y in zip(a, b))
    
print(dot_product(A,B))