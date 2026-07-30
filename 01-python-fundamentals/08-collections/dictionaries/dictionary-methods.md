# Python Dictionaries — Common Methods

## `get()`

Safely retrieves the value associated with a key.

```python
user.get("email")
```

Returns `None` if the key does not exist.

You can also provide a default value:

```python
user.get("email", "Not Provided")
```

### When to use

Use `get()` when the key is optional and your program should continue even if the key is missing.

---

## `keys()`

Returns a live view of all dictionary keys.

```python
student.keys()
```

Example:

```
name
age
course
```

---

## `values()`

Returns a live view of all dictionary values.

```python
student.values()
```

Example:

```
Sarah
20
Dentistry
```

---

## `items()`

Returns a view of key-value pairs as tuples.

```python
student.items()
```

Example:

```python
("name", "Sarah")
("age", 20)
```

This is commonly used with tuple unpacking:

```python
for key, value in student.items():
    print(key, value)
```

---

## `pop()`

Removes a key from the dictionary and returns its value.

```python
age = student.pop("age")
```

After:

```python
student = {
    "name": "Sarah"
}
```

`age` contains:

```python
20
```

---

## `update()`

Adds new key-value pairs or overwrites existing ones.

```python
user.update({
    "age": 25,
    "city": "Lagos"
})
```

Useful for merging new information into an existing dictionary.

---

## `clear()`

Removes every key-value pair from a dictionary.

```python
cart.clear()
```

Result:

```python
{}
```

The dictionary object still exists; it is simply empty.

---

# Dictionary Views

The objects returned by `keys()`, `values()`, and `items()` are **views**, not copies.

If the dictionary changes, the views automatically reflect those changes.

---

# Key Takeaways

- Use `[]` when a key **must** exist.
- Use `get()` when a key is optional.
- `items()` returns tuples.
- `pop()` removes a key and returns its value.
- `update()` merges or overwrites data.
- Dictionary views stay synchronized with the dictionary.