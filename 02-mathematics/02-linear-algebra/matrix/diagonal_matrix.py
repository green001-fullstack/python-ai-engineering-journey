def diagonal_matrix(values):

    size = len(values)

    result = []

    for i in range(size):

        row = []

        for j in range(size):

            if i == j:
                row.append(values[i])
            else:
                row.append(0)

        result.append(row)

    return result

values = [1, 2, 3]
print(diagonal_matrix(values))


