# Python Collections — Indexing and Slicing

## Overview

Lists allow elements to be accessed and modified using indexing and slicing.

Understanding the difference between the two is important because indexing returns a single object, while slicing creates a new list.

---

# Indexing

```python
numbers = [10, 20, 30]

x = numbers[1]
```

- Indexing returns the object referenced at the specified position.
- The returned value is not copied; its reference is copied.

Positive indices start from the beginning.

```
0   1   2
10 20 30
```

Negative indices start from the end.

```
-3  -2  -1
10  20  30
```

Example:

```python
numbers[-1]
```

returns:

```python
30
```

---

# Element Assignment

```python
numbers[1] = 99
```

This does **not** modify the integer `20`.

Instead, the list updates the reference stored at index `1` to point to the integer `99`.

The list object remains the same.

---

# Slicing

```python
numbers = [10, 20, 30, 40, 50]

part = numbers[1:4]
```

Result:

```python
[20, 30, 40]
```

Python reads this as:

- Start at index `1`.
- Stop before index `4`.

The stop index is **exclusive**.

---

# Slicing Creates a New List

Unlike indexing, slicing creates a new outer list.

```python
part = numbers[1:4]
```

The new list contains references to the same objects as the original list.

For immutable objects such as integers and strings, this sharing is safe.

For nested mutable objects, slicing behaves like a shallow copy.

---

# Slice Assignment

```python
numbers[1:3] = [100, 200]
```

This modifies the existing list by replacing the references stored in the selected slice.

---

# Deleting with Slices

```python
del numbers[1:3]
```

Removes the selected elements from the existing list.

---

# Key Takeaways

- Lists store references to objects.
- Indexing returns one referenced object.
- Slicing creates a new outer list.
- Slicing performs a shallow copy.
- Positive indices count from the beginning.
- Negative indices count from the end.
- Slice assignment modifies the existing list.
- The stop index in a slice is exclusive.