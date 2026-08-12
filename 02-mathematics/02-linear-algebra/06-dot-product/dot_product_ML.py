# Create the input lists
features = [30, 5, 2, 85]
weights = [0.1, 0.5, -0.3, 0.8]


def weighted_score(features, weights):
    # Bonus: Raise ValueError if dimensions do not match
    if len(features) != len(weights):
        raise ValueError(
            f"Dimension mismatch: Features has {len(features)} elements, "
            f"but weights has {len(weights)} elements."
        )

    # Calculate the dot product using a list comprehension and sum()
    return sum(f * w for f, w in zip(features, weights))


# Calculate and print the result
result = weighted_score(features, weights)
print(f"Weighted Score: {result}")
