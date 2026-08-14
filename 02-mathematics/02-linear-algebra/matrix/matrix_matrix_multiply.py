def matrix_multiply(A, B):

    if len(A[0]) != len(B):
        raise ValueError(
            "Number of columns in A must equal number of rows in B"
        )

    result = []

    for row in A:

        result_row = []

        for j in range(len(B[0])):

            column = [B[i][j] for i in range(len(B))]

            value = sum(
                x * y
                for x, y in zip(row, column)
            )

            result_row.append(value)

        result.append(result_row)

    return result