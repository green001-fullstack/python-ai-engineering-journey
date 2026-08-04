# Inheritance in Python

## What is Inheritance?

Inheritance allows one class to reuse the attributes and methods of another class.

It models an **"is-a"** relationship.

Example:

- Applicant is a Person.
- LoanOfficer is a Person.
- Dog is an Animal.

---

## Why Use Inheritance?

Without inheritance, common code must be copied into multiple classes.

This leads to:

- duplicated code,
- harder maintenance,
- inconsistent behavior,
- more bugs.

Inheritance lets common behavior be written once and reused.

---

## Basic Example

```python
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello")


class Applicant(Person):
    pass
```

Creating an object:

```python
john = Applicant("John")

john.greet()
```

Output:

```
Hello
```

Although `Applicant` does not define `greet()`, it inherits it from `Person`.

---

## Adding Child Behavior

A child class can define its own methods.

```python
class Applicant(Person):

    def request_assessment(self):
        print("Assessment requested")
```

The child now has:

- inherited behavior,
- its own specialized behavior.

---

## Overriding Methods

A child can replace a parent's implementation.

```python
class Person:

    def describe(self):
        print("Person")


class Applicant(Person):

    def describe(self):
        print("Applicant")
```

Calling:

```python
john.describe()
```

prints:

```
Applicant
```

---

## Using `super()`

When a child has its own `__init__`, it should usually call the parent's initializer.

```python
class Applicant(Person):

    def __init__(self, name, score):
        super().__init__(name)
        self.score = score
```

This lets each class initialize the part of the object it owns.

---

## When to Use Inheritance

Use inheritance only when there is a genuine **is-a** relationship.

Examples:

- Applicant → Person
- LoanOfficer → Person
- Dog → Animal

Do **not** use inheritance for **has-a** relationships.

Example:

An Applicant **has an** EmailAddress.

An Applicant **has a** Consent.

These are composition relationships.

---

# Key Takeaways

- Inheritance promotes code reuse.
- It models **is-a** relationships.
- Child classes inherit attributes and methods from parent classes.
- `super()` lets the parent initialize its own state.
- Avoid inheritance when the relationship is not naturally "is-a".