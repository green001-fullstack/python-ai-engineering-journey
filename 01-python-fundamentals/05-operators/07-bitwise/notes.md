The Bitwise Operators
Operator	Name
&	AND
`	`
^	XOR
~	NOT
<<	Left Shift
>>	Right Shift

Don't worry if these look unfamiliar.

We'll build them one at a time.

Step 1 — Bitwise AND (&)

Suppose:

10 & 12

First convert them to binary.

10 = 1010

12 = 1100

Now compare each bit.

Rule:

1 & 1 → 1

1 & 0 → 0

0 & 1 → 0

0 & 0 → 0

Let's align them.

1010
1100
----
1000

Binary:

1000

is decimal:

8

So:

10 & 12

returns

8
Step 2 — Bitwise OR (|)

Rule:

1 | 1 → 1

1 | 0 → 1

0 | 1 → 1

0 | 0 → 0

Example:

1010
1100
----
1110

Binary:

1110

Decimal:

14

Therefore:

10 | 12

returns

14
Step 3 — Bitwise XOR (^)

Rule:

Bits must be different.

1 ^ 1 → 0

0 ^ 0 → 0

1 ^ 0 → 1

0 ^ 1 → 1

Example:

1010
1100
----
0110

Binary:

0110

Decimal:

6
Step 4 — Left Shift (<<)

Suppose:

5 << 1

Binary of 5:

0101

Shift everything left one place.

1010

Binary:

10

So:

5 << 1

↓

10

A useful mental shortcut:

For non-negative integers,

x << 1

is equivalent to:

x × 2

Similarly:

x << 2

means:

x × 4

because each left shift multiplies by 2.

Step 5 — Right Shift (>>)

Suppose:

20 >> 1

Binary:

10100

Shift right.

01010

Binary:

10

So:

20 >> 1

↓

10

A useful shortcut:

x >> 1

is roughly:

x ÷ 2

for non-negative integers.

Step 6 — Bitwise NOT (~)

This one is different.

It flips every bit.

1 → 0

0 → 1

In Python, because integers have arbitrary precision and use a signed representation, you'll see results like:

~5

↓

-6

This surprises many people.

We'll revisit why when we discuss binary representation of signed numbers. For now, it's enough to know that ~ inverts the bits.

Where Is This Used?

Although you won't use bitwise operators every day, they're very important in:

Operating systems
Networking protocols
Compression algorithms
Cryptography
Image processing
Graphics programming
Embedded systems
Device drivers
Performance optimization
Connecting Back to Hardware

Remember when we studied the CPU?

The ALU (Arithmetic Logic Unit) doesn't understand Python.

It understands operations like:

ADD
SUBTRACT
AND
OR
XOR
SHIFT

Python's bitwise operators map closely to those low-level CPU operations.

This is one reason bitwise operations are usually very fast.