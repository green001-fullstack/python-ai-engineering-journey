Floats

Let's start with a question.

What is this?

3.14

Most people answer:

"A decimal number."

That's true, but as we've learned, Python sees something more specific.

It sees:

A float object.

Just like integers:

42

creates an int object,

this:

3.14

creates a float object.

Floats Are Objects Too
x = 3.14

Conceptually:

Namespace

x
│
▼
Reference
│
▼

Object

Type: float

Value: 3.14

The object model hasn't changed.

Only the object's type has.

Why Do We Need Floats?

Integers represent whole numbers:

5
100
-42

But what about:

3.14
2.718
98.6
0.5

These contain fractional parts.

Integers cannot represent them.

So Python provides another object type:

float
Are Floats Immutable?

Let's test our reasoning.

x = 3.14

Later:

x = x + 1

Did Python modify the existing float object?

No.

Exactly like integers:

a new float object is created,
x is rebound,
the old object remains unchanged.

Floats are immutable too.

Now Comes the Surprise

Let's try this in the REPL.

0.1 + 0.2

Most people expect:

0.3

Python prints:

0.30000000000000004

Wait...

What?

Did Python fail primary school mathematics?

No.

This is one of the most famous examples in programming.

The Real Problem

The problem is not Python.

The problem is binary.

Remember when we studied binary numbers?

Everything inside the computer is stored using:

0
1

Computers do not store decimal numbers directly.

They store binary approximations.

Let's Compare Fractions

In decimal:

1/2 = 0.5

Perfect.

1/4 = 0.25

Perfect.

1/10 = 0.1

Perfect.

Decimal represents these nicely because it's base 10.

Now think about binary.

Binary represents fractions using powers of two:

1/2
1/4
1/8
1/16
1/32
...

Let's see.

Can binary represent:

0.5

Yes.

0.1₂

Exactly.

Can binary represent:

0.25

Yes.

0.01₂

Exactly.

But what about:

0.1₁₀

(decimal one tenth)

Binary cannot represent it exactly.

Instead it becomes:

0.000110011001100110011...

Notice something.

It repeats forever.

Just like:

1/3

=

0.333333333...

in decimal.

This Is the Key Idea

Most people think:

"0.1 is simple."

It is simple...

in decimal.

To a binary computer:

0.1

is actually an infinitely repeating binary fraction.

The computer has to stop somewhere.

It stores an approximation.

Visualizing It

What you write:

0.1

What Python stores internally is conceptually closer to:

0.10000000000000000555...

Not exactly that number, but very close.

Similarly:

0.2

is also stored as a tiny approximation.

When you add the two approximations together:

approximation

+

approximation

↓

0.30000000000000004

Python is honestly showing you the nearest representable result.

Is This a Python Problem?

No.

Try the same thing in:

Go
Java
C
JavaScript
C#
Rust

They all behave similarly because they use the same IEEE 754 floating-point standard.

This is a property of binary floating-point arithmetic, not of Python itself.

Comparing Floats

Because of these tiny approximations:

Avoid:

0.1 + 0.2 == 0.3

Instead use:

import math

math.isclose(0.1 + 0.2, 0.3)

which returns:

True

We'll study modules later, so for now just remember that exact equality isn't always appropriate for floats.

Float Operations
3.5 + 1.2

creates a new float object.

7.8 * 2

creates a new float object.

Again, the original objects are never modified.

The immutability principle still holds.

Engineer Thinking

Imagine computers used decimal hardware instead of binary.

Would this problem exist?

For numbers like:

0.1

No.

But then numbers like:

1/3

would become repeating decimals instead.

Every number system has values it can represent exactly and values it must approximate.