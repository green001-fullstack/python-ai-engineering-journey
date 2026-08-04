# Understanding `__init__` in Python

## What is `__init__`?

`__init__` is a special method that initializes a newly created object.

Python automatically calls it immediately after creating an instance.

Example:

```python
class Applicant:

    def __init__(self, name):
        self.name = name
```

Creating an object:

```python
john = Applicant("John")
```

Conceptually becomes:

```python
Applicant.__init__(john, "John")
```

---

## Creation vs Initialization

Two separate steps occur:

1. Python creates a new object.
2. Python calls `__init__` to initialize that object.

The object already exists before `__init__` runs.

---

## Why Use `self.name = name`?

The parameter `name` is only a local variable.

```python
def __init__(self, name):
    name = name
```

stores nothing on the object.

Instead:

```python
self.name = name
```

stores the value as part of the object's state.

---

## Business Rules

`__init__` is an excellent place to enforce invariants.

Example:

```python
if name == "":
    raise ValueError("Name cannot be empty")
```

This prevents invalid objects from being created.

---

## Atlas Connection

Instead of:

```python
applicant = Applicant()

applicant.name = "John"
applicant.email = "john@example.com"
```

prefer:

```python
applicant = Applicant(
    "John",
    "john@example.com"
)
```

This guarantees every `Applicant` starts in a valid state.

---

# Key Takeaways

- `__init__` initializes newly created objects.
- Python calls it automatically.
- Objects exist before `__init__` runs.
- `self.attribute = value` stores data on the object.
- Initialization is a good place to enforce business rules.