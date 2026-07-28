# Python Collections — Tuples (Part 1)

## Overview

A tuple is an **immutable** Python object that stores an ordered collection of references.

Like lists, tuples preserve order and support indexing and slicing.

Unlike lists, tuples cannot be modified after creation.

---

# Creating a Tuple

```python
point = (10, 20)
```

Python creates a tuple object containing references to two integer objects.

---

# Characteristics

- Ordered
- Immutable
- Stores references
- Supports indexing
- Supports slicing
- Can contain any Python object

---

# Indexing

```python
point = (10, 20)

print(point[0])
```

Output:

```python
10
```

Negative indexing also works.

```python
point[-1]
```

returns:

```python
20
```

---

# Immutability

This is not allowed:

```python
point[0] = 99
```

Python raises a `TypeError` because tuples cannot have their elements reassigned.

---

# Mutable Objects Inside Tuples

Although the tuple itself is immutable, it may reference mutable objects.

```python
data = (
    [1, 2],
    [3, 4]
)

data[0].append(100)
```

Output:

```python
([1, 2, 100], [3, 4])
```

The tuple did not change.

The list inside the tuple changed.

---

# Packing

Python automatically creates tuples.

```python
person = "John", 25, "Dentist"
```

This is equivalent to:

```python
person = ("John", 25, "Dentist")
```

---

# Unpacking

```python
person = ("John", 25)

name, age = person
```

Python assigns:

- `name` → `"John"`
- `age` → `25`

---

# One-Element Tuples

Incorrect:

```python
value = (10)
```

This is just an integer.

Correct:

```python
value = (10,)
```

The comma creates the tuple.

---

# Tuple vs List

| Feature | List | Tuple |
|---------|------|-------|
| Ordered | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Stores references | ✅ | ✅ |
| Supports indexing | ✅ | ✅ |
| Supports slicing | ✅ | ✅ |

---

# When to Use Tuples

Use tuples when the data:

- represents a fixed record,
- should not change,
- communicates constant values,
- groups related values together.

Examples:

- GPS coordinates
- RGB colors
- Dates
- Dimensions
- Database identifiers

---

# Key Takeaways

- Tuples are immutable collections.
- They store references just like lists.
- The tuple itself cannot change after creation.
- Mutable objects inside a tuple can still be modified.
- The comma, not the parentheses, creates a tuple.