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

# OOP

    class Matrix:

    def __init__(self, rows):

        if not rows:
            raise ValueError("Matrix cannot be empty")

        self._rows = [list(row) for row in rows]

        column_count = len(self._rows[0])

        if column_count == 0:
            raise ValueError("Matrix cannot have empty rows")

        if any(len(row) != column_count for row in self._rows):
            raise ValueError("All rows must have the same length")

    @property
    def shape(self):
        return len(self._rows), len(self._rows[0])

    def transpose(self):
        rows, columns = self.shape

        result = []

        for j in range(columns):
            new_row = []

            for i in range(rows):
                new_row.append(self._rows[i][j])
            result.append(new_row)
            
        return Matrix(result)

    def __repr__(self):
        return f"Matrix({self._rows})"
    
    @classmethod
    def identity(cls, size):

        result = []

        for i in range(size):

            row = []

            for j in range(size):

                if i == j:
                    row.append(1)
                else:
                    row.append(0)

            result.append(row)

        return cls(result)


A = Matrix([
    [10, 20, 30],
    [40, 50, 60]
])

print(A)
print(A.transpose())
print(Matrix.identity(3))
