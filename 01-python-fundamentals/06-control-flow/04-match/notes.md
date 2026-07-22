# Chapter 6.4 — `match` Statement

## What is `match`?

The `match` statement is used to compare a single value against multiple possible cases. It provides a cleaner alternative to long `if-elif` chains when checking one variable against fixed values.

## Syntax

```python
match variable:
    case value1:
        # code

    case value2:
        # code

    case _:
        # default case
```

## How It Works

1. Python evaluates the value after `match`.
2. It compares that value with each `case` from top to bottom.
3. The first matching `case` is executed.
4. The remaining cases are skipped.
5. If no case matches, `case _:` acts as the default case.

## Example

```python
operator = "+"

match operator:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")
    case _:
        print("Invalid operation")
```

## When to Use `match`

Use `match` when:

* Comparing one variable against several fixed values.
* Creating menus or command handlers.
* Handling predefined options such as days, commands, or operators.

## When Not to Use `match`

Do not use `match` for:

* Numeric ranges (`score >= 90`)
* Comparisons (`age > 18`)
* Complex logical expressions (`age >= 18 and has_ticket`)

Use `if-elif-else` instead.

## Common Mistakes

* Forgetting the colon (`:`).
* Forgetting the `case` keyword.
* Omitting quotation marks around string values.
* Forgetting the wildcard `case _:` for unmatched values.

## Key Takeaways

* `match` compares one value against multiple fixed cases.
* Only one matching `case` executes.
* `case _:` is the default branch, similar to `else`.
* `match` is best suited for fixed-value comparisons, not conditions or ranges.
