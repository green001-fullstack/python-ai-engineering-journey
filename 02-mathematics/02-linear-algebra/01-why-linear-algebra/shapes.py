def describe_shape(data):
    # your implementation
    return len(data), len(data[0])

data = [
    [1, 2, 3],
    [4, 5, 6]
]
print(describe_shape(data))