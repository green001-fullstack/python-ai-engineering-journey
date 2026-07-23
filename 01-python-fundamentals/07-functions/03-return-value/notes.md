# Python Functions — Return Values

## Overview

Functions often need to send results back to the code that called them.

Python does this using the `return` statement.

A return value is the output produced by a function after it has finished processing its input.

---

# Input → Processing → Output

A function can be viewed as a machine.

```
Input
   │
   ▼
+------------------+
|    Function      |
|                  |
|  Processes Data  |
+------------------+
   │
   ▼
Output
```

Parameters receive input.

Return values produce output.

---

# print() vs return

These are completely different operations.

## print()

Displays information on the screen.

```python
def greet():
    print("Hello")
```

Output

```
Hello
```

Nothing useful is returned.

Python automatically returns `None`.

---

## return

Returns an object back to the caller.

```python
def greet():
    return "Hello"
```

The caller decides what to do with it.

```python
message = greet()

print(message)
```

Output

```
Hello
```

---

# What return Does

The `return` statement performs two actions.

1. Sends an object back to the caller.
2. Immediately stops function execution.

Example

```python
def example():
    print("One")
    return
    print("Two")
```

Output

```
One
```

The second print statement never executes.

---

# Function Calls Are Expressions

Suppose

```python
def double(x):
    return x * 2
```

Then

```python
double(10)
```

evaluates to

```
20
```

This means a function call can be used anywhere a value is expected.

```python
result = double(10)

print(double(10))

if double(10) > 15:
    print("Large")

answer = double(10) + 5
```

---

# Implicit Return

Every Python function returns something.

If no explicit return statement exists,

```python
def greet():
    print("Hello")
```

Python automatically behaves as though it were

```python
def greet():
    print("Hello")
    return None
```

---

# Returning Objects

Functions return object references.

Example

```python
def create_name():
    return "Oladimeji"

name = create_name()
```

Memory conceptually

```
"Oladimeji"
      ▲
      │
    name
```

The returned object becomes bound to the caller's variable.

---

# Why return Is Better Than print

Using print()

```python
def calculate_score():
    print(720)
```

The caller cannot reuse the score.

Using return

```python
def calculate_score():
    return 720
```

Now the score can be

- stored
- compared
- passed to another function
- written to a database
- displayed to the user

---

# Common Misconceptions

❌ print() returns the printed value.

✔ print() displays information.

---

❌ return prints to the screen.

✔ return sends an object back to the caller.

---

❌ Functions without return return nothing.

✔ They automatically return None.

---

# Key Ideas

- Functions receive data through parameters.
- Functions send data back using return.
- A function call is an expression.
- return immediately ends the function.
- Every Python function returns a value.
- If no value is specified, Python returns None.

---

# Connections

## Builds On

- Variables
- Objects
- References
- Parameters
- Function Objects
- Immutable vs Mutable Objects

## Prepares For

- Scope
- LEGB Rule
- Recursion
- Closures
- Decorators

Understanding return values makes it much easier to understand recursive functions, higher-order functions, and decorators later in the course.