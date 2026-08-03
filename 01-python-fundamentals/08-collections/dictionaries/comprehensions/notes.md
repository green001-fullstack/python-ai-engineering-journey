# Python Dictionaries — Iteration & Comprehensions

## Iterating Over Keys

By default, iterating over a dictionary returns its keys.

```python
student = {
    "name": "Sarah",
    "age": 20
}

for key in student:
    print(key)
```

Output:

```
name
age
```

This is equivalent to:

```python
for key in student.keys():
    print(key)
```

---

## Iterating Over Values

Use `values()` when you only need the values.

```python
for value in student.values():
    print(value)
```

Output:

```
Sarah
20
```

---

## Iterating Over Keys and Values

Use `items()` to iterate over both keys and values.

```python
for key, value in student.items():
    print(key, value)
```

Conceptually, `items()` returns tuples:

```python
("name", "Sarah")
("age", 20)
```

Python automatically unpacks each tuple into `key` and `value`.

---

## Dictionary Comprehensions

Dictionary comprehensions create new dictionaries.

```python
numbers = [1, 2, 3]

squares = {
    n: n * n
    for n in numbers
}
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9
}
```

---

## Filtering

Dictionary comprehensions can include conditions.

```python
squares = {
    n: n * n
    for n in numbers
    if n % 2 == 0
}
```

Result:

```python
{
    2: 4
}
```

---

## Transforming Existing Dictionaries

```python
prices = {
    "Rice": 5000,
    "Beans": 3000
}

new_prices = {
    item: price * 2
    for item, price in prices.items()
}
```

---

# When to Use Comprehensions

Use dictionary comprehensions when they make the code simpler and more readable.

If the transformation becomes complex, a regular `for` loop is often easier to understand and maintain.

---

# Key Takeaways

- Iterating over a dictionary returns keys by default.
- `values()` iterates over values.
- `items()` returns key-value tuples.
- Python automatically unpacks tuples in `for key, value in ...`.
- Dictionary comprehensions build new dictionaries concisely.
- Readability should always guide the choice between a comprehension and a loop.