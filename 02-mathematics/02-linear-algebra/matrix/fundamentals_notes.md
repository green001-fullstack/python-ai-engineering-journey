# 📘 Linear Algebra Notes — Matrices

## 3. What Is a Matrix?

A matrix is a **rectangular arrangement of numbers** organized into rows and columns.

For example:

```
A = [1  2  3]
    [4  5  6]
```

This matrix has:

- 2 rows
- 3 columns
- Shape: `(2, 3)`

A matrix can represent many things in computing and AI, including:

- datasets
- images
- transformations
- neural-network weights
- feature representations
- mathematical systems

---

## 3.1 Matrix Representation

A matrix is commonly represented using:

```
A = [aᵢⱼ]
```

where:

- `i` represents the row
- `j` represents the column

For example:

```
A = [10  20  30]
    [40  50  60]
    [70  80  90]
```

Then:

```
A₁,₁ = 10
A₂,₃ = 60
A₃,₂ = 80
```

### Python representation

```python
A = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Each **inner list represents a row**.

---

## 3.2 Matrix Shape

The shape tells us:

```
rows × columns
```

For:

```python
A = [
    [1, 2, 3],
    [4, 5, 6]
]
```

we have shape `(2, 3)`, meaning:

- 2 rows
- 3 columns

### Important rule

Always remember the order is:

```
(rows, columns)
```

not the other way around.

### NumPy

```python
A.shape
```

returns:

```
(2, 3)
```

---

## 3.3 Matrix Indexing

Indexing allows us to access individual elements.

Mathematically, `Aᵢⱼ` means: **element at row i, column j**.

In Python, however, indexing starts from `0`.

```python
A = [
    [10, 20, 30],
    [40, 50, 60]
]

A[0][0]   # 10
A[1][2]   # 60
```

| Python | Mathematical idea |
|---|---|
| `A[0][0]` | row 1, column 1 |
| `A[1][2]` | row 2, column 3 |

---

## 3.4 Matrix Addition

### Why does it exist?

Sometimes we have two matrices representing the same type of information and want to combine corresponding elements. Matrix addition is performed **element by element**.

Given:

```
A = [1  2]        B = [5  6]
    [3  4]            [7  8]
```

then:

```
A + B = [1+5  2+6]   =  [6   8]
        [3+7  4+8]      [10  12]
```

### Requirement

The matrices must have the **same shape**.

```
(2,3) + (2,3)  → valid
(2,3) + (3,2)  → NOT valid
```

### Python

```python
def add_matrices(A, B):
    if len(A) != len(B):
        raise ValueError("Matrices must have the same shape")

    result = []

    for row_a, row_b in zip(A, B):
        if len(row_a) != len(row_b):
            raise ValueError("Matrices must have the same shape")

        result.append([
            x + y
            for x, y in zip(row_a, row_b)
        ])

    return result
```

### NumPy

```python
A + B
```

NumPy performs the element-wise addition for us.

---

## 3.5 Matrix Subtraction

Matrix subtraction works exactly like addition.

Given:

```
A = [10  20]        B = [1  2]
    [30  40]             [3  4]
```

then:

```
A - B = [9   18]
        [27  36]
```

Again: **same shape required**.

### Python

```python
def subtract_matrices(A, B):
    if len(A) != len(B):
        raise ValueError("Matrices must have the same shape")

    result = []

    for row_a, row_b in zip(A, B):

        if len(row_a) != len(row_b):
            raise ValueError("Matrices must have the same shape")

        result.append([
            x - y
            for x, y in zip(row_a, row_b)
        ])

    return result
```

### NumPy

```python
A - B
```

---

## 3.6 Scalar Multiplication

### What is a scalar?

A scalar is a single number, e.g. `2, 5, -3, 0.5`.

Scalar multiplication means **multiplying every element** of a matrix by that number.

Given:

```
A = [1  2]
    [3  4]
```

and scalar `3`:

```
3A = [3   6]
     [9  12]
```

### Python

```python
def scale_matrix(matrix, scalar):

    result = []

    for row in matrix:
        result.append([
            scalar * value
            for value in row
        ])

    return result
```

### NumPy

```python
3 * A
```

This is one of the reasons NumPy arrays are so useful for numerical computing: the operation naturally applies to the entire array.

---

## 3.7 Matrix–Vector Multiplication

This is an important step because it introduces the deeper meaning of matrix multiplication.

Suppose:

```
A = [1  2  3]        x = [10]
    [4  5  6]             [20]
                          [30]
```

The matrix has shape `(2, 3)`. The vector has 3 elements.

Therefore multiplication is valid:

```
(2,3)(3,1) = (2,1)
```

The result is another vector:

```
Ax = [1(10) + 2(20) + 3(30)]   =  [140]
     [4(10) + 5(20) + 6(30)]      [320]
```

### The key intuition

> Each row of the matrix performs a dot product with the vector.

```
Matrix row
    ↓
[1, 2, 3]
    ↓
dot product
    ↓
[10, 20, 30]
    ↓
140
```

Then the next row does the same thing.

```
Matrix-vector multiplication = multiple dot products
```

### Python

```python
def matrix_vector_multiply(A, x):

    if len(A[0]) != len(x):
        raise ValueError(
            "Matrix columns must match vector length"
        )

    result = []

    for row in A:
        result.append(
            sum(a * b for a, b in zip(row, x))
        )

    return result
```

### NumPy

```python
A @ x
```

The `@` operator means matrix multiplication in Python.

---

## 3.8 Matrix Multiplication

This is one of the most important operations in linear algebra.

Given:

```
A → shape (m, n)
B → shape (n, p)
```

the result has shape:

```
(m, p)
```

The **inner dimensions must match**:

```
(m, n)(n, p)
```

For example:

```
(2,3)(3,4)  → valid, produces (2,4)
(2,3)(2,4)  → invalid because 3 ≠ 2
```

### How is multiplication performed?

Consider:

```
A = [1  2]        B = [5  6]
    [3  4]             [7  8]
```

Each element of the result is:

```
row of A · column of B
```

For example:

```
C₁,₁ = [1, 2] · [5, 7] = 1(5) + 2(7) = 19
```

So:

```
AB = [19  22]
     [43  50]
```

### Fundamental idea

```
Cᵢⱼ = rowᵢ(A) · columnⱼ(B)
```

This connects directly to the dot product learned earlier.

---

## 3.9 Matrix Transpose

Transpose means:

> Rows become columns and columns become rows.

It is represented by `Aᵀ`.

Given:

```
A = [1  2  3]
    [4  5  6]
```

then:

```
Aᵀ = [1  4]
     [2  5]
     [3  6]
```

The shape changes:

```
(m, n) → (n, m)
(2, 3) → (3, 2)
```

### Element-level definition

Transpose swaps the indices:

```
(Aᵀ)ᵢⱼ = Aⱼᵢ
```

So `A₂,₃` moves to `(Aᵀ)₃,₂`.

### Transpose twice

One of the fundamental properties:

```
(Aᵀ)ᵀ = A
```

Transpose once → rows become columns. Transpose again → they return to their original positions.

### Python — straightforward implementation

```python
def transpose(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    result = []

    for j in range(columns):

        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result
```

### A more Pythonic version

```python
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
```

`zip(*matrix)` groups elements by their positions, effectively turning columns into rows.

### OOP version

In a `Matrix` class:

```python
def transpose(self):

    rows, columns = self.shape

    result = []

    for j in range(columns):

        new_row = []

        for i in range(rows):
            new_row.append(self._rows[i][j])

        result.append(new_row)

    return Matrix(result)
```

Compact version:

```python
def transpose(self):
    return Matrix(
        [list(row) for row in zip(*self._rows)]
    )
```

### NumPy

```python
A.T
```

or:

```python
np.transpose(A)
```

---

## 🔗 Important Connections We've Built

This is probably the most important section of these notes — these concepts aren't isolated.

**Vector operations** taught us:

```
a · b
```

**Matrix-vector multiplication** showed that `Ax` is essentially multiple dot products.

**Matrix multiplication** extended the same idea:

```
Cᵢⱼ = rowᵢ(A) · columnⱼ(B)
```

**Transpose** gave us another way to express the dot product:

```
a · b = aᵀb
```

This is a major bridge between elementary vector operations and the matrix notation used in machine learning.

---

## 🤖 Connection to AI/ML

Remember the earlier weighted-score problem:

```python
features = [30, 5, 2, 85]
weights  = [0.1, 0.5, -0.3, 0.8]
```

You calculated:

```
0.1(30) + 0.5(5) - 0.3(2) + 0.8(85)
```

That's a dot product.

When we have many applicants:

```
X = [30  5  2  85]        w = [0.1]
    [25  3  1  71]             [0.5]
    [40  8  4  90]             [-0.3]
                                [0.8]
```

we can perform:

```
Xw
```

and obtain **one score per applicant**. That's exactly what was implemented with:

```python
np.dot(applicants, weights)
```

or equivalently:

```python
applicants @ weights
```

So the path goes: **linear algebra → data → machine learning.**

---

## 📌 Matrix Operations Cheat Sheet

| Operation | Meaning | Shape requirement |
|---|---|---|
| `A + B` | Element-wise addition | Same shape |
| `A - B` | Element-wise subtraction | Same shape |
| `cA` | Multiply every element by scalar | Any matrix |
| `Ax` | Matrix-vector multiplication | columns(A) = length(x) |
| `AB` | Matrix multiplication | columns(A) = rows(B) |
| `Aᵀ` | Swap rows and columns | Always possible |

**Matrix multiplication shape:**

```
(m, n)(n, p) = (m, p)
```

**Transpose shape:**

```
(m, n)ᵀ = (n, m)
```

---

## 🧠 The Three Rules to Remember

If you forget everything else from this chapter, remember these:

**Rule 1 — Addition/subtraction**

```
Same shape required
```

**Rule 2 — Matrix multiplication**

```
Inner dimensions must match
(m, n)(n, p)
```

**Rule 3 — Transpose**

```
Rows become columns
```