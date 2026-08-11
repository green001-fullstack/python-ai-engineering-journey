# Linear Algebra — Vectors
### Phase 1: The Language of Linear Algebra

---

## 1. What Is a Vector?

A vector is an **ordered collection of numbers**.

$$\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$$

In Python:
```python
v = [3, 4]
```

The key word is **ordered** — position matters. `[3, 4]` is not the same as `[4, 3]`.

---

## 2. Vector Dimensions

The number of components in a vector determines its **dimension**.

| Vector | Dimension |
|---|---|
| `[5]` | 1D |
| `[3, 4]` | 2D |
| `[1, 2, 3]` | 3D |
| `[29, 700000, 1500000, 82]` | 4D |

In machine learning, dimensions often represent **features**, e.g. `[age, income, loan_amount, trust_score]`.

---

## 3. Vectors as Features

A vector can represent the features of a single observation:

```
applicant = [29, 700000, 1500000, 82]
```

| Value | Meaning |
|---|---|
| 29 | age |
| 700000 | monthly income |
| 1500000 | loan amount |
| 82 | trust score |

This is a 4-dimensional **feature vector**.

---

## 4. Vectors as Points

A 2D vector can be interpreted as a point: `[3, 4]` ↔ `(3, 4)`.

> ⚠️ A vector and a point are **not** mathematically identical. The same numbers `[3, 4]` could represent a point, a displacement, a feature vector, a direction+magnitude, or a plain mathematical vector — **meaning depends on context**.

---

## 5. Vectors as Directions

`[3, 4]` can represent movement: 3 units right, 4 units up.

Starting at `(0, 0)` and applying `[3, 4]` → arrive at `(3, 4)`.

---

## 6. Displacement Between Two Points

$$\mathbf{v} = \text{end} - \text{start}$$

Given `start = (2, 1)`, `end = (5, 5)`:

$$\mathbf{v} = (5-2,\ 5-1) = (3, 4)$$

---

## 7. Displacement — Pure Python

```python
start = [2, 1]
end = [5, 5]

vector = [
    end[i] - start[i]
    for i in range(len(start))
]

print(vector)  # [3, 4]
```

---

## 8. Displacement — NumPy

```python
import numpy as np

start = np.array([2, 1])
end = np.array([5, 5])

vector = end - start
print(vector)  # [3 4]
```

NumPy performs the subtraction **element by element**.

---

## 9–11. Vector Addition

$$a + b = [a_1+b_1,\ a_2+b_2,\ a_3+b_3]$$

Given `a = [1, 2, 3]`, `b = [4, 5, 6]` → `a + b = [5, 7, 9]`

**Pure Python:**
```python
def add_vectors(a, b):
    return [x + y for x, y in zip(a, b)]

print(add_vectors([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]
```

**NumPy:**
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # [5 7 9]
```

---

## 12–14. Vector Subtraction

Given `a = [1, 2, 3]`, `b = [4, 5, 6]` → `a - b = [-3, -3, -3]`

**Pure Python:**
```python
def subtract_vectors(a, b):
    return [x - y for x, y in zip(a, b)]
```

**NumPy:**
```python
result = a - b  # [-3 -3 -3]
```

---

## 15–17. Scalar Multiplication

A scalar is a single number. Given `v = [2, 4, 6]`, `c = 3`:

$$3v = [3(2), 3(4), 3(6)] = [6, 12, 18]$$

The scalar changes the **size** of the vector.

**Pure Python:**
```python
def scale_vector(vector, scalar):
    return [scalar * value for value in vector]
```

**NumPy:**
```python
result = scalar * vector  # [ 6 12 18]
```

---

## 18–21. Linear Combinations

A linear combination mixes scalar multiplication and addition, e.g. `2a + 3b`.

Given `a = [1, 2, 3]`, `b = [4, 5, 6]`:
- `2a = [2, 4, 6]`
- `3b = [12, 15, 18]`
- `2a + 3b = [14, 19, 24]`

**Pure Python:**
```python
def linear_combination(a, b, scalar_a, scalar_b):
    return [scalar_a * x + scalar_b * y for x, y in zip(a, b)]
```

**NumPy (with subtraction, e.g. `4a - 2b`):**
```python
import numpy as np

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
result = 4 * a - 2 * b  # [ 6 10 14]
```

NumPy syntax stays very close to the mathematical notation.

---

## 22–26. Vector Magnitude (Euclidean / L2 Norm)

For `v = [3, 4]`:

$$\|v\| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$$

**General formula** for n-dimensional vectors:

$$\|v\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**Pure Python:**
```python
import math

def vector_magnitude(vector):
    square = [x * x for x in vector]
    return math.sqrt(sum(square))

print(vector_magnitude([6, 8]))  # 10.0
```

**NumPy:**
```python
import numpy as np

magnitude = np.linalg.norm(np.array([6, 8]))  # 10.0
```

**Geometric meaning:** `[3, 4]` has magnitude 5; `[6, 8]` has magnitude 10 — same direction, second vector is twice as long.

---

## 27–31. Direction of a Vector

For `v = [x, y]`, direction is the angle measured **counterclockwise from the positive x-axis**:

$$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$

For `[3, 4]`: θ ≈ 53.13°

> Use `math.atan2(y, x)` instead of `math.atan(y / x)` — it correctly handles the quadrant.

```python
import math

angle_radians = math.atan2(4, 3)
angle_degrees = math.degrees(angle_radians)
print(angle_degrees)  # 53.13010235415598
```

**Quadrants** (sign of x, y):

```
             y+
              ↑
        II    |    I
              |
x− ←──────────┼──────────→ x+
              |
       III    |    IV
              ↓
             y−
```

| x | y | Quadrant |
|---|---|---|
| + | + | I |
| − | + | II |
| − | − | III |
| + | − | IV |

**Four vectors, equal magnitude (5), different direction:**

| Vector | Angle |
|---|---|
| `[3, 4]` | 53.13° |
| `[-3, 4]` | 126.87° |
| `[-3, -4]` | 233.13° |
| `[3, -4]` | 306.87° |

> **Magnitude tells us how much. Direction tells us where.**

**Normalizing angle to 0–360°:**
```python
import math

x, y = -3, 4
angle = math.degrees(math.atan2(y, x))
if angle < 0:
    angle += 360
print(angle)  # 126.87... → Quadrant II
```

---

## 32–36. Vector Normalization

Normalization rescales a vector to **magnitude 1** while preserving direction:

$$\hat{v} = \frac{v}{\|v\|}$$

For `v = [3, 4]`, `‖v‖ = 5`:

$$\hat{v} = \left[\frac{3}{5}, \frac{4}{5}\right] = [0.6, 0.8]$$

**Key property:** `[3, 4]` and `[6, 8]` point in the same direction and both normalize to `[0.6, 0.8]`.

**Pure Python:**
```python
import math

def normalize_vector(vector):
    magnitude = math.sqrt(sum(x * x for x in vector))
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    return [x / magnitude for x in vector]
```

**NumPy:**
```python
import numpy as np

def normalize_vector(vector):
    vector = np.array(vector)
    magnitude = np.linalg.norm(vector)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    return vector / magnitude
```

**Zero vector problem:** `‖[0, 0, ..., 0]‖ = 0`, so normalizing it requires dividing by zero — always guard against this.

---

## 37–39. Row and Column Vectors & Shape

| Form | Shape |
|---|---|
| `np.array([1, 2, 3])` | `(3,)` — 1D array |
| `np.array([[1, 2, 3]])` | `(1, 3)` — row vector |
| `np.array([[1], [2], [3]])` | `(3, 1)` — column vector |

**Transposing a row vector:**
```python
import numpy as np

row_v = np.array([[1, 2, 3]])
print(row_v.shape)          # (1, 3)

transposed_v = row_v.T
print(transposed_v)
# [[1]
#  [2]
#  [3]]
print(transposed_v.shape)   # (3, 1)
```

> Although `(3,)`, `(1, 3)`, and `(3, 1)` may contain the same numbers, their mathematical roles differ — this matters a great deal for matrix multiplication.

---

## 40–44. Vectors & Matrices in Machine Learning

A single observation = a vector. Multiple observations = a **matrix**.

```python
applicants = [
    [29, 700000, 1500000, 82],
    [35, 500000, 900000, 71],
    [24, 300000, 400000, 65]
]
```

This has shape `(3, 4)` → 3 applicants, 4 features.

```python
import numpy as np

applicants = np.array([
    [29, 700000, 1500000, 82],
    [35, 500000, 900000, 71],
    [24, 300000, 400000, 65]
])
print(applicants.shape)  # (3, 4)
```

**Indexing:**
```python
applicants[2, 3]   # row 2, column 3 → 65 (trust score of 3rd applicant)
applicants[:, 3]    # every row, column 3 → [82, 71, 65] (trust score column)
```

---

## 45–47. Python Lists vs. NumPy Arrays

```python
[1, 2, 3] + [4, 5, 6]                      # → [1, 2, 3, 4, 5, 6]  (concatenation!)
np.array([1, 2, 3]) + np.array([4, 5, 6])  # → [5 7 9]             (element-wise)
```

> A Python list does **not** automatically behave like a mathematical vector.

**Function call reminder:**
```python
print(add_vectors)        # prints the function object
print(add_vectors(a, b))  # actually calls it
```

**Dimension validation:**
```python
def vector_addition(a, b):
    if len(a) != len(b):
        raise ValueError(
            f"Vector dimensions must match. Found {len(a)} and {len(b)}"
        )
    return [x + y for x, y in zip(a, b)]
```

---

## 48. AI / ML Connection

```
Real-world data
      ↓
Numerical features
      ↓
Feature vector
      ↓
Feature matrix
      ↓
Mathematical operations
      ↓
Machine-learning model
      ↓
Prediction
```

**Example pipeline:**
```
Financial Evidence → Numerical features → Applicant feature vector
→ Dataset matrix → ML model → Trust Assessment
```

---

## 49. Vector Embeddings

Modern AI represents words, sentences, documents, images, users, and products as vectors:

```
[0.21, -0.54, 0.81, 0.13, ...]
```

Real embeddings often have hundreds or thousands of dimensions.

> **Core idea:** similar things are represented by vectors that are close together in mathematical space (explored later via dot products & cosine similarity).

---

## 50. Complexity Analysis

For a vector of `n` elements:

| Operation | Complexity |
|---|---|
| Addition | O(n) |
| Subtraction | O(n) |
| Scalar multiplication | O(n) |
| Magnitude | O(n) |
| Normalization | O(n) |
| Extra memory (new result vector) | O(n) |

---

## 51. Common Mistakes

1. **Thinking every Python list is a vector** — it can represent one, but isn't automatically one.
2. **Forgetting vector order** — `[1, 2] ≠ [2, 1]`.
3. **Ignoring dimensions** — can't add `[1, 2, 3]` to `[4, 5]`.
4. **Confusing point and vector** — `[3, 4]` means different things in different contexts.
5. **Forgetting the zero-vector problem** — can't normalize `[0, 0]` (magnitude 0).
6. **Confusing shape** — `(3,)`, `(1, 3)`, and `(3, 1)` are all different.
7. **Forgetting NumPy ≠ Python list** — `+` concatenates lists but adds arrays element-wise.