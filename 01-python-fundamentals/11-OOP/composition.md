# Composition in Python

## What is Composition?

Composition is the practice of building a larger object by combining it with other objects.

It represents a **"has-a"** relationship.

Examples:

- Applicant has an EmailAddress.
- Applicant has a PhoneNumber.
- Applicant has a Consent.
- Car has an Engine.
- LoanApplication has an Applicant.

---

## Composition vs Inheritance

Inheritance represents an **"is-a"** relationship.

```text
Dog IS an Animal
Applicant IS a Person
```

Composition represents a **"has-a"** relationship.

```text
Applicant HAS an EmailAddress
Car HAS an Engine
```

---

## Example

```python
class EmailAddress:

    def __init__(self, value):
        self.value = value


class Applicant:

    def __init__(self, email):
        self.email = email
```

Now:

```python
email = EmailAddress("john@example.com")

john = Applicant(email)
```

The Applicant contains an EmailAddress object.

---

## Why Composition?

Composition reduces coupling.

Each component can manage its own responsibility.

For example:

```text
Applicant
    |
    └── PhoneNumber
            |
            ├── validation
            ├── normalization
            └── formatting
```

The Applicant does not need to understand all the details of phone-number processing.

---

## Composition and Single Responsibility

Composition works naturally with the Single Responsibility Principle.

Instead of putting everything inside Applicant:

```python
class Applicant:

    # email validation
    # phone validation
    # consent logic
    # financial profile logic
    # assessment logic
```

we can separate responsibilities:

```text
Applicant
    |
    ├── EmailAddress
    ├── PhoneNumber
    ├── Consent
    └── FinancialProfile
```

Each component is responsible for its own behavior.

---

## Why Favor Composition Over Inheritance?

Deep inheritance hierarchies can become fragile.

For example:

```text
Person
  |
Employee
  |
LoanOfficer
  |
SeniorLoanOfficer
  |
RegionalLoanOfficer
```

A change near the top can affect many classes below it.

Composition avoids much of this tight coupling.

---

## Atlas Example

The Applicant aggregate can be composed of several domain objects:

```text
Applicant
    |
    ├── EmailAddress
    ├── PhoneNumber
    ├── Consent
    └── FinancialProfile
```

This allows each object to protect its own rules.

For example:

```python
applicant.phone_number.validate()
```

The Applicant does not need to implement every phone-number rule itself.

---

# Key Takeaways

- Composition represents a **has-a** relationship.
- Inheritance represents an **is-a** relationship.
- Composition reduces coupling.
- Composition supports the Single Responsibility Principle.
- Components can evolve independently.
- Modern software design often favors composition over deep inheritance hierarchies.