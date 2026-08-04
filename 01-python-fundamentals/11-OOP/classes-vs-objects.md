# Classes and Objects in Python

## What is a Class?

A class defines what kind of objects can be created.

It describes:

- The data (state) an object can hold.
- The behaviors (methods) an object can perform.

A class is itself an object in Python.

Example:

```python
class Applicant:
    pass
```

This creates one class object named `Applicant`.

---

## What is an Object?

An object (also called an instance) is a concrete realization of a class.

Objects are created by calling the class.

```python
john = Applicant()
```

`john` is an instance of the `Applicant` class.

---

## One Class, Many Objects

```python
class Applicant:
    pass

john = Applicant()
mary = Applicant()
```

Memory Conceptually:

```
Applicant Class Object

      ▲
      │
 Applicant

────────────────────

john ─────► Applicant Instance

mary ─────► Applicant Instance
```

The class exists once.

Multiple objects can be created from it.

---

## Everything is an Object

Examples:

```python
10
```

Instance of:

```python
int
```

```python
"Python"
```

Instance of:

```python
str
```

```python
[]
```

Instance of:

```python
list
```

Your own objects work the same way:

```python
Applicant()
```

creates an instance of the `Applicant` class.

---

## Key Takeaways

- A class defines a type of object.
- Objects are instances created from classes.
- One class can create many objects.
- Classes themselves are objects.
- Everything in Python is an object.