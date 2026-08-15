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
    
     def __matmul__(self, other):
        # 1. Dimension Check: Columns of A must equal Rows of B
        rows_A, cols_A = self.shape
        rows_B, cols_B = other.shape
        
        if cols_A != rows_B:
            raise ValueError(
                f"Cannot multiply {rows_A}x{cols_A} matrix by {rows_B}x{cols_B} matrix. "
                f"Inner dimensions must match ({cols_A} != {rows_B})."
            )

        # 2. Perform Matrix Multiplication using dot products
        result = []
        for i in range(rows_A):
            new_row = []
            for j in range(cols_B):
                # Calculate the dot product of Row i from self and Column j from other
                dot_product = sum(self._rows[i][k] * other._rows[k][j] for k in range(cols_A))
                new_row.append(dot_product)
            result.append(new_row)

        return Matrix(result)

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

        
    @classmethod
    def diagonal(cls, values):

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

        return cls(result)





iden = Matrix.identity(3)

D = Matrix.diagonal([2, 3, 4])

A = Matrix([
    [1, 2],
    [3, 4]
])

# print(A.transpose())
print(A @ iden)
