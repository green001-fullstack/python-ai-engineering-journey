# Encapsulation in Python

## What is Encapsulation?

Encapsulation is the principle of **protecting an object's state by controlling how it can be changed**.

Its primary goal is **not** to hide data, but to ensure that an object always remains in a valid state by enforcing its own business rules.

---

## The Problem Without Encapsulation

Suppose we have:

```python
class Applicant:

    def __init__(self):
        self.consent = False
```

Any code can do:

```python
applicant.consent = True
```

This changes the object's state directly.

The problem is that important business rules may be skipped.

For example:

- Was the applicant shown the consent form?
- Was the consent timestamp recorded?
- Was an audit log created?
- Was a domain event published?

Simply changing a variable cannot answer these questions.

---

## A Better Design

Instead of exposing state directly:

```python
applicant.consent = True
```

provide a business operation:

```python
applicant.grant_consent()
```

Now the object decides whether the operation is valid.

Example:

```python
class Applicant:

    def grant_consent(self):
        if self.consent:
            raise Exception("Consent already granted")

        self.consent = True
```

Every consent change now follows the same business rules.

---

## Encapsulation Protects Invariants

An invariant is a business rule that must always remain true.

Example:

- An applicant cannot grant consent twice.
- An applicant cannot request an assessment before granting consent.
- A bank account balance cannot become negative.
- An email address cannot be empty.

Encapsulation ensures these rules are enforced inside the object itself.

---

## Private Attributes

Python supports naming conventions for internal attributes.

```python
self._email
```

A single underscore means:

> "This is intended for internal use."

Double underscores trigger name mangling:

```python
self.__email
```

This makes accidental access more difficult.

However, private attributes alone are **not** encapsulation.

Encapsulation is about controlling behavior, not merely hiding variables.

---

## Atlas Example

Poor design:

```python
applicant.trust_score = 95
```

Better design:

```python
applicant.generate_trust_score(financial_profile)
```

The second approach allows the object to:

- validate financial evidence,
- perform fraud checks,
- calculate the score,
- generate explanations,
- publish domain events,
- maintain audit history.

---

## Benefits of Encapsulation

- Protects business rules.
- Prevents invalid object states.
- Keeps logic in one place.
- Improves maintainability.
- Makes software easier to understand.
- Supports Domain-Driven Design aggregates.

---

# Key Takeaways

- Encapsulation protects an object's state.
- Objects should expose behaviors, not unrestricted state changes.
- Business rules belong inside the object.
- Private attributes support encapsulation but are not encapsulation itself.
- Well-encapsulated objects are easier to maintain and harder to misuse.