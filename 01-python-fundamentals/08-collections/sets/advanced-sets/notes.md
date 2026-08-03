# Python Sets — Advanced Operations

## Union

Returns all unique elements from both sets.

```python
a | b
# or
a.union(b)
```

---

## Intersection

Returns elements common to both sets.

```python
a & b
# or
a.intersection(b)
```

---

## Difference

Returns elements that exist only in the first set.

```python
a - b
# or
a.difference(b)
```

---

## Symmetric Difference

Returns elements that exist in exactly one of the two sets.

```python
a ^ b
# or
a.symmetric_difference(b)
```

---

## Subsets

Checks whether every element of one set exists in another.

```python
admins.issubset(employees)
```

---

## Supersets

Checks whether one set contains all elements of another.

```python
employees.issuperset(admins)
```

---

## Disjoint Sets

Checks whether two sets have no elements in common.

```python
team_a.isdisjoint(team_b)
```

---

## Frozen Sets

A `frozenset` is an immutable version of a set.

```python
permissions = frozenset({"READ", "WRITE"})
```

Because it is immutable, it is hashable and can be used as:

- a dictionary key
- an element inside another set

---

## Set Comprehensions

Create a new set using a comprehension.

```python
squares = {
    n * n
    for n in numbers
}
```

Filtering:

```python
evens = {
    n
    for n in numbers
    if n % 2 == 0
}
```

---

# Choosing the Right Collection

| Collection | Best Use |
|------------|----------|
| List | Ordered sequence, duplicates allowed |
| Tuple | Fixed, immutable records |
| Dictionary | Fast key-value lookup |
| Set | Unique elements, fast membership testing |
| Frozen Set | Immutable unique elements, hashable |

---

# Key Takeaways

- Set operations model mathematical set theory.
- Sets use hash tables for fast membership tests.
- `frozenset` is immutable and hashable.
- Set comprehensions provide a concise way to build unique collections.
- Choose collections based on the required properties of your data.