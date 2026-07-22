# Chapter 6.2 — `elif` Statements

## What is `elif`?

`elif` stands for **"else if"**. It allows a program to check another condition only if the previous condition was `False`.

It is useful when there are multiple possible outcomes, but only one should be executed.

## Syntax

```python
if condition1:
    # Code block

elif condition2:
    # Code block

elif condition3:
    # Code block
```

Python evaluates the conditions from top to bottom. Once a condition is `True`, its block is executed and the remaining `elif` statements are skipped.

## Why Use `elif` Instead of Multiple `if` Statements?

Using multiple `if` statements may cause more than one block to execute.

```python
if score >= 90:
    print("Excellent")

elif score >= 75:
    print("Very Good")

elif score >= 50:
    print("Pass")
```

This ensures that only one grade is printed.

## Execution Flow

1. Evaluate the first condition.
2. If it is `True`, execute its block and stop checking.
3. If it is `False`, evaluate the next `elif`.
4. Continue until a condition is `True` or no conditions remain.

## Best Practices

* Arrange conditions from most specific to least specific.
* Avoid unnecessary upper bounds when earlier conditions already exclude them.
* Keep conditions simple and readable.

## Common Mistakes

* Using multiple `if` statements when only one result is expected.
* Placing broader conditions before more specific ones.
* Forgetting the colon (`:`).
* Incorrect indentation.

## Key Takeaways

* `elif` allows a program to choose between multiple conditions.
* Only the first matching condition is executed.
* The order of conditions matters.
* Earlier conditions influence which later conditions are evaluated.
