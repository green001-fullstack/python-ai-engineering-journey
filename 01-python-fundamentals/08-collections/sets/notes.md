# Python Collections — Sets

## Overview

A **set** is a mutable Python object that stores **unique hashable objects** using a **hash table**.

Unlike dictionaries, sets store only elements (no key-value pairs).

---

# Creating Sets

```python
fruits = {"Apple", "Banana", "Orange"}
```

To create an empty set:

```python
fruits = set()
```

> `{}` creates an empty dictionary, **not** an empty set.

---

# Uniqueness

Sets automatically remove duplicates.

```python
numbers = {1, 2, 2, 3, 1}
```

Result:

```python
{1, 2, 3}
```

---

# Hashability

Set elements must be **hashable**.

Valid:

```python
1
"Python"
(1, 2)
True
None
```

Invalid:

```python
[1, 2]
{"a": 1}
{1, 2}
```

Mutable objects cannot be hashable because changes would invalidate the hash-table structure.

---

# Membership Testing

```python
"APP001" in applicants
```

Membership testing is very fast because sets use hash tables.

---

# Adding Elements

```python
fruits.add("Banana")
```

Adding an existing element has no effect.

---

# Removing Elements

```python
fruits.remove("Apple")
```

Raises a `KeyError` if the element does not exist.

Safe alternative:

```python
fruits.discard("Apple")
```

Does nothing if the element is absent.

---

# Set Operations

## Union

```python
a | b
```

Elements in either set.

---

## Intersection

```python
a & b
```

Elements common to both sets.

---

## Difference

```python
a - b
```

Elements only in the first set.

---

## Symmetric Difference

```python
a ^ b
```

Elements in exactly one of the sets.

---

# Key Takeaways

- Sets store unique elements.
- Elements must be hashable.
- Sets are mutable.
- Membership testing is very fast.
- Sets are built on hash tables.
- Set operations make working with collections concise and efficient.