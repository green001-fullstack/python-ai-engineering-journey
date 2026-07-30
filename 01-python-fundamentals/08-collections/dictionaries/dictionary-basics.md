# Python Collections — Dictionaries (Part 1)

## Overview

A dictionary is a **mutable** Python object that stores **key-value pairs** using a **hash table**.

Unlike lists, dictionaries are indexed by **keys** instead of numeric positions.

---

# Creating a Dictionary

```python
ages = {
    "John": 25,
    "Mary": 30
}
```

Each entry consists of:

```
key → value
```

Example:

```
"John" → 25
```

---

# Accessing Values

```python
print(ages["John"])
```

Output:

```python
25
```

Python computes the key's hash, locates the correct position in the hash table, and returns the associated value.

---

# Dictionary Keys

Keys must be:

- Hashable
- Unique

Examples of valid keys:

```python
1
"John"
(6.5244, 3.3792)
True
None
```

Invalid keys:

```python
[1, 2]
{"x": 1}
{1, 2}
```

These objects are mutable and therefore unhashable.

---

# Values

Values may be any Python object.

They do **not** need to be unique.

```python
ages = {
    "John": 25,
    "Mary": 25,
    "David": 25
}
```

---

# Updating Values

```python
ages["John"] = 40
```

If the key already exists, its value is replaced.

---

# Adding New Entries

```python
ages["Alice"] = 28
```

A new key-value pair is added to the dictionary.

---

# Duplicate Keys

```python
ages = {
    "John": 25,
    "John": 40
}
```

Result:

```python
{
    "John": 40
}
```

The last assignment wins because keys must be unique.

---

# Dictionaries Store References

A dictionary stores references to objects, not copies.

```python
scores = {
    "math": [80, 90]
}

scores["math"].append(100)
```

Output:

```python
{
    "math": [80, 90, 100]
}
```

The dictionary still points to the same list. The list itself changed.

---

# Dictionary vs List

| List | Dictionary |
|------|------------|
| Indexed by position | Indexed by key |
| Lookup by index | Lookup by hash |
| Good for ordered sequences | Good for fast retrieval by key |

---

# Key Takeaways

- Dictionaries map keys to values.
- Keys must be unique and hashable.
- Values can be any Python object.
- Dictionaries are mutable.
- Dictionaries store references, not copies.
- Hash tables provide fast lookups.