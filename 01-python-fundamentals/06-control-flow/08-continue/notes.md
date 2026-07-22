# Chapter 6.8 — `continue`

## What is `continue`?

The `continue` statement skips the rest of the current iteration of a loop and immediately moves to the next iteration.

Unlike `break`, it does **not** end the loop.

## Syntax

```python
for item in iterable:
    if condition:
        continue
    # remaining code
```

## How `continue` Works

1. The loop starts an iteration.
2. If `continue` is encountered, the remaining statements in that iteration are skipped.
3. The loop proceeds to the next iteration.
4. The loop ends naturally when there are no more iterations.

## Example

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

## `continue` vs `break`

### `continue`

* Skips the current iteration.
* Continues with the next iteration.

### `break`

* Stops the loop immediately.
* No further iterations are executed.

## Common Uses

* Ignoring invalid data.
* Skipping unwanted values.
* Filtering input during iteration.

## Common Mistakes

* Forgetting to print or process values after `continue`.
* Confusing `continue` with `break`.
* Using `continue` before updating the loop variable in a `while` loop, which can cause an infinite loop.

## Key Takeaways

* `continue` skips only the current iteration.
* The loop continues running after `continue`.
* In `while` loops, always ensure the loop variable is updated before `continue`.
* `continue` is useful for filtering data while iterating.
