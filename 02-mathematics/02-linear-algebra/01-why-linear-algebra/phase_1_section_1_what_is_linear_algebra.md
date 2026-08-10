# Linear Algebra for AI — Section 1 Notes

## 1. What Is Linear Algebra?

Linear algebra is the branch of mathematics that studies mathematical objects such as scalars, vectors, and matrices, and the relationships and transformations between them.

A useful mental model:

> Linear algebra gives us a mathematical language for representing and manipulating numerical data and relationships.

Linear algebra is especially important in AI because machine-learning systems work heavily with numerical representations.

## 2. Why Linear Algebra Matters for AI

AI systems work with numerical data. Examples include:

- Images
- Text representations
- Financial data
- Audio
- Sensor data
- Neural-network parameters

Linear algebra gives us tools to represent and manipulate these quantities.

For example, an applicant might be represented using numerical features:

$$
x = \begin{bmatrix} 29 \\ 700000 \\ 1500000 \\ 200000 \\ 42 \end{bmatrix}
$$

This is a **vector**.

A collection of many applicants can be represented as a **matrix**:

$$
X = \begin{bmatrix}
29 & 700000 & 1500000 & 200000 & 42 \\
35 & 450000 & 900000 & 150000 & 31 \\
24 & 300000 & 300000 & 50000 & 18
\end{bmatrix}
$$

This allows machine-learning algorithms to operate on many observations and features mathematically.

## 3. The Four Important Levels

A useful hierarchy:

```
Scalar
   ↓
Vector
   ↓
Matrix
   ↓
Tensor
```

**Scalar** — a single numerical quantity.
$$5$$

**Vector** — an ordered collection of numbers.
$$\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$$

**Matrix** — a rectangular arrangement of numbers organized into rows and columns.
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$

**Tensor** — a generalization of scalars, vectors, and matrices to higher dimensions.

- Scalar → 0-dimensional
- Vector → 1-dimensional
- Matrix → 2-dimensional
- Tensor → potentially higher-dimensional

Images, batches of images, and neural-network data are commonly represented using tensors.

## 4. Dimensions and Shape

Shape describes the size of an object along each dimension.

For the matrix:

$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$

the shape is $2 \times 3$, because it contains 2 rows and 3 columns.

In NumPy:

```python
matrix.shape
```

would return:

```python
(2, 3)
```

## 5. Machine-Learning Dataset Shape

Suppose a dataset contains:

- 50,000 applicants
- 20 features per applicant

The feature matrix has shape $50000 \times 20$, or in NumPy:

```python
X.shape
```

would produce:

```python
(50000, 20)
```

This means: 50,000 observations, 20 features.

## 6. Pure Python Representation

Python lists can represent mathematical structures.

```python
scalar = 5

vector = [2, 4, 6]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

tensor = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
```

However, Python does not automatically understand these nested lists as mathematical vectors, matrices, or tensors. They are fundamentally Python lists.

## 7. NumPy Representation

NumPy provides numerical arrays designed for mathematical computation.

```python
import numpy as np

scalar = np.array(5)

vector = np.array([2, 4, 6])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

tensor = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Their shapes are:

- Scalar → `()`
- Vector → `(3,)`
- Matrix → `(2, 3)`
- Tensor → `(2, 2, 2)`

## 8. Mathematical Object vs Programming Representation

A very important distinction:

- A Python list is **not automatically** a mathematical vector.
- A Python list **can be used to represent** a vector.
- Similarly, a list of lists can represent a matrix.

The mathematical object has mathematical rules and operations. The programming representation is simply how we store it in code.

NumPy gives us structures that are much more appropriate for numerical computation.

## 9. AI Connection

A simplified AI pipeline can be viewed as:

```
Real-world data
      ↓
Numerical representation
      ↓
Vectors / Matrices / Tensors
      ↓
Mathematical operations
      ↓
Machine-learning model
      ↓
Prediction
```

For Atlas:

```
Financial evidence
      ↓
Numerical features
      ↓
Feature vector
      ↓
Feature matrix
      ↓
Machine-learning model
      ↓
Trust assessment
```

For computer vision:

```
Image
  ↓
Pixel values
  ↓
Tensor
  ↓
Neural network
  ↓
Prediction
```

## 10. Neural Network Connection

A simplified neural-network layer can be represented as:

$$y = Wx + b$$

where:

- $x$ = input vector
- $W$ = weight matrix
- $b$ = bias vector
- $y$ = output vector

This is one of the fundamental reasons linear algebra is essential for deep learning.

Multiple layers perform transformations such as:

$$h_1 = W_1x + b_1$$
$$h_2 = W_2h_1 + b_2$$

and eventually produce an output.

## 11. Pure Python Shape Exercise

A simple function for determining the shape of a rectangular 2D list:

```python
def describe_shape(data):
    return len(data), len(data[0])
```

Example:

```python
data = [
    [1, 2, 3],
    [4, 5, 6]
]

print(describe_shape(data))
```

Output:

```python
(2, 3)
```

The function works because:

- `len(data)` returns the number of rows.
- `len(data[0])` returns the number of elements in the first row.

## 12. Limitations of the Simple Implementation

```python
def describe_shape(data):
    return len(data), len(data[0])
```

**Limitations:**

- For an empty list `data = []`, accessing `data[0]` raises an `IndexError`.
- It does not verify that every row has the same number of elements. For example:

```python
data = [
    [1, 2, 3],
    [4, 5]
]
```

is not a proper rectangular matrix.

We will deal with these issues later when we build more serious data structures.

## 13. Complexity

If the dimensions are already known, retrieving the shape is generally $O(1)$.

If we have to inspect every element to determine some property of an $m \times n$ structure, the operation may require $O(mn)$ operations.

## 14. Common Mistakes

**Mistake 1** — Thinking a vector is simply a Python list.
A Python list can represent a vector, but the mathematical object and programming representation are different concepts.

**Mistake 2** — Thinking a matrix is simply a list of lists.
A list of lists can represent a matrix, but matrices have mathematical operations and properties.

**Mistake 3** — Confusing dimension and shape.
$2 \times 3$ describes the shape of a matrix: 2 rows, 3 columns.

**Mistake 4** — Ignoring shapes when working with numerical data.
Many NumPy and PyTorch errors occur because the dimensions of objects do not match the operation being attempted.

## 15. Interview Questions

- What is linear algebra?
- Why is linear algebra important in machine learning?
- What is the difference between a scalar, vector, matrix, and tensor?
- What does the shape `(10000, 5)` represent?
- What is the difference between a mathematical vector and a Python list?
- Why are matrices useful in machine learning?
- What does $Wx+b$ represent conceptually?
- Why is understanding shape important in NumPy and PyTorch?

## 16. Key Mental Model

```
Scalar
   ↓
Vector
   ↓
Matrix
   ↓
Tensor
```

```
Mathematics
    ↓
Representation
    ↓
Python
    ↓
NumPy
    ↓
PyTorch
    ↓
AI
```