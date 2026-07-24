# Python Functions — The LEGB Rule

## Overview

Whenever Python encounters a variable name, it follows a fixed search order to determine which object that name refers to.

This search order is called the **LEGB Rule**.

```
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

Python stops searching as soon as it finds the first matching name.

---

# The Four Scopes

## Local (L)

The current function's namespace.

```python
def greet():
    message = "Hello"
    print(message)
```

Search:

```
Local
↓

Found
```

---

## Enclosing (E)

The namespace of the surrounding function.

```python
def outer():
    name = "Go"

    def inner():
        print(name)

    inner()
```

Search inside `inner()`:

```
Local
↓

Enclosing
↓

Found
```

---

## Global (G)

Names defined outside every function.

```python
country = "Nigeria"

def show():
    print(country)
```

Search:

```
Local
↓

Global
↓

Found
```

---

## Built-in (B)

Python's predefined names.

Examples:

- print
- len
- input
- int
- float
- list
- dict
- type
- sum
- max
- min

Example:

```python
print("Hello")
```

Search:

```
Local
↓

Enclosing
↓

Global
↓

Built-in
↓

Found
```

---

# Python Stops at the First Match

```python
x = 10

def demo():
    x = 20
    print(x)
```

Search:

```
Local

↓

Found

Stop
```

Output

```
20
```

The global variable is never considered.

---

# Name Lookup Is an Algorithm

Python does not search randomly.

For every variable name, Python performs:

```
1. Local
2. Enclosing
3. Global
4. Built-in
```

The first successful lookup wins.

---

# Why This Design?

Searching from the most specific scope to the most general scope allows functions to have their own local variables without interfering with the rest of the program.

It also makes large applications easier to read and maintain.

---

# Common Misconceptions

❌ Python searches the global scope first.

✔ Local scope is always searched first.

---

❌ Enclosing means the function that called me.

✔ Enclosing means the function where this function was **defined**.

---

❌ Python continues searching after finding a name.

✔ Python stops immediately after the first successful lookup.

---

# Key Ideas

- LEGB is Python's name lookup algorithm.
- Variable lookup follows a fixed order.
- The first matching name is used.
- Local variables have the highest priority.
- Built-in names are searched last.

---

# Connections

## Builds On

- Variables are names bound to objects.
- Names live in namespaces.
- Scope determines where names are visible.

## Prepares For

- Closures
- Decorators
- `global`
- `nonlocal`
- Recursion

Understanding LEGB is essential for predicting how Python resolves variable names in nested functions and advanced language features.