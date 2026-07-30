# Python Tuples — Hashability

## What is a Hash?

A hash is a numeric value computed from an object.

Python uses hashes to quickly locate objects in dictionaries and sets.

```python
hash("Sarah")
hash(100)
hash((1, 2))
```

---

## Hashable Objects

An object is **hashable** if it can produce a stable hash value throughout its lifetime.

Examples:

- Integers
- Floats
- Strings
- Booleans
- None
- Tuples (when all elements are hashable)

---

## Unhashable Objects

Mutable objects are generally unhashable because their contents can change.

Examples:

- Lists
- Dictionaries
- Sets

```python
hash([1, 2])      # TypeError
hash({"x": 1})    # TypeError
```

---

## Why Dictionaries Need Hashable Keys

A dictionary stores key-value pairs using a hash table.

When a key is inserted:

1. Python computes the key's hash.
2. The hash determines where the key is stored.
3. Future lookups compute the same hash to retrieve the value quickly.

If a key's hash could change after insertion, the dictionary would no longer know where to find it.

---

## Why Lists Cannot Be Keys

Lists are mutable.

```python
key = [1, 2]
```

If lists were allowed as dictionary keys, modifying the list could change its hash and make the key unreachable.

Python prevents this by making lists unhashable.

---

## Why Tuples Can Be Keys

Tuples are immutable.

```python
location = (6.5244, 3.3792)
```

Since their contents cannot change (provided every element is hashable), their hash remains stable.

This makes tuples safe dictionary keys.

---

## Important Rule

A tuple is hashable **only if every element inside it is hashable**.

Examples:

```python
(1, 2)
("John", 25)
(True, None)
```

Not hashable:

```python
([1, 2], 3)
({"x": 1}, 5)
```

---

## Key Takeaways

- Dictionaries rely on hashing for fast lookups.
- Hash values must remain stable.
- Mutable objects are generally unhashable.
- Tuples are hashable only when all of their elements are hashable.
- Hashability is a consequence of object design, not an arbitrary language rule.