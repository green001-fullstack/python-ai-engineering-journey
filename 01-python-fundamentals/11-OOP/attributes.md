# Attributes in Python

## What are Attributes?

Attributes are data stored on an object or on a class.

They represent the **state** of an object.

---

## Instance Attributes

Instance attributes belong to individual objects.

Example:

```python
class Applicant:

    def __init__(self, name):
        self.name = name
```

Each object has its own value.

```python
john = Applicant("John")
mary = Applicant("Mary")
```

Changing John's name does not affect Mary's.

---

## Class Attributes

Class attributes belong to the class itself.

Example:

```python
class Applicant:

    country = "Nigeria"
```

Every instance can access this shared value.

---

## Choosing Between Them

Use an **instance attribute** when each object should have its own value.

Examples:

- name
- email
- phone_number
- consent
- trust_score

Use a **class attribute** when every object shares the same value.

Examples:

- organization_name
- max_trust_score
- country (if the application is country-specific)

---

## Avoid Mutable Class Attributes

Avoid:

```python
class Applicant:
    loans = []
```

All instances share the same list.

Instead:

```python
class Applicant:

    def __init__(self):
        self.loans = []
```

Each object gets its own independent list.

---

# Key Takeaways

- Instance attributes belong to objects.
- Class attributes belong to the class.
- Instance attributes are independent.
- Mutable class attributes often cause shared-state bugs.
- Choose attributes based on business ownership, not convenience.
