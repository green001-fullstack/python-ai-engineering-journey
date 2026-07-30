# Python Collections — List Methods

## Overview

List methods operate on **list objects**.

Most list methods **modify the existing list** rather than creating a new one.

Understanding which methods modify a list and which return new objects helps avoid common Python bugs.

---

# Growing a List

## append()

```python
numbers = [1, 2]
numbers.append(3)
```

Output:

```python
[1, 2, 3]
```

- Adds a single object to the end of the list.
- Modifies the existing list.
- Returns `None`.

---

## extend()

```python
a = [1, 2]
b = [3, 4]

a.extend(b)
```

Output:

```python
[1, 2, 3, 4]
```

`extend()` iterates over another iterable and appends each element individually.

Compare with:

```python
a.append(b)
```

Output:

```python
[1, 2, [3, 4]]
```

---

## insert()

```python
numbers.insert(1, 99)
```

Inserts an element at a specified index.

The existing elements are shifted to make room.

---

# Removing Elements

## pop()

```python
last = numbers.pop()
```

- Removes an element by index (default: last element).
- Returns the removed object.

---

## remove()

```python
numbers.remove(20)
```

Removes the **first occurrence** of the specified value.

Removes by **value**, not by position.

---

## clear()

```python
numbers.clear()
```

Removes all elements from the existing list.

The list object still exists; it simply becomes empty.

---

# Rearranging Elements

## sort()

```python
numbers.sort()
```

- Sorts the existing list.
- Modifies the list.
- Returns `None`.

---

## reverse()

```python
numbers.reverse()
```

Reverses the order of elements in the existing list.

---

# Inspecting a List

## index()

```python
numbers.index(20)
```

Returns the index of the first matching value.

Does not modify the list.

---

## count()

```python
numbers.count(2)
```

Returns how many times a value appears.

Does not modify the list.

---

# The sorted() Function

```python
sorted_numbers = sorted(numbers)
```

Unlike `sort()`, `sorted()`:

- returns a **new sorted list**,
- leaves the original list unchanged.

---

# Summary

| Method | Modifies List | Returns |
|---------|---------------|----------|
| append() | Yes | None |
| extend() | Yes | None |
| insert() | Yes | None |
| pop() | Yes | Removed object |
| remove() | Yes | None |
| clear() | Yes | None |
| sort() | Yes | None |
| reverse() | Yes | None |
| index() | No | Index |
| count() | No | Count |
| sorted() | No | New sorted list |

---

# Key Takeaways

- Lists are mutable objects.
- Most list methods modify the existing list.
- Methods like `append()` and `sort()` return `None`.
- `pop()` is special because it returns the removed object.
- `append()` adds one object.
- `extend()` adds each element from another iterable.
- `sort()` modifies the list.
- `sorted()` returns a new list.
- Choose between modifying data and creating a new copy based on your application's requirements.