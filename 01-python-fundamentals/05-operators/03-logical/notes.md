Logical Operators

Logical operators combine or modify truth values.

Python has three logical operators:

Operator	Meaning
and	Both conditions must be truthy
or	At least one condition must be truthy
not	Reverses truthiness

Most tutorials stop there.

We're not.

The real question is:

What do these operators actually return?

First, Remember Truthiness

From Chapter 4, we learned:

These are falsey:

False
None
0
0.0
""
[]
{}
set()

Everything else is generally truthy.

Examples:

5

↓

Truthy

"Python"

↓

Truthy

[1, 2, 3]

↓

Truthy

This lesson depends heavily on that idea.

and

Suppose:

True and True

returns:

True
True and False

returns:

False

So far, nothing surprising.

Now watch this:

5 and 10

What do you think?

Many beginners answer:

True

But Python returns:

10

Why?

The Rule for and

Python evaluates the left operand first.

If the left operand is falsey, it immediately returns that operand.

Otherwise, it evaluates and returns the right operand.

Notice:

It returns an object, not necessarily a boolean.

Let's test it.

0 and 10

Left operand:

0

Falsey.

Python stops immediately.

Result:

0

Now:

5 and 10

Left operand:

5

Truthy.

Python continues.

Returns:

10

Another example:

"Hello" and "World"

returns:

"World"

Both are truthy, so Python returns the second operand.

Why?

Think like an engineer.

The purpose of and is:

"If the first thing is falsey, the whole expression cannot succeed."

There's no need to evaluate the second operand.

This is called short-circuit evaluation.

or

Now:

False or True

↓

True

Simple.

But now:

0 or 10

returns:

10

Why?

Because:

0

is falsey.

Python looks at the next operand.

Now:

5 or 10

returns:

5

Not True.

The actual object:

5
Rule for or

Evaluate the left operand.

If it is truthy:

Return it immediately.

Otherwise:

Evaluate and return the right operand.

Example:

"" or "Python"

↓

Left operand:

""

Falsey.

Result:

"Python"

Example:

"Go" or "Python"

↓

Left operand already truthy.

Result:

"Go"
not

Unlike and and or:

not always returns a boolean object.

Example:

not True

↓

False
not False

↓

True

Now:

not 5

↓

False

because 5 is truthy.

not ""

↓

True

because the empty string is falsey.

Short-Circuit Evaluation

This is one of Python's most useful optimizations.

Suppose:

False and expensive_function()

Will expensive_function() run?

No.

Why?

Because:

False and anything

can never become true.

Python stops immediately.

Similarly:

True or expensive_function()

The function never runs.

Python already knows the answer.

A Practical Example

Suppose:

name = ""

Now:

name or "Anonymous"

returns:

"Anonymous"

Why?

Because:

name

is an empty string.

Empty strings are falsey.

This pattern is extremely common in Python.

Another example:

user_input = input("Name: ")

display_name = user_input or "Guest"

If the user presses Enter without typing anything:

user_input

is:

""

Falsey.

So:

display_name

becomes:

"Guest"

Elegant.

Engineer Thinking

Suppose:

x = []

result = x or [1, 2, 3]

Question:

Does Python create the second list?

Or does it skip it?

Think carefully.

The list literal [1, 2, 3] is part of the expression. Python must evaluate it if it needs it. Since x is an empty list (falsey), or evaluates and returns the right-hand list object.

Now compare with:

x = [9]

result = x or [1, 2, 3]

Here x is truthy, so Python returns the existing list referenced by x and does not evaluate the right-hand operand.

This is another example of short-circuit evaluation.

Connecting to Previous Lessons

Notice how everything fits together.

Comparison:

10 > 5

↓

Returns:

True

Then:

(10 > 5) and (3 < 7)

↓

Both comparison expressions produce boolean objects.

Then and operates on those results.

Everything builds on what you've already learned.


### Suppose:

username = ""

display = username or "Guest"

### Why is this pattern better than writing:

if username == "":
    display = "Guest"
else:
    display = username

##### Think about readability, expressiveness, and Python's truthiness model.

### Ans: The first pattern:

display = username or "Guest"

is better because:

It's shorter.
It expresses the intent clearly: "Use username; otherwise use 'Guest'."
It leverages Python's truthiness model, making it idiomatic Python.
It scales well.