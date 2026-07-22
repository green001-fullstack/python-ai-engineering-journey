# Chapter 6.3 — `else` Statements

## What is `else`?

An `else` statement defines the default block of code that runs when all preceding `if` and `elif` conditions evaluate to `False`.

Unlike `if` and `elif`, `else` does not have a condition.

## Syntax

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

## How Python Executes an `if-elif-else` Chain

1. Evaluate the `if` condition.
2. If it is `True`, execute its block and skip the rest.
3. If it is `False`, evaluate each `elif` in order.
4. Execute the first matching `elif` and skip the remaining branches.
5. If no condition matches, execute the `else` block.

## Example

```python
marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 70:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## Best Practices

* Use `else` for the default or fallback case.
* Keep conditions ordered from most specific to least specific.
* Use `>=` or `<=` carefully based on the requirement.
* Avoid unnecessary conditions inside `else`.

## Common Mistakes

* Writing a condition after `else`.
* Forgetting the colon (`:`).
* Incorrect indentation.
* Using `>` instead of `>=` when boundary values should be included.

## Key Takeaways

* `else` runs only if every previous condition is `False`.
* An `if` chain can have only one `else`.
* `else` always comes last.
* `if`, `elif`, and `else` together allow programs to make complete decisions.
