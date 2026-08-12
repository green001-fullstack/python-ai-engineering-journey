def vector_relationship(a, b):
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions must match: {len(a)} != {len(b)}"
        )

    dot = sum(x * y for x, y in zip(a, b))

    if dot > 0:
        return "acute"
    elif dot == 0:
        return "orthogonal"
    else:
        return "obtuse"