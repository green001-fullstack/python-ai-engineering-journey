# Chapter 6.6 — `for` Loops

## What is a `for` Loop?

A `for` loop repeats a block of code for each item in a sequence. It is commonly used when the number of iterations is known or when iterating over collections like lists, strings, or ranges.

## Syntax

```python
for variable in iterable:
    # code block
```

## The `range()` Function

`range()` generates a sequence of numbers.

### 1. One Argument

```python
range(5)
```

Output:

```
0, 1, 2, 3, 4
```

### 2. Two Arguments

```python
range(1, 6)
```

Output:

```
1, 2, 3, 4, 5
```

### 3. Three Arguments

```python
range(2, 11, 2)
```

Output:

```
2, 4, 6, 8, 10
```

The third argument is called the **step**, which controls how much the value changes after each iteration.

## `for` vs `while`

### `for`

* Best when the number of repetitions is known.
* Python automatically handles the loop variable.

### `while`

* Best when repetition depends on a condition.
* You must manually initialize and update the loop variable.

## Common Mistakes

* Forgetting that the stop value in `range()` is excluded.
* Using unnecessary updates like `i += 1` inside a `for` loop.
* Incorrect indentation.
* Missing the colon (`:`).

## Key Takeaways

* `for` loops iterate over sequences.
* `range(stop)` starts at `0` and stops before `stop`.
* `range(start, stop)` includes the start but excludes the stop.
* `range(start, stop, step)` changes the increment between values.
* `for` loops are generally preferred over `while` loops when the number of iterations is known.
