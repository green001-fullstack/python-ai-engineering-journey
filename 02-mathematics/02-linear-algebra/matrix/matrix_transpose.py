def transpose(matrix):

    result = []

    rows = len(matrix)
    columns = len(matrix[0])

    for j in range(columns):

        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result