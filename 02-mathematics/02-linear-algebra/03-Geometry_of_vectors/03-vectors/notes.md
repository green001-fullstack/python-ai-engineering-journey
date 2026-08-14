# Vectors

## 1. The Problem: Why Do We Need Vectors?

Imagine Atlas has one applicant:

```
Age:             29
Monthly income:  700,000
Loan amount:     1,500,000
Trust score:     82
```

Each individual value is a **scalar**.

But suppose we want to give the entire applicant to a machine-learning model.

We don't want to pass:

```
age = 29
income = 700000
loan = 1500000
trust_score = 82
```

as four unrelated quantities.

We want to represent them together:

```
x = [29, 700000, 1500000, 82]
```

This is a **vector**.

So our first important mental model is:

> A vector is a structured collection of numerical values that can represent several related quantities together.

---

## 2. What Is a Vector?

A vector is an **ordered collection of numbers**.

For example:

```
x = [2, 4, 6]
```

contains three numbers.

We call these numbers the **components** or **elements** of the vector.

So `x = [2, 4, 6]` has:

- 3 components
- dimension 3

We can also write it horizontally or vertically — these can represent the same vector, depending on the mathematical context.

---

## 3. Scalar vs Vector

This distinction is extremely important.

**Scalar**
```
5
```
One value.

**Vector**
```
[5, 10, 15]
```
Three values grouped together.

Think:

```
Scalar
   ↓
one number

Vector
   ↓
multiple ordered numbers
```

For example:

```
age = 29          # scalar
applicant = [29, 700000, 1500000, 82]   # vector
```

---

## 4. Why "Ordered" Matters

Consider:

```
[29, 700000, 1500000, 82]
```

We have to know what each position means:

```
position 0 → age
position 1 → income
position 2 → loan amount
position 3 → trust score
```

If we randomly rearrange the values:

```
[82, 1500000, 29, 700000]
```

the vector now means something completely different.

> The order of a vector's components matters.

This is one of the differences between a vector and an ordinary mathematical "bag" of numbers.

---

## 5. Vector Dimension

The **dimension** of a vector tells us how many components it contains.

For `x = [2, 4, 6]`, we have 3 components. Therefore:

```
x ∈ R³
```

This means: *x is a vector in three-dimensional real-number space.*

Another example: `x = [29, 700000, 1500000, 82]` has dimension 4, so `x ∈ R⁴`.

---

## 6. Row Vector vs Column Vector

There are two common ways to write a vector.

**Column vector**
```
[2]
[4]
[6]
```
Shape → `(3, 1)`

**Row vector**
```
[2 4 6]
```
Shape → `(1, 3)`

Both contain three numbers, but their shapes are different. This distinction becomes extremely important when we start multiplying matrices and vectors.

---

## 7. Vector as a Point

Vectors can be interpreted geometrically.

Consider `v = [3, 2]`. We can visualize this as the point `(3, 2)` on a coordinate plane.

The important idea isn't a particular drawing — it's that a two-component vector gives us two coordinates: `(x, y)`.

```
Vector:
[3]
[2]

↓

Point:
(3, 2)
```

So a vector can tell us **where something is**.

---

## 8. Vector as a Direction

A vector can also represent a direction.

Suppose `v = [3, 2]`. We can draw an arrow starting at the origin and ending at `(3, 2)`.

Conceptually:

```
        • (3,2)
       /
      /
     /
    /
   /
  •
 (0,0)
```

The arrow tells us: *move 3 units horizontally and 2 units vertically.*

So vectors can represent:

- position
- displacement
- direction
- velocity
- features
- model parameters

This flexibility is one reason vectors are so important.

---

## 9. Vector as Features

This is where things become particularly important for AI.

Suppose we have an applicant:

```
Age = 29
Income = 700,000
Loan = 1,500,000
Trust Score = 82
```

We can represent the applicant as:

```
x = [29, 700000, 1500000, 82]
```

Each component represents a **feature**:

```
x₁ → age
x₂ → income
x₃ → loan amount
x₄ → trust score
```

The model can now operate on the entire applicant using mathematical operations.

This is a huge conceptual transition:

```
Real-world object
       ↓
Features
       ↓
Numbers
       ↓
Vector
       ↓
Machine-learning model
```

---

## 10. High-Dimensional Vectors

Don't think vectors are limited to two or three dimensions.

An applicant could have:

- 5 features
- 20 features
- 100 features
- 500 features

A text embedding might have hundreds or thousands of dimensions.

For example, `x ∈ R⁷⁶⁸` means the vector contains 768 numerical components. This is common in modern AI.

You cannot physically visualize a 768-dimensional vector easily, but mathematically it is still just an ordered collection of numbers.

---

## 11. Pure Python Representation

We can represent a vector using a list:

```python
applicant = [
    29,
    700000,
    1500000,
    82
]
```

We can access individual components:

```python
print(applicant[0])
print(applicant[1])
print(applicant[2])
print(applicant[3])
```

Output:

```
29
700000
1500000
82
```

Remember: Python starts indexing at 0.

```
index 0 → age
index 1 → income
index 2 → loan
index 3 → trust score
```

---

## 12. A Vector Has Structure

We shouldn't think `[29, 700000, 1500000, 82]` is merely "a list."

Conceptually, we're using that list to represent a structured vector `x`. This distinction will become important as we build our own mathematical operations.

---

## 13. NumPy Representation

NumPy is much better suited for numerical vectors.

```python
import numpy as np

applicant = np.array([
    29,
    700000,
    1500000,
    82
])
```

Check its shape:

```python
print(applicant.shape)
```

Output:

```
(4,)
```

This means: *a one-dimensional array containing 4 elements.*

Notice that NumPy reports `(4,)` rather than `(4, 1)`. That is because this is a 1-dimensional array, not explicitly a 4-by-1 matrix. This distinction will become very important later.

---

## 14. Vector Arithmetic

Suppose:

```
a = [1, 2, 3]
b = [4, 5, 6]
```

We can add them component by component:

```
a + b = [1+4, 2+5, 3+6] = [5, 7, 9]
```

In NumPy:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
```

Output:

```
[5 7 9]
```

Notice something important:

```
vector + vector
       ↓
     vector
```

---

## 15. Scalar Multiplication

A scalar can multiply a vector.

Suppose `x = [2, 4, 6]` and `c = 3`. Then:

```
3x = [6, 12, 18]
```

Every component gets multiplied by 3.

In Python:

```python
x = [2, 4, 6]

result = [3 * value for value in x]

print(result)
```

Output:

```
[6, 12, 18]
```

In NumPy:

```python
import numpy as np

x = np.array([2, 4, 6])

print(3 * x)
```

Output:

```
[ 6 12 18]
```

This is one of the first places where NumPy becomes extremely powerful.

---

## 16. Why NumPy Matters

Pure Python:

```python
result = [3 * value for value in x]
```

requires us to explicitly iterate.

NumPy:

```python
result = 3 * x
```

allows the numerical operation to be expressed directly. This is called **vectorization**.

> Vectorization allows numerical operations to be performed efficiently over entire arrays without writing explicit Python loops for each element.

---

## 17. AI Connection — Feature Vectors

Suppose we have 20 applicant features:

```
x = [x₁, x₂, ..., x₂₀]
```

This is a 20-dimensional feature vector.

A model might have corresponding weights:

```
w = [w₁, w₂, ..., w₂₀]
```

Later, we'll learn how these vectors interact through the **dot product**.

Eventually, `wᵀx` will allow the model to combine all 20 features into a single number.

That single operation is foundational to:

- linear regression
- logistic regression
- neural networks
- embeddings
- attention mechanisms

So vectors are not just a mathematical topic we're studying because we have to. They are one of the fundamental languages of AI.

---

## 18. Hands-On Exercise — VS Code

Create:

```
phase_1/
    02_vectors.py
```

Start with:

```python
applicant = [
    29,
    700000,
    1500000,
    82
]

print("Applicant vector:", applicant)
print("Number of features:", len(applicant))
```

Expected:

```
Applicant vector: [29, 700000, 1500000, 82]
Number of features: 4
```

Now print each feature:

```python
print("Age:", applicant[0])
print("Income:", applicant[1])
print("Loan:", applicant[2])
print("Trust Score:", applicant[3])
```

---

## 19. Your First Vector Function

Write this yourself before looking at an implementation:

```python
def add_vectors(a, b):
    # your implementation
```

Given:

```python
a = [1, 2, 3]
b = [4, 5, 6]
```

the function should return:

```python
[5, 7, 9]
```

**Think about the algorithm.** You need to:

1. Create a result.
2. Visit each position.
3. Add the corresponding elements.
4. Store the result.
5. Return the result.

Try implementing it yourself.

---

## 20. NumPy Version

After your pure Python implementation, implement the same operation using NumPy:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a + b

print(result)
```

Compare:

```
Pure Python
     ↓
Explicit loop
     ↓
Manual element-by-element operation


NumPy
     ↓
Vectorized operation
     ↓
a + b
```

This is exactly the type of hands-on progression we'll continue throughout the AI journey.

---

## 21. Vector Length

The number of components in a vector is its dimension.

For `x = [2, 4, 6, 8]`, dimension = 4.

In Python:

```python
x = [2, 4, 6, 8]

print(len(x))
```

Output:

```
4
```

In NumPy:

```python
x = np.array([2, 4, 6, 8])

print(x.shape)
print(x.ndim)
```

Output:

```
(4,)
1
```

So:

```
shape → (4,)
ndim  → 1
```

---

## 22. Vector Shape vs Vector Dimension

Be careful here.

For:

```python
x = np.array([1, 2, 3])
```

we have:

```
dimension → 1
shape     → (3,)
```

The vector is one-dimensional, but it contains three elements. These concepts are related but different.

- **ndim** = number of axes
- **shape** = size along each axis

This distinction becomes crucial when we work with matrices and tensors.

---

## 23. Complexity

Suppose `a, b ∈ Rⁿ` and we want to add them. We must process all n components.

Therefore: **O(n)** time complexity.

For example:

```
3 elements         → 3 additions
1,000 elements      → 1,000 additions
1,000,000 elements  → 1,000,000 additions
```

Space complexity for creating a new result vector is also **O(n)**, because we store n results.

---

## 24. Common Mistakes

**Mistake 1 — Thinking every Python list is a vector**

```python
x = [1, 2, 3]
```

is a Python list. It can represent a vector, but Python itself doesn't automatically impose vector mathematics on it.

**Mistake 2 — Forgetting order**

```
[age, income, loan, trust]
```

is not equivalent to:

```
[income, age, loan, trust]
```

The positions have meaning.

**Mistake 3 — Confusing (3,) with (3,1)**

These are different shapes:

- `(3,)` means a one-dimensional array with 3 elements.
- `(3,1)` means 3 rows and 1 column.

We will explore this deeply when matrices begin.

**Mistake 4 — Assuming vectors must have three dimensions**

Vectors can have:

```
1 dimension
2 dimensions
3 dimensions
10 dimensions
100 dimensions
768 dimensions
4096 dimensions
```

There is no requirement that a vector must be visually representable.

---

## 25. Interview Questions

Try answering these without looking back.

1. What is a vector?
2. What is the difference between a scalar and a vector?
3. What does the dimension of a vector mean?
4. What is the difference between a row vector and a column vector?
5. What does NumPy shape `(5,)` mean?
6. What is the difference between `(5,)` and `(5,1)`?
7. Why are vectors important in machine learning?
8. What does a feature vector represent?
9. Why does vector addition have O(n) complexity?
10. Give three different ways vectors are used in AI.

---

## 🧠 Engineer Thinking

Here's an important question:

> Suppose Atlas has 1 million applicants, and each applicant has 50 features. How could we represent the entire dataset?

Think about:

```
One applicant
      ↓
Vector
      ↓
1 million applicants
      ↓
???
```

This question naturally leads us to our next mathematical structure: **Matrices**.

But don't jump there yet. First, master the vector.