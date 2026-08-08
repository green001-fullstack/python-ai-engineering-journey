# Equations and Inequalities

## 1. Equations

An equation states that two mathematical expressions have equal values.

Example:

```text
2x + 3 = 11
```

Solving:

```text
2x = 8

x = 4
```

---

## 2. The Balance Principle

Whatever operation is performed on one side of an equation must also be performed on the other side.

Example:

```text
x + 5 = 12

x + 5 - 5 = 12 - 5

x = 7
```

Think of an equation as a mathematical balance.

---

## 3. Solving Equations

The general strategy is to **undo operations**.

Example:

```text
3x + 7 = 22

3x = 15

x = 5
```

The original operations were:

```text
x
↓
×3
↓
+7
```

To solve, reverse them:

```text
result
↓
-7
↓
÷3
↓
x
```

---

## 4. Variables on Both Sides

Example:

```text
5x + 2 = 2x + 14
```

Move variable terms to one side:

```text
3x + 2 = 14
```

Then:

```text
3x = 12

x = 4
```

---

# Inequalities

An inequality describes a relationship or range of possible values.

| Symbol | Meaning |
|---|---|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

Examples:

```text
x > 5
x < 5
x >= 5
x <= 5
```

---

## Solving Inequalities

Example:

```text
2x + 4 > 10

2x > 6

x > 3
```

---

## Negative Multiplication or Division

When multiplying or dividing an inequality by a negative number, reverse the inequality sign.

Example:

```text
-2x > 6

x < -3
```

The sign changes from:

```text
>
```

to:

```text
<
```

This happens because multiplying or dividing by a negative number reverses the order on the number line.

---

# Number Line Interpretation

```text
x > 3
```

means every number greater than 3.

```text
x >= 3
```

means every number greater than or equal to 3.

The difference is whether the boundary value is included.

---

# Python Connection

Mathematical equality:

```text
x = 10
```

is represented differently in Python.

### Assignment

```python
x = 10
```

Assigns `10` to `x`.

### Equality comparison

```python
x == 10
```

Checks whether `x` is equal to `10`.

---

## Python Inequalities

Mathematical:

```text
x > 5
```

Python:

```python
x > 5
```

Mathematical:

```text
x >= 5
```

Python:

```python
x >= 5
```

Python also supports chained comparisons.

Mathematical:

```text
0 <= x <= 100
```

Python:

```python
0 <= x <= 100
```

---

# AI / Machine Learning Connection

Equations describe mathematical relationships.

For example:

```text
y = wx + b
```

can represent a simple predictive model.

Inequalities can represent constraints.

For example:

```text
x >= 0
```

can represent a requirement that a quantity cannot be negative.

More generally, optimization problems can contain:

```text
Minimize f(x)

subject to:

g(x) <= 0

h(x) = 0
```

This idea becomes important in machine-learning optimization.

---

# Engineering Example

Suppose Atlas requires a loan amount to be greater than zero.

Mathematical rule:

```text
loanAmount > 0
```

Python validation:

```python
if loan_amount <= 0:
    raise ValueError("Loan amount must be greater than zero")
```

The mathematical inequality describes the business rule.

The Python code enforces it.

---

# Key Takeaways

- An equation expresses equality.
- Solving an equation means finding values that make it true.
- Operations must preserve equality on both sides.
- Inequalities describe ranges of possible values.
- Multiplying or dividing an inequality by a negative reverses its sign.
- Python uses `=` for assignment.
- Python uses `==` for equality comparison.
- Mathematical constraints can become software validation rules.
- Equations and inequalities are foundations for optimization.