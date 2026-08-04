# Python Exceptions — Best Practices

## Catch Specific Exceptions

Prefer:

```python
try:
    data = open("data.csv")
except FileNotFoundError:
    print("File not found.")
```

Avoid:

```python
except Exception:
```

or

```python
except:
```

Specific exception handling makes programs easier to understand and debug.

---

## Only Catch Exceptions You Can Handle

Ask yourself:

> Can my program recover from this?

If yes:

Catch the exception.

If not:

Allow it to propagate.

Example:

```python
try:
    age = int(input())
except ValueError:
    print("Please enter a valid number.")
```

This is recoverable.

Example:

```python
except MemoryError:
```

Usually not recoverable.

---

## Avoid `except: pass`

```python
try:
    process()
except:
    pass
```

This silently ignores errors and can hide serious bugs.

---

## Keep `try` Blocks Small

Small `try` blocks make it easier to determine:

- what failed,
- why it failed,
- and how to recover.

---

## Fail Fast

Detect invalid states as early as possible.

```python
if amount < 0:
    raise InvalidLoanAmountError(
        "Loan amount cannot be negative."
    )
```

Early failures are easier to diagnose and fix.

---

## Use `finally` for Cleanup

```python
file = open("data.txt")

try:
    process(file)
finally:
    file.close()
```

`finally` guarantees cleanup regardless of success or failure.

---

## Re-raise When Necessary

```python
try:
    process()
except ValueError:
    log_error()
    raise
```

This allows higher-level code to decide how to recover.

---

# Professional Mental Checklist

Before catching an exception, ask:

1. Can I recover?
2. Am I hiding a programming bug?
3. Should this exception propagate?
4. Is there a more specific exception to catch?

---

# Key Takeaways

- Catch only what you can handle.
- Prefer specific exception types.
- Keep `try` blocks focused.
- Never silently ignore important errors.
- Use exceptions to communicate abnormal situations clearly.