# Algebraic Expressions

## 1. What Is an Algebraic Expression?

An algebraic expression is a combination of:

- numbers
- variables
- operators

Example:

```text
3x + 5
```

Components:

- `3` → coefficient
- `x` → variable
- `5` → constant
- `+` → operator

An expression does not make an equality claim.

---

## 2. Expression vs Equation

### Expression

```text
3x + 5
```

This represents a mathematical quantity.

### Equation

```text
3x + 5 = 20
```

This states that two expressions have equal values.

An equation can be solved for an unknown.

Example:

```text
3x + 5 = 20

3x = 15

x = 5
```

---

## 3. Variables

A variable represents a quantity.

Example:

```text
x = 10
```

Variables can represent different mathematical structures.

A scalar:

```text
x
```

A vector:

```text
x⃗
```

A matrix:

```text
X
```

This progression becomes important in linear algebra and machine learning.

---

## 4. Coefficients

In:

```text
7x
```

`7` is the coefficient of `x`.

It means:

```text
7 × x
```

---

## 5. Like Terms

Terms containing the same variable can be combined.

```text
3x + 5x = 8x
```

But:

```text
3x + 5y
```

cannot be simplified further because `x` and `y` may represent different quantities.

---

## 6. Distributive Property

The distributive property states:

```text
a(b + c) = ab + ac
```

Example:

```text
3(x + 4)

= 3x + 12
```

It also works in reverse:

```text
3x + 12

= 3(x + 4)
```

---

## 7. Exponents

An exponent indicates repeated multiplication.

```text
x² = x × x

x³ = x × x × x
```

For a non-zero number:

```text
x⁰ = 1
```

---

## 8. Order of Operations

Mathematical operations follow an order.

For example:

```text
2 + 3 × 4
```

Multiplication happens first:

```text
2 + 12 = 14
```

Parentheses can change the order:

```text
(2 + 3) × 4
```

```text
5 × 4 = 20
```

---

# Machine Learning Connection

A simple predictive model can be represented as:

```text
y = wx + b
```

Where:

- `x` → input
- `w` → coefficient/weight
- `b` → constant/intercept
- `y` → output/prediction

Example:

```text
y = 5x + 10
```

The `5` determines how strongly the input affects the output.

The `10` is the constant/intercept.

This simple equation is a foundation for understanding linear regression and eventually more complex machine-learning models.

---

# Pure Python

```python
x = 10
w = 3
b = 2

y = w * x + b

print(y)
```

Output:

```text
32
```

---

# Key Takeaways

- An expression represents a mathematical quantity.
- An equation states that two expressions are equal.
- A variable represents a quantity.
- A coefficient multiplies a variable.
- Like terms can be combined.
- The distributive property allows multiplication across parentheses.
- Exponents represent repeated multiplication.
- Mathematical expressions are the foundation of machine-learning formulas.