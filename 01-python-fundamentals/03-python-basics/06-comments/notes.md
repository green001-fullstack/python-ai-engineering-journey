# Comments

Let's start with a question.

Suppose I write this:

x = x + 1

Can Python understand it?

Yes.

Can another programmer understand it?

Maybe.

Can future you understand it six months later?

Not always.

That's why comments exist.

What is a Comment?

A comment is:

Text written for humans that Python ignores during execution.

Notice that phrase carefully:

Python ignores it.

That means comments are not converted into bytecode.

They are not executed.

They never reach the CPU.

Remember Our Execution Journey

When we studied the interpreter, we learned this pipeline:

Source Code
      │
      ▼
Bytecode
      │
      ▼
Python Virtual Machine
      │
      ▼
Machine Instructions
      │
      ▼
CPU

Now imagine this code:

(hash) Calculate the total
total = price * quantity

Python effectively behaves like this:

total = price * quantity

The comment is skipped.

It never becomes part of the program's execution.

Single-Line Comments

Python uses the # symbol.

Example:

(hash) This stores the user's age

age = 27

Everything after # on that line is treated as a comment.

Another example:

temperature = 37  # Body temperature

The code executes normally.

The text after # is ignored.

Multi-Line Comments?

Python doesn't have a special multi-line comment syntax like:

/* comment */

Instead, we usually write:

(hash) Step 1

(hash) Read the file

(hash) Convert it to JSON

(hash) Save the result

One # per line.

What About Triple Quotes?

You may see:

"""
This looks like
a multi-line comment.
"""

Is this actually a comment?

Not exactly.

It's a string object.

Remember:

Everything in quotes creates a string object.

If that string isn't assigned to a name or used, Python simply discards it.

People sometimes use this as a comment, but technically it's an unused string literal.

Later, you'll learn its real purpose: docstrings.

Good Comments vs Bad Comments

Suppose we have:

age = age + 1

Bad comment:

(hash) Increase age by 1
age = age + 1

Why is this bad?

Because the code already tells us that.

The comment adds no new information.

A better example:

(hash) Age is stored in years because the API expects years.
age = age + 1

Now the comment explains why, not what.

Comments Should Explain Why

Imagine this:

discount = price * 0.07

Good?

Maybe.

But imagine writing:

(hash) Government tax regulation requires a fixed 7% deduction.
discount = price * 0.07

Now another developer understands the reason.

Comments Can Become Wrong

Suppose today you write:

(hash) Apply 5% tax
tax = price * 0.05

Later someone changes the code:

tax = price * 0.08

But forgets the comment.

Now:

The code says:

8%

The comment says:

5%

Which one is true?

The code.

This is why outdated comments can be worse than no comments.

Code Should Be Readable

Instead of:

x = a * b

You might write:

area = width * height

Now the names explain the code.

No comment needed.

Good naming often eliminates the need for comments.

Comments and the CPU

Let's connect this to everything we've learned.

Suppose we write:

(hash) Store the user's score
score = 100

What reaches RAM?

Not the comment.

Only the object created by:

score = 100

The comment disappears before execution.

It never reaches:

RAM
CPU
Registers
ALU

It exists purely for humans reading the source code.

Engineer Thinking

Imagine comments were executed.

What would this mean?

(hash) Hello Python

Would Python have to convert English into machine code?

That wouldn't make sense.

Instead, the interpreter recognizes comments during parsing and skips them.

This is one reason comments have zero effect on your program's behavior.

Best Practices

✔ Use comments to explain why something is done.

✔ Keep comments updated.

✔ Use meaningful variable names first.

✔ Avoid commenting every obvious line.