# Chapter 6.9 — `pass`

## What is `pass`?

The `pass` statement is a null operation. It tells Python to do nothing and is commonly used as a placeholder where code will be added later.

## Syntax

```python
pass
```

## Why Use `pass`?

Python requires every code block to contain at least one statement. If a block is not yet implemented, `pass` prevents syntax errors while allowing the program to run.

## Examples

### `pass` in an `if` Statement

```python
if True:
    pass
```

### `pass` in a `for` Loop

```python
for i in range(5):
    pass
```

### `pass` in a `while` Loop

```python
count = 1

while count <= 3:
    pass
    count += 1
```

## `pass` vs `break` vs `continue`

| Statement  | Purpose                                                       |
| ---------- | ------------------------------------------------------------- |
| `pass`     | Do nothing.                                                   |
| `continue` | Skip the rest of the current iteration and continue the loop. |
| `break`    | Exit the loop immediately.                                    |

## Common Uses

* Placeholder for future code.
* Creating empty functions or classes during development.
* Building program structure before implementation.

## Key Takeaways

* `pass` does not stop a loop.
* `pass` does not skip an iteration.
* `pass` simply allows the program to continue.
* It is mainly used as a placeholder during development.
