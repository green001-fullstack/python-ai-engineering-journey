A=[[1,2,3], [4,5,6]]
scalar = 2
def scale_matrix(matrix, scalar):
    result = []
    for i in matrix:
        row = [scalar * x for x in i]
        result.append(row)
    return result
print(scale_matrix(A, scalar))
