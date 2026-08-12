import math


def magnitude(vector):
    return math.sqrt(sum(x * x for x in vector))


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions must match: {len(a)} != {len(b)}"
        )

    return sum(x * y for x, y in zip(a, b))


def cosine_similarity(a, b):
    dot = dot_product(a, b)

    magnitude_a = magnitude(a)
    magnitude_b = magnitude(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "Cosine similarity is undefined for a zero vector."
        )

    return dot / (magnitude_a * magnitude_b)