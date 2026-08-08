# Polymorphism in Python

## What is Polymorphism?

Polymorphism means that different objects can respond to the same operation in different ways.

The core idea is:

> **Same interface, different behavior.**

Example:

```python
class Dog:

    def speak(self):
        return "Woof"


class Cat:

    def speak(self):
        return "Meow"
```

Both objects provide:

```python
speak()
```

but they behave differently.

---

## Using Polymorphism

```python
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
```

Output:

```text
Woof
Meow
```

The loop does not need to know the specific type of each object.

It simply asks each object to perform:

```python
animal.speak()
```

---

## Duck Typing

Python often uses duck typing.

The idea is:

> If an object provides the behavior we need, we can use it.

Example:

```python
class Dog:

    def speak(self):
        return "Woof"


class Robot:

    def speak(self):
        return "Beep"
```

We can write:

```python
def make_speak(thing):
    return thing.speak()
```

The function doesn't need to know whether `thing` is a Dog or Robot.

It only requires that `thing` provide a `speak()` method.

---

## Polymorphism Without Inheritance

Inheritance is not required.

Completely unrelated classes can support the same operation:

```python
class Dog:

    def speak(self):
        return "Woof"


class Robot:

    def speak(self):
        return "Beep"
```

Both can participate in:

```python
def make_speak(thing):
    return thing.speak()
```

---

## Atlas Example

Suppose Atlas has several financial evidence sources:

```text
FinancialEvidenceSource

├── BankStatementSource
├── MobileMoneySource
└── TransactionAPISource
```

Each provides:

```python
fetch_transactions()
```

Instead of writing:

```python
if source_type == "bank":
    ...
elif source_type == "mobile_money":
    ...
elif source_type == "api":
    ...
```

we can write:

```python
def collect_transactions(source):
    return source.fetch_transactions()
```

Each source handles its own implementation.

---

## Benefits

Polymorphism can provide:

- less conditional logic,
- easier extension,
- reduced coupling,
- clearer code,
- easier testing,
- better separation of responsibilities.

---

## Open/Closed Principle

Polymorphism can help support the Open/Closed Principle:

> Software should be open for extension but closed for modification.

For example, we can add:

```python
class OpenBankingSource:

    def fetch_transactions(self):
        ...
```

without necessarily modifying:

```python
collect_transactions()
```

---

# Key Takeaways

- Polymorphism means different objects can respond differently to the same operation.
- Python frequently uses duck typing.
- Inheritance is not required.
- Polymorphism reduces conditional logic.
- Polymorphism makes systems easier to extend.