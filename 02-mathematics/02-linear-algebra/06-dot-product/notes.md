
| Angle ($\theta$) | Direction Relationship | Visual Meaning |
| :--- | :--- | :--- |
| $\theta = 0^\circ$ | Identical Direction | Parallel; pointing the exact same way. |
| $0^\circ < \theta < 90^\circ$ | Similar Direction | Acute; moving generally forward together, but splitting apart. |
| $\theta = 90^\circ$ | Independent Direction | Perpendicular; one vector has zero effect on the other's path. |
| $90^\circ < \theta < 180^\circ$ | Opposing Direction | Obtuse; moving away from each other. |
| $\theta = 180^\circ$ | Opposite Direction | Parallel; pointing in completely backward directions. |

# The Dot Product

## 1. What Is the Dot Product?

The dot product (weighted sum) is calculated as:

```
weighted score = Σ (xᵢ × wᵢ)
```

For:

```python
features = [30, 5, 2, 85]
weights  = [0.1, 0.5, -0.3, 0.8]
```

the calculation is:

```
30 × 0.1  =  3.0
 5 × 0.5  =  2.5
 2 × -0.3 = -0.6
85 × 0.8  = 68.0
----------------
             72.9
```

So:

```
Weighted Score: 72.9
```

---

## 2. Pure Python Implementation

```python
def weighted_score(features, weights):
    if len(features) != len(weights):
        raise ValueError("features and weights must be the same length")

    return sum(f * w for f, w in zip(features, weights))

features = [30, 5, 2, 85]
weights  = [0.1, 0.5, -0.3, 0.8]

print(weighted_score(features, weights))
# Output: 72.9
```

### Why the dimension check matters

```python
if len(features) != len(weights):
    raise ValueError(...)
```

A dot product requires **corresponding elements**. For example:

```
[30, 5, 2, 85]
[0.1, 0.5, -0.3]
```

doesn't make mathematical sense as a standard dot product, because there isn't a weight for `85`. Validating the lengths first prevents a silently wrong (or crashing) computation.

---

## 3. The AI Insight

This is a tiny piece of what happens inside a machine-learning model.

You started with:

```
features
    ↓
[30, 5, 2, 85]
```

and:

```
weights
    ↓
[0.1, 0.5, -0.3, 0.8]
```

Then:

```
       features
          ↓
[30, 5, 2, 85]
          ×
[0.1, 0.5, -0.3, 0.8]
          ↓
     DOT PRODUCT
          ↓
        72.9
```

That `72.9` is a **weighted combination of the features** — not just an arbitrary Python exercise, but the mathematical foundation underneath AI:

```
Linear Algebra
      ↓
Linear models
      ↓
Neural network layers
      ↓
Deep learning
      ↓
Transformers
      ↓
LLMs
```

---

## 4. NumPy Implementation

Since the mathematics was implemented manually above, here's the same idea expressed in NumPy:

```python
import numpy as np

features = np.array([30, 5, 2, 85])
weights = np.array([0.1, 0.5, -0.3, 0.8])

score = np.dot(features, weights)

print(score)
# Output: 72.9
```

### Pure Python vs NumPy

**Pure Python** — you explicitly implement the mathematics:

```python
sum(f * w for f, w in zip(features, weights))
```

**NumPy** — you tell NumPy what mathematical operation you want:

```python
np.dot(features, weights)
```

Same mathematics, different implementation. That relationship — explicit computation vs. declarative/vectorized computation — is central to how NumPy (and most ML libraries) work.

---

## 5. Mini Challenge — Multiple Applicants at Once

Given three applicants:

```python
import numpy as np

applicants = np.array([
    [30, 5, 2, 85],
    [25, 3, 1, 71],
    [40, 8, 4, 90]
])

weights = np.array([0.1, 0.5, -0.3, 0.8])
```

**Goal:** compute a score for each applicant — without a Python `for` loop.

### Solution

```python
score = np.dot(applicants, weights)

print(score)
print(score.shape)
```

Output:

```
[72.9 61.8 80.6]
(3,)
```

This introduces **matrix × vector multiplication** — the bridge from vectors to matrices.

---

## 6. Understanding the Shapes

```python
score = np.dot(applicants, weights)
```

computes the dot product of **each applicant row** with the weight vector.

| Array | Shape |
|---|---|
| `applicants` | `(3, 4)` |
| `weights` | `(4,)` |
| `score` | `(3,)` |

Conceptually:

```
                 weights
                    ↓
Applicant 1 ──→ 72.9
Applicant 2 ──→ 61.8
Applicant 3 ──→ 80.6
```

---

## 7. What You Just Discovered

You started with **one applicant**:

```
x · w = one score
```

Then expanded to **many applicants**:

```
Xw = many scores
```

where:

```
X = applicants   (a matrix — many rows of features)
w = weights      (a single vector)
```

This is one of the most important patterns in machine learning:

> **Many observations × their feature weights → predictions/scores.**

And notice something beautiful: **no loop was written.** NumPy performed the operation across all rows automatically. That's **vectorization**, which you'll encounter constantly in AI/ML.

---

## 8. Summary

- **Dot product:** `Σ(xᵢ × wᵢ)` — combines a feature vector and a weight vector into a single weighted score.
- Always validate that `features` and `weights` are the same length before computing.
- `np.dot(a, b)` computes the same result as `sum(f * w for f, w in zip(a, b))`, but vectorized.
- `np.dot(matrix, vector)` applies the dot product **row-by-row** across a matrix — turning `(3, 4) · (4,) → (3,)`.
- This is the mathematical seed of linear models, neural network layers, and eventually transformers/LLMs: **many observations × weights → scores**, computed without explicit loops.