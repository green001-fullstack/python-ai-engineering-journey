# Understanding `self` in Python

## What is `self`?

`self` is the first parameter of an instance method.

It represents the object that the method is operating on.

Example:

```python
class Applicant:

    def greet(self):
        print("Hello")
```

Calling:

```python
john.greet()
```

is approximately equivalent to:

```python
Applicant.greet(john)
```

Python automatically passes the instance (`john`) as the first argument.

---

## Is `self` a Keyword?

No.

`self` is **not** a reserved keyword.

It is simply the naming convention for the first parameter of an instance method.

Although another name would work, using `self` is the accepted Python convention.

---

## Why is `self` Needed?

Imagine two applicants:

```python
john = Applicant()
mary = Applicant()
```

Both can call:

```python
grant_consent()
```

`self` tells the method **which specific object** it should operate on.

---

## Benefits

- Removes ambiguity.
- Allows one method to work with many objects.
- Keeps behavior attached to the object that owns it.
- Improves readability and maintainability.

---

## Key Takeaways

- Methods are functions defined inside a class.
- Python automatically passes the current object as the first argument.
- `self` is a convention, not a keyword.
- `self` refers to the current instance being operated on.