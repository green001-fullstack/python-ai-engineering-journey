# Chapter 7.7 — Lambda Functions

## What is a Lambda Function?

A lambda function is a small, anonymous function used for short operations.

Unlike a normal function, it is written in a single line and automatically returns the result of its expression.

## Syntax

```python
lambda parameters: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

## Multiple Parameters

Lambda functions can accept multiple parameters.

```python
add = lambda a, b: a + b

print(add(10, 5))
```

Output:

```text
15
```

## Conditional Expressions

Lambda functions can also use conditional expressions.

```python
check_age = lambda age: "Adult" if age >= 18 else "Minor"
```

## When to Use Lambda

Use lambda functions for:

* Small, simple operations
* One-time functions
* Passing functions to other functions (such as `map()` and `filter()`)

## When Not to Use Lambda

Avoid lambda functions when:

* The logic is complex.
* Multiple statements are required.
* A named function improves readability.

## Key Takeaways

* Lambda functions are anonymous functions.
* They consist of a single expression.
* The expression is returned automatically.
* They are useful for short, simple tasks.
* Use regular `def` functions for more complex logic.
