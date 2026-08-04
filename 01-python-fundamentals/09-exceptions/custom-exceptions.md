# Python Exceptions — Raising and Custom Exceptions

## Raising Exceptions

Python allows developers to raise their own exceptions using the `raise` keyword.

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

Raising an exception immediately interrupts normal execution and begins searching for an exception handler.

---

## Why Raise Instead of Returning False?

Returning special values such as `False` or `None` hides information.

```python
if amount > balance:
    return False
```

Instead, exceptions clearly communicate the reason for failure.

```python
if amount > balance:
    raise ValueError("Insufficient balance")
```

---

## Creating Custom Exceptions

Applications often have business rules that deserve their own exception types.

```python
class ApplicantAlreadyRegistered(Exception):
    pass
```

```python
class ConsentNotGrantedError(Exception):
    pass
```

```python
class InvalidLoanAmountError(Exception):
    pass
```

These exceptions inherit from Python's `Exception` class.

---

## Why Use Custom Exceptions?

Custom exceptions:

- Express business rules clearly.
- Improve readability.
- Allow specific exception handling.
- Make logs easier to understand.
- Improve maintainability.

Instead of:

```python
raise ValueError("Loan amount invalid")
```

Prefer:

```python
raise InvalidLoanAmountError(
    "Loan amount cannot be negative."
)
```

---

## Exception Hierarchy

```
BaseException
      │
 Exception
      │
 ├── ValueError
 ├── TypeError
 ├── FileNotFoundError
 ├── ApplicantAlreadyRegistered
 ├── ConsentNotGrantedError
 └── InvalidLoanAmountError
```

Custom exceptions become part of Python's exception hierarchy through inheritance.

---

# Key Takeaways

- Use `raise` to signal abnormal situations.
- Exceptions are objects.
- Custom exceptions model business rules.
- Prefer expressive exception names over generic exceptions when appropriate.
- Good exception design improves readability and maintainability.