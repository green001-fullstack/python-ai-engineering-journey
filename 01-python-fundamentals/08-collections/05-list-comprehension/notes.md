# Python Collections — List Comprehensions

## Overview

A list comprehension is a concise way to create a new list by iterating over an iterable, optionally filtering elements, and transforming them.

It replaces the common pattern of:

```python
result = []

for item in iterable:
    result.append(expression)
```

with:

```python
result = [expression for item in iterable]
```

---

# Basic Syntax

```python
result = [expression for item in iterable]
```

Read it as:

> For each item in the iterable, produce the expression.

Example:

```python
numbers = [1, 2, 3, 4]

squares = [x * x for x in numbers]
```

Output:

```python
[1, 4, 9, 16]
```

---

# Filtering

A condition can be added to include only selected elements.

```python
numbers = [1, 2, 3, 4, 5]

evens = [x for x in numbers if x % 2 == 0]
```

Output:

```python
[2, 4]
```

---

# Transforming and Filtering

Both operations can be combined.

```python
numbers = [1, 2, 3, 4, 5]

even_squares = [
    x * x
    for x in numbers
    if x % 2 == 0
]
```

Output:

```python
[4, 16]
```

---

# Object Model

A list comprehension **creates a new list object**.

It does **not** modify the original list.

Example:

```python
numbers = [1, 2, 3]

result = [x + 1 for x in numbers]
```

After execution:

- `numbers` still references the original list.
- `result` references a new list.

---

# Advantages

- Shorter than writing a loop with `append()`.
- Clearly expresses the intent to build a new list.
- Usually easier to read for simple transformations.
- Often slightly faster because Python performs much of the work internally.

---

# When Not to Use a List Comprehension

Avoid comprehensions when:

- The logic becomes difficult to understand.
- Multiple nested conditions are required.
- Several statements need to run for each iteration.
- Readability suffers.

In these situations, a normal `for` loop is usually a better choice.

---

# Comparison

Loop:

```python
result = []

for x in numbers:
    result.append(x * 10)
```

Comprehension:

```python
result = [x * 10 for x in numbers]
```

Both produce the same result.

---

# Key Takeaways

- A list comprehension creates a **new list**.
- It combines iteration and transformation into one expression.
- Filtering is optional.
- Read comprehensions from **right to left**:
  - `for ...`
  - optional `if ...`
  - expression to produce.
- Prefer comprehensions for simple, readable transformations.
- Prefer loops when the logic becomes complex.