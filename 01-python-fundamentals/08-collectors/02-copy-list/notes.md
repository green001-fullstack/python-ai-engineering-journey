# Python Collections — Copying Lists

## Overview

A common beginner misconception is that assigning one list to another creates a new list.

```python
a = [1, 2, 3]
b = a
```

This **does not** create a new list.

Instead, both variables reference the **same list object**.

---

# Assignment (`=`)

```python
a = [1, 2]
b = a
```

Memory model:

```
        +-------------+
a ─────►| List Object |
b ─────►| 1 | 2       |
        +-------------+
```

Only one list exists.

Assignment copies the **reference**, not the object.

If the list changes through one variable, every variable referencing it sees the change.

Example:

```python
a.append(3)

print(a)
print(b)
```

Output:

```
[1, 2, 3]
[1, 2, 3]
```

---

# Shallow Copy

```python
a = [1, 2, 3]
b = a.copy()
```

Now there are two different outer list objects.

```
a                     b

│                     │

▼                     ▼

+---------+      +---------+

|1|2|3|      |1|2|3|

+---------+      +---------+
```

Appending to one list does not affect the other.

```python
a.append(4)

print(a)
print(b)
```

Output:

```
[1, 2, 3, 4]
[1, 2, 3]
```

---

# Nested Lists

Consider:

```python
a = [
    [1],
    [2]
]

b = a.copy()
```

The outer list is copied.

The inner lists are **not**.

```
Outer List A

↓

• ───► Inner List #1

↓

• ───► Inner List #2


Outer List B

↓

• ───► Inner List #1

↓

• ───► Inner List #2
```

Both outer lists reference the same inner lists.

If one inner list is modified:

```python
a[0].append(100)
```

Output:

```python
print(b)
```

```
[[1, 100], [2]]
```

This happens because the inner list is shared.

---

# Deep Copy

```python
import copy

b = copy.deepcopy(a)
```

Deep copy creates entirely new objects.

```
Original

Outer List

↓

Inner List A

↓

Inner List B



Deep Copy

Outer List

↓

New Inner List A

↓

New Inner List B
```

Nothing is shared.

Changes to one structure do not affect the other.

---

# Comparison

| Operation | Outer List | Inner Objects |
|------------|------------|---------------|
| `b = a` | Shared | Shared |
| `b = a.copy()` | New | Shared |
| `copy.deepcopy(a)` | New | New |

---

# Performance Considerations

Assignment is the fastest because it creates no new list.

Shallow copy is efficient because it copies only the outer container.

Deep copy is the most expensive because every nested object is duplicated.

Choose the approach that best matches your correctness and performance requirements.

---

# Key Takeaways

- Assignment copies references.
- Lists are mutable.
- Shallow copy creates a new outer list but shares nested objects.
- Deep copy duplicates the entire object graph.
- Immutable objects such as integers are safe to share.
- Understanding Python's object model makes copying behavior predictable rather than something to memorize.

---

# Engineering Insight

Correctness comes before optimization.

When experimenting with nested datasets or customer records, a deep copy may be the safest choice, even though it consumes more memory.

Only optimize after you have confirmed that your program behaves correctly.