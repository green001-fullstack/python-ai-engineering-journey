# Special / Dunder Methods in Python

## What Are Dunder Methods?

"Dunder" means **double underscore**.

Examples:

```python
__init__
__str__
__repr__
__eq__
__len__
__add__
```

The more precise Python term is **special methods**.

They allow objects to participate in Python's built-in operations and language syntax.

---

## `__init__`

`__init__` initializes an object after it has been created.

```python
class Applicant:

    def __init__(self, name):
        self.name = name
```

When creating:

```python
applicant = Applicant("John")
```

the initialization logic runs automatically.

---

## `__str__`

`__str__` provides a human-readable representation of an object.

```python
class Applicant:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Applicant: {self.name} | Trust Score: {self.score}"
```

Now:

```python
print(applicant)
```

can produce:

```text
Applicant: John | Trust Score: 82
```

Use `__str__` when the representation should be easy for humans to read.

---

## `__repr__`

`__repr__` provides a developer-oriented representation of an object.

```python
class Applicant:

    def __init__(self, applicant_id, name, score):
        self.id = applicant_id
        self.name = name
        self.score = score

    def __repr__(self):
        return (
            f"Applicant("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"score={self.score!r})"
        )
```

Example:

```python
repr(applicant)
```

might produce:

```text
Applicant(id=1, name='John', score=82)
```

This is useful for debugging and inspecting objects.

---

## `__str__` vs `__repr__`

A useful mental model is:

```text
__str__  → human-friendly
__repr__ → developer-friendly
```

`__repr__` should ideally be unambiguous and, where practical, useful for recreating the object.

---

## `__eq__`

`__eq__` controls equality using:

```python
==
```

Example:

```python
class Applicant:

    def __init__(self, applicant_id):
        self.id = applicant_id

    def __eq__(self, other):

        if not isinstance(other, Applicant):
            return False

        return self.id == other.id
```

Now two different objects can be considered equal when they represent the same Applicant.

```python
a = Applicant(10)
b = Applicant(10)

print(a == b)
```

Output:

```text
True
```

---

## Identity vs Equality

Identity asks:

> "Are these the exact same object?"

```python
a is b
```

Equality asks:

> "Do these objects represent the same value or entity according to their equality rules?"

```python
a == b
```

These are different concepts.

---

## `__len__`

`__len__` allows an object to work with:

```python
len(object)
```

Example:

```python
class Portfolio:

    def __init__(self, applications):
        self.applications = applications

    def __len__(self):
        return len(self.applications)
```

Now:

```python
len(portfolio)
```

returns the number of applications.

---

## Operator Overloading

Special methods can define how operators work with custom objects.

For example:

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)
```

Now:

```python
a = Money(100)
b = Money(50)

c = a + b
```

works because Python uses:

```python
__add__
```

for the `+` operation.

---

## Common Special Methods

| Method | Purpose |
|---|---|
| `__init__` | Initialize an object |
| `__str__` | Human-readable representation |
| `__repr__` | Developer/debug representation |
| `__eq__` | Equality with `==` |
| `__len__` | Behavior of `len()` |
| `__add__` | Behavior of `+` |
| `__lt__` | Less-than comparison |
| `__gt__` | Greater-than comparison |
| `__iter__` | Make an object iterable |

You do not need to memorize all special methods.

The important idea is:

> Python provides special methods as hooks that allow objects to participate naturally in Python's language features.

---

## Atlas Example

Domain identity can influence equality.

If Applicant identity is determined by an ID:

```python
def __eq__(self, other):

    if not isinstance(other, Applicant):
        return False

    return self.id == other.id
```

Then equality reflects the domain concept of identity.

This allows Python's object model to work naturally with domain objects.

---

# Key Takeaways

- Dunder means double underscore.
- Special methods allow objects to interact with Python's built-in operations.
- `__str__` provides a human-friendly representation.
- `__repr__` provides a developer-friendly representation.
- `__eq__` defines equality behavior.
- `is` checks identity.
- `==` checks equality.
- Special methods allow operator overloading.
- You do not need to memorize every dunder method.