# Python Exceptions — try, except, else, finally

## The `try` Block

The `try` block contains code that may raise an exception.

```python
try:
    age = int(input("Age: "))
```

If no exception occurs, execution continues normally.

If an exception occurs, Python immediately leaves the remaining code inside the `try` block.

---

## The `except` Block

The `except` block handles a matching exception.

```python
try:
    age = int(input())
except ValueError:
    print("Invalid age")
```

Only matching exceptions are handled.

If no matching handler exists, the exception continues propagating upward.

---

## Multiple Exception Handlers

Python checks `except` blocks from top to bottom.

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except FileNotFoundError:
    ...
```

The first matching handler is executed.

---

## The `else` Block

The `else` block runs only if the `try` block completes successfully.

```python
try:
    age = int(input())
except ValueError:
    print("Invalid")
else:
    print("Accepted")
```

---

## The `finally` Block

The `finally` block always executes, regardless of whether an exception occurs.

```python
file = open("data.txt")

try:
    data = file.read()
finally:
    file.close()
```

This is commonly used for cleanup tasks:

- Closing files
- Closing database connections
- Releasing network sockets
- Freeing resources

---

# Execution Flow

## Success

```
Enter try
      ↓
No exception
      ↓
Run else
      ↓
Run finally
      ↓
Continue program
```

## Exception Raised

```
Enter try
      ↓
Exception occurs
      ↓
Leave try immediately
      ↓
Find matching except
      ↓
Run finally
      ↓
Continue (if handled)
```

---

# Key Takeaways

- Exceptions immediately interrupt normal execution.
- Python skips the remaining statements in the `try` block after an exception.
- `except` handles matching exceptions.
- `else` runs only when no exception occurs.
- `finally` always runs and is the preferred place for cleanup.