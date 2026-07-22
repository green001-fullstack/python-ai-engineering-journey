# Chapter 6.1 — `if` Statements

## What is Control Flow?

Control flow is the order in which a program executes its statements. By default, Python executes code sequentially (top to bottom). `if` statements allow a program to make decisions and execute code conditionally.

## What is an `if` Statement?

An `if` statement executes a block of code only when its condition evaluates to `True`.

### Syntax

```python
if condition:
    # code block
```

* The condition must evaluate to `True` or `False`.
* A colon (`:`) is required after the condition.
* The code block must be indented.

## Example

```python
age = 20

if age >= 18:
    print("Adult")
```

## How Python Executes an `if`

1. Evaluate the condition.
2. If the result is `True`, execute the indented block.
3. If the result is `False`, skip the block and continue with the next statement.

## Nested `if`

An `if` statement can be placed inside another `if` statement.

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed")
```

## Common Mistakes

* Forgetting the colon (`:`).
* Incorrect indentation.
* Using `=` instead of `==`.
* Writing `Print()` instead of `print()`.
* Using the wrong comparison operator (`>=` vs `<=`).

## Key Takeaways

* `if` statements enable decision-making.
* Conditions always evaluate to `True` or `False`.
* Python uses indentation to define code blocks.
* A block only runs when its condition is `True`.
* Nested `if` statements allow multiple levels of decision-making.
