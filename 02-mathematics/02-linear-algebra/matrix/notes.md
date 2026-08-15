# 📘 Linear Algebra — Matrix Structures

## 4. Matrix Structures

This section covers important special types of matrices and fundamental properties of matrix operations.

---

## 4.1 Identity Matrix

The identity matrix is a **square matrix** whose main diagonal contains 1s and every other element is 0.

For a 3 × 3 matrix:

```
I = [1  0  0]
    [0  1  0]
    [0  0  1]
```

It is the matrix equivalent of the scalar number **1**.

```
IA = AI = A
```

For a vector:

```
Ix = x
```

The identity matrix leaves the vector unchanged.

### Important relationship

The identity matrix is a special **diagonal matrix** whose diagonal elements are all 1.

---

## 4.2 Diagonal Matrix

A diagonal matrix is a square matrix in which every element **outside** the main diagonal is zero.

```
D = [2  0  0]
    [0  3  0]
    [0  0  4]
```

### Why does it exist?

It provides a simple way to **scale different coordinates independently**.

For:

```
D = [2  0]        v = [3]
    [0  5]            [4]
```

we get:

```
Dv = [6]
     [20]
```

So the x-coordinate is scaled by 2 and the y-coordinate by 5.

### Scalar matrix

A diagonal matrix whose diagonal entries are all equal is a **scalar matrix**:

```
3I = [3  0  0]
     [0  3  0]
     [0  0  3]
```

### Python

```python
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
```

### NumPy

```python
import numpy as np

D = np.diag([2, 3, 4])
```

---

## 4.3 Symmetric Matrix

A square matrix is **symmetric** if its transpose equals itself:

```
Aᵀ = A
```

Example:

```
A = [1  2  3]
    [2  5  6]
    [3  6  9]
```

Its elements satisfy:

```
Aᵢⱼ = Aⱼᵢ
```

For example: `A₁,₃ = A₃,₁`.

> A symmetric matrix must be square.

### Relationship with diagonal matrices

Every diagonal matrix is symmetric, but **not every symmetric matrix is diagonal**.

Example of symmetric but non-diagonal:

```
[1  2]
[2  5]
```

### Why it matters

Symmetric matrices occur in important AI/ML concepts such as:

- covariance matrices
- PCA
- eigenvalues and eigenvectors
- optimization

### Python

```python
def is_symmetric(matrix):
    rows = len(matrix)

    if any(len(row) != rows for row in matrix):
        return False

    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True
```

---

## 4.4 Matrix Properties

### Associative Property

Matrix multiplication is associative:

```
(AB)C = A(BC)
```

> The grouping can change, but the order cannot.

### Commutative Property of Addition

Matrix addition is commutative:

```
A + B = B + A
```

### Matrix Multiplication Is Not Generally Commutative

In general:

```
AB ≠ BA
```

Unlike ordinary numbers, matrix multiplication depends on the **order** of the matrices. The inner dimensions must also match.

For example:

```
(2,3)(3,4) = (2,4)   → valid
(3,4)(2,3)            → NOT valid (4 ≠ 2)
```

### Distributive Property

Matrix multiplication distributes over addition:

```
A(B + C) = AB + AC
(A + B)C = AC + BC
```

### Zero Matrix

The zero matrix contains only zeros.

For compatible matrices:

```
A + 0 = A
A0 = 0
0A = 0
```

### Identity Matrix as Multiplicative Identity

```
AI = IA = A
```

This is analogous to `1x = x`.

### Transpose of a Sum

```
(A + B)ᵀ = Aᵀ + Bᵀ
```

### Transpose of a Product

One of the most important properties:

```
(AB)ᵀ = BᵀAᵀ
```

> The order **reverses**. It is **not** `AᵀBᵀ`.

### Transpose Twice

```
(Aᵀ)ᵀ = A
```

---

## 4.5 Dot Product as Matrix Multiplication

For vectors:

```
a = [a₁]        b = [b₁]
    [a₂]            [b₂]
    [a₃]            [b₃]
```

the dot product is:

```
a · b = a₁b₁ + a₂b₂ + a₃b₃
```

Using matrix notation:

```
a · b = aᵀb
```

This connects the earlier vector lessons directly to matrix notation.

---

## 4.6 Matrix-Vector Multiplication

Matrix-vector multiplication is essentially a collection of dot products.

For:

```
A = [1  2  3]        x = [10]
    [4  5  6]             [20]
                          [30]
```

each row of `A` takes a dot product with `x`.

```
Matrix-vector multiplication = multiple dot products
```

---

## 4.7 The Expression AᵀA

If `A` has shape `(3, 2)`, then `Aᵀ` has shape `(2, 3)`.

Therefore:

```
AᵀA
```

has shape:

```
(2,3)(3,2) = (2,2)
```

The expression `AᵀA` will appear later in:

- least squares
- linear regression
- optimization
- covariance-related calculations
- machine learning

---

## 4.8 Summary

| Type / Property | Definition |
|---|---|
| Identity | Diagonal entries are 1; everything else is 0 |
| Diagonal | Everything outside the main diagonal is 0 |
| Symmetric | `Aᵀ = A` |
| Zero matrix | Every element is 0 |
| Addition | `A + B = B + A` |
| Multiplication associative | `(AB)C = A(BC)` |
| Multiplication generally not commutative | `AB ≠ BA` |
| Distributive | `A(B + C) = AB + AC` |
| Identity | `AI = IA = A` |
| Transpose twice | `(Aᵀ)ᵀ = A` |
| Transpose of sum | `(A + B)ᵀ = Aᵀ + Bᵀ` |
| Transpose of product | `(AB)ᵀ = BᵀAᵀ` |
| Dot product | `a · b = aᵀb` |

---

## 4.9 Key Ideas to Remember

- **Identity matrix** behaves like `1`.
- **Zero matrix** behaves like `0` for addition and annihilates compatible matrix products.
- **Diagonal matrices** independently scale coordinate directions.
- **Symmetric matrices** satisfy `Aᵀ = A`.
- Matrix **addition** is commutative.
- Matrix **multiplication** is associative but generally **not** commutative.
- Matrix multiplication is based on **row-column dot products**.
- Transposing a product **reverses the order**: `(AB)ᵀ = BᵀAᵀ`.
- A vector dot product can be written as `aᵀb`.
- `AᵀA` will become important later in machine learning.

---

## 4.10 Roadmap

**Completed:**

```
4. MATRIX STRUCTURES
├── Identity matrix                  ✅
├── Diagonal matrix                  ✅
├── Symmetric matrix                 ✅
└── Matrix properties                ✅
```

**Next:**

```
5. LINEAR EQUATIONS
├── What makes an equation linear?
├── Solving linear equations
├── Linear functions
├── Slope
├── Intercepts
├── Lines in 2D
├── Systems of equations
├── Matrix representation
└── Ax = b
```

The goal is to build the bridge:

```
Matrices
   ↓
Linear Equations
   ↓
Systems
   ↓
Ax = b
   ↓
Row Reduction
   ↓
Rank / Null Space
   ↓
Vector Spaces
   ↓
Linear Transformations
   ↓
Projection
```

This sequence will let us **understand the concepts** rather than memorize formulas.