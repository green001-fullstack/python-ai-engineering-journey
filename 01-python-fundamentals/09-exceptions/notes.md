# Python Exceptions — Why They Exist

## What Is an Exception?

An exception is a Python object representing an abnormal situation that interrupts the normal execution of a program.

Exceptions are objects, meaning they have:

- a type
- associated data (such as an error message)
- behavior inherited from their class

---

## Why Not Return Special Values?

Without exceptions, every function would need to return special values such as `None` or `-1` to indicate failure.

The caller would then have to manually check every result:

```python
result = load_model()
if result is None:
    ...
```

This quickly leads to repetitive and cluttered code.

Exceptions allow failures to propagate automatically until they reach code that knows how to handle them.

---

## Common Exceptions

| Exception | Meaning |
|-----------|---------|
| `ValueError` | Correct type, invalid value |
| `TypeError` | Wrong object type |
| `IndexError` | Invalid list or tuple index |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | Requested file does not exist |
| `ZeroDivisionError` | Division by zero |

---

## Raising Exceptions

Programs can raise their own exceptions when they detect invalid states.

```python
raise ValueError("Age cannot be negative")
```

This immediately interrupts normal execution.

---

## Software Engineering Principles

Exceptions separate responsibilities.

A function should:

- perform its task
- raise an exception if it cannot complete successfully

The caller decides how to respond.

This keeps code modular and easier to maintain.

---

# Key Takeaways

- Exceptions are Python objects.
- They represent abnormal situations.
- They interrupt normal execution.
- They are preferable to returning special error values in many cases.
- Raising an exception communicates failure clearly while allowing higher-level code to decide how to recover.