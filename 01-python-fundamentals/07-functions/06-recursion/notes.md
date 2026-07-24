# Python Functions — Recursion

## Overview

Recursion is a technique where a function solves a problem by calling itself on a **smaller version of the same problem** until it reaches a **base case**.

Every recursive function has two essential parts:

1. **Base Case** – the stopping condition.
2. **Recursive Case** – reduces the problem and calls the function again.

---

# The Two Ingredients

```python
def countdown(n):
    if n == 0:
        return          # Base Case

    print(n)
    countdown(n - 1)    # Recursive Case
```

The recursive case must always move toward the base case.

---

# The Call Stack

Each recursive call creates a new **stack frame**.

Example:

```text
countdown(3)

+---------------+
| countdown(3)  |
+---------------+

↓

+---------------+
| countdown(2)  |
+---------------+
| countdown(3)  |
+---------------+

↓

+---------------+
| countdown(1)  |
+---------------+
| countdown(2)  |
+---------------+
| countdown(3)  |
+---------------+

↓

+---------------+
| countdown(0)  |
+---------------+
| countdown(1)  |
+---------------+
| countdown(2)  |
+---------------+
| countdown(3)  |
+---------------+
```

When the base case is reached, the stack unwinds in reverse order.

---

# Every Call Has Its Own Local Scope

Each recursive call creates:

- A new local namespace.
- A new parameter binding.
- A new stack frame.

Even though every call uses the parameter `n`, each call has its own independent copy.

---

# Example: Factorial

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)
```

Execution:

```text
factorial(4)

↓

4 * factorial(3)

↓

4 * (3 * factorial(2))

↓

4 * (3 * (2 * factorial(1)))

↓

4 * (3 * (2 * 1))

↓

24
```

The recursive calls build the stack first.

The return values are computed while the stack unwinds.

---

# Common Mistakes

❌ Forgetting the base case.

Results in:

```text
RecursionError
```

---

❌ Not reducing the problem.

```python
countdown(n)
```

instead of

```python
countdown(n - 1)
```

The recursion never progresses.

---

❌ Thinking recursive calls share the same local variables.

Each call gets its own local namespace.

---

# Key Ideas

- Recursion solves smaller versions of the same problem.
- Every recursive function needs a base case.
- Every recursive call creates a new stack frame.
- The call stack grows until the base case is reached.
- Return values are produced as the stack unwinds.

---

# Connections

## Builds On

- Function calls
- Parameters
- Local scope
- LEGB
- Objects and references

## Used In

- Tree traversals
- Binary search trees
- Graph depth-first search
- Divide-and-conquer algorithms
- Parsing nested structures
