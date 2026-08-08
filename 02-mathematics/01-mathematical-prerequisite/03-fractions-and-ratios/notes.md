# Fractions and Ratios

## 1. Fractions

A fraction represents a part of a whole or a division.

```text
3/4
```

- `3` → numerator
- `4` → denominator

It can be interpreted as:

```text
3 parts out of 4
```

or:

```text
3 ÷ 4 = 0.75
```

---

## 2. Proper and Improper Fractions

Proper fraction:

```text
3/5
```

The numerator is smaller than the denominator.

Improper fraction:

```text
7/5
```

The numerator is greater than the denominator.

---

## 3. Equivalent Fractions

Different-looking fractions can represent the same value.

```text
1/2 = 2/4 = 5/10
```

Multiplying both numerator and denominator by the same non-zero value does not change the fraction's value.

---

## 4. Simplifying Fractions

Divide the numerator and denominator by their greatest common divisor.

Example:

```text
18/24
```

Both are divisible by 6:

```text
18 ÷ 6 = 3
24 ÷ 6 = 4
```

Therefore:

```text
18/24 = 3/4
```

---

## 5. Adding Fractions

Fractions with different denominators require a common denominator.

Example:

```text
1/2 + 1/3
```

Common denominator:

```text
6
```

Convert:

```text
1/2 = 3/6
1/3 = 2/6
```

Therefore:

```text
3/6 + 2/6 = 5/6
```

---

## 6. Multiplying Fractions

Multiply numerator by numerator and denominator by denominator.

```text
2/3 × 4/5

= 8/15
```

Always simplify if possible.

Example:

```text
2/3 × 3/5

= 6/15

= 2/5
```

---

## 7. Dividing Fractions

Dividing by a fraction is equivalent to multiplying by its reciprocal.

Example:

```text
3/4 ÷ 2/5
```

Flip the second fraction:

```text
3/4 × 5/2
```

Therefore:

```text
15/8
```

---

# Ratios

A ratio describes a relationship between quantities.

Example:

```text
80 approved
20 rejected
```

Ratio:

```text
80:20
```

Simplify:

```text
4:1
```

This means:

> For every 4 approved applications, there is 1 rejected application.

---

# Ratio vs Fraction

Suppose:

```text
80 approved
20 rejected
```

Ratio:

```text
80:20 = 4:1
```

Fraction of applications that were approved:

```text
80 / (80 + 20)

= 80/100

= 0.8
```

Percentage:

```text
0.8 × 100 = 80%
```

The ratio compares quantities.

The fraction can represent a part relative to the whole.

---

# Proportions

A proportion states that two ratios are equal.

```text
2/3 = 4/6
```

Example:

```text
x/5 = 6/10
```

Cross multiply:

```text
10x = 30

x = 3
```

---

# Fractions and Percentages

Percentages are fractions whose denominator is 100.

```text
25% = 25/100 = 1/4 = 0.25
```

```text
80% = 80/100 = 4/5 = 0.8
```

---

# Python

True division:

```python
7 / 2
```

returns:

```text
3.5
```

Floor division:

```python
7 // 2
```

returns:

```text
3
```

---

## Python Fractions

Python provides an exact Fraction type:

```python
from fractions import Fraction

x = Fraction(3, 4)

print(x)
```

Output:

```text
3/4
```

Convert to a floating-point number:

```python
float(x)
```

Output:

```text
0.75
```

---

# AI / Machine Learning Connection

Many ML metrics are ratios.

For example, accuracy:

```text
correct predictions / total predictions
```

If a model gets 90 out of 100 predictions correct:

```text
90/100 = 0.9 = 90%
```

---

# Normalization

Normalization can transform numerical values into a more manageable range.

Example:

```text
income = 400,000
maximum = 800,000
```

Normalized value:

```text
400,000 / 800,000 = 0.5
```

Instead of giving the model a feature with a large numerical magnitude, we can represent it using a smaller scaled value.

Different ML algorithms use different scaling techniques.

---

# Common Mistakes

### Adding fractions incorrectly

Incorrect:

```text
1/2 + 1/3 = 2/5
```

Correct:

```text
1/2 + 1/3 = 5/6
```

### Forgetting to simplify

```text
6/15
```

can be simplified to:

```text
2/5
```

### Confusing ratio and proportion

```text
4:1
```

is a ratio.

```text
4/5
```

could represent a proportion of a whole depending on context.

### Dividing by zero

```text
x/0
```

is undefined.

---

# Complexity

For ordinary fixed-size integers:

- Fraction addition → O(1)
- Fraction multiplication → O(1)
- GCD-based simplification → approximately O(log n)

Python integers have arbitrary precision, so actual computational cost increases with the number of digits.

---

# Key Takeaways

- A fraction can represent a part of a whole or division.
- The numerator is above the denominator.
- Equivalent fractions have the same value.
- Fractions can be simplified.
- Different-denominator fractions require a common denominator for addition/subtraction.
- Dividing by a fraction means multiplying by its reciprocal.
- Ratios compare quantities.
- Proportions express equivalent ratios.
- Percentages are fractions out of 100.
- ML metrics frequently use ratios.
- Normalization changes the scale of numerical features.