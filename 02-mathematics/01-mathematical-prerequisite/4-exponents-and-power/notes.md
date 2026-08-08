# Exponents and Powers

## 1. What Is an Exponent?

An exponent tells us how many times a base is multiplied by itself.

```text
2^4 = 2 × 2 × 2 × 2 = 16
```

For:

```text
7^3
```

- `7` is the base
- `3` is the exponent
- `7^3` is a power

---

## 2. Important Rules

### Power of 1

```text
x^1 = x
```

### Power of 0

For non-zero x:

```text
x^0 = 1
```

---

## 3. Multiplication of Powers

When multiplying powers with the same base, add the exponents.

```text
x^a × x^b = x^(a+b)
```

Example:

```text
3^2 × 3^4

= 3^6
```

---

## 4. Division of Powers

When dividing powers with the same base, subtract the exponents.

```text
x^a / x^b = x^(a-b)
```

Example:

```text
5^7 / 5^3

= 5^4
```

---

## 5. Power Raised to a Power

Multiply the exponents.

```text
(x^a)^b = x^(ab)
```

Example:

```text
(2^3)^2

= 2^6
```

---

## 6. Power of a Product

The exponent applies to each factor.

```text
(ab)^n = a^n b^n
```

Example:

```text
(2 × 3)^2

= 2^2 × 3^2

= 36
```

---

## 7. Negative Exponents

A negative exponent means reciprocal.

```text
x^(-n) = 1 / x^n
```

Example:

```text
2^(-2) = 1/4
```

---

## 8. Fractional Exponents

A fractional exponent represents a root.

```text
x^(1/n) = nth root of x
```

Examples:

```text
9^(1/2) = √9 = 3

8^(1/3) = ∛8 = 2
```

More generally:

```text
x^(m/n) = nth root of (x^m)
```

Example:

```text
8^(2/3)

= (∛8)^2

= 2^2

= 4
```

---

# Exponential Growth

An exponential function can grow extremely quickly.

```text
y = 2^x
```

Examples:

```text
2^1 = 2
2^2 = 4
2^3 = 8
2^10 = 1024
```

This is much faster than linear growth:

```text
y = 2x
```

---

# Computer Science Connection

Exponential complexity:

```text
O(2^n)
```

grows rapidly.

Examples:

```text
2^5  = 32
2^10 = 1,024
2^20 = 1,048,576
2^30 = 1,073,741,824
```

This is why exponential-time algorithms can become impractical as input size grows.

---

# AI / Machine Learning Connection

Exponentials appear throughout machine learning.

## Probability

Repeated independent probabilities can involve powers.

```text
0.8^5 = 0.32768
```

---

## Exponential Functions

Euler's number:

```text
e ≈ 2.71828
```

is fundamental to ML.

The sigmoid function is:

```text
σ(x) = 1 / (1 + e^(-x))
```

---

## Softmax

Softmax uses exponentials to transform model scores into normalized values:

```text
e^(z_i) / Σ e^(z_j)
```

The exponential amplifies differences between scores, and normalization makes the resulting values sum to 1.

---

# Python

Python uses:

```python
**
```

for exponentiation.

Example:

```python
2 ** 4
```

returns:

```text
16
```

Negative exponent:

```python
2 ** -1
```

returns:

```text
0.5
```

Fractional exponent:

```python
9 ** 0.5
```

returns:

```text
3.0
```

---

## Important Python Difference

```python
2 ** 3
```

is exponentiation.

```python
2 ^ 3
```

is bitwise XOR.

`^` is NOT the exponent operator in Python.

---

# Common Mistakes

### Mistake 1

```text
x^2 = x × 2
```

Incorrect.

```text
x^2 = x × x
```

---

### Mistake 2

Adding exponents for a power raised to a power.

Incorrect:

```text
(x^2)^3 = x^5
```

Correct:

```text
(x^2)^3 = x^6
```

---

### Mistake 3

Thinking negative exponents produce negative numbers.

Incorrect:

```text
2^-2 = -4
```

Correct:

```text
2^-2 = 1/4
```

---

### Mistake 4

Using `^` for exponentiation in Python.

Incorrect:

```python
2 ^ 3
```

Correct:

```python
2 ** 3
```

---

# Complexity

For fixed-size numbers, exponentiation can often be treated as constant-time in basic algorithm analysis.

However, arbitrary-precision arithmetic becomes more expensive as the number of digits grows.

For example:

```text
2^1,000,000
```

contains a very large number of digits.

Therefore, the computational cost depends partly on the size of the numbers being manipulated.

---

# Key Takeaways

- An exponent represents repeated multiplication.
- Multiplying powers with the same base → add exponents.
- Dividing powers with the same base → subtract exponents.
- Power raised to a power → multiply exponents.
- Negative exponent → reciprocal.
- Fractional exponent → root.
- Exponential growth is much faster than linear growth.
- Exponentials appear heavily in probability and ML.
- Python uses `**` for exponentiation.
- Python uses `^` for bitwise XOR.