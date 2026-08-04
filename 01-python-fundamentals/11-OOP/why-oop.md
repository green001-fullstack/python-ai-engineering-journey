# Why Object-Oriented Programming Exists

## The Problem

As software grows, separating data from the functions that operate on it becomes difficult to manage.

Example:

```python
applicant = {
    "name": "Sarah",
    "consent": False
}

grant_consent(applicant)
generate_trust_score(applicant)
update_email(applicant)
```

The data lives in one place, while the behavior is scattered across many functions.

As systems grow, this becomes difficult to understand and maintain.

---

## OOP's Solution

Object-Oriented Programming groups related **state** and **behavior** together.

Instead of:

```python
grant_consent(applicant)
```

we write:

```python
applicant.grant_consent()
```

The behavior clearly belongs to the object.

---

## Objects Mirror the Real World

Real-world objects have:

### Identity

Who the object is.

Examples:

- Applicant ID
- Loan ID

---

### State

The information the object currently holds.

Examples:

- Name
- Email
- Consent status
- Trust score

---

### Behavior

The actions the object can perform.

Examples:

- Grant consent
- Update email
- Request assessment

Behavior changes the object's state.

---

## Why OOP Helps

Grouping state and behavior together improves:

- Readability
- Maintainability
- Discoverability
- Team collaboration
- Large-scale software design

---

## Connection to DDD

Domain-Driven Design models business concepts as objects.

Example:

```text
Applicant
├── State
│   ├── Name
│   ├── Email
│   └── Consent
│
└── Behavior
    ├── GrantConsent()
    ├── UpdateEmail()
    └── RequestAssessment()
```

DDD provides the design principles.

OOP provides the language features to implement those designs.

---

# Key Takeaways

- OOP was created to organize large software systems.
- Objects combine state and behavior.
- Every object has identity, state, and behavior.
- Python's built-in types (`list`, `dict`, `str`) are already objects.
- DDD and OOP complement each other.