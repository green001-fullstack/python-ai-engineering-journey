Comparison Operators

Comparison operators ask questions.

Unlike arithmetic operators, which produce numbers or strings, comparison operators produce boolean objects.

For example:

5 > 3

does not produce an integer.

It produces:

True

And remember from the last chapter:

True is a bool object.

The Comparison Operators
Operator	Meaning
==	Equal to
!=	Not equal to
<	Less than
>	Greater than
<=	Less than or equal
>=	Greater than or equal
What Happens Internally?

Suppose we write:

result = 10 > 5

Let's trace it.

Step 1

Evaluate:

10

↓

Integer object.

Step 2

Evaluate:

5

↓

Another integer object.

Step 3

Python performs the comparison.

The result is:

True

Notice something important.

Python doesn't return the word "True."

It returns the singleton True object.

Step 4
result

↓

True

The variable is now bound to the True object.

Again, our object model hasn't changed.

Equality (==)

Suppose:

x = 10
y = 10

x == y

What question is Python asking?

It is asking:

Do these objects represent the same value?

The answer is:

True

Notice carefully:

== is about value equality.

Not memory.

Not identity.

Identity (is)

Now consider:

x is y

This asks a completely different question:

Are these two names referring to the exact same object?

This has nothing to do with value.

It is about object identity.

You already know this from our previous lessons.

Example
a = [1, 2]
b = [1, 2]

Now:

a == b

↓

True

because the lists contain the same values.

But:

a is b

↓

False

because they are two different list objects.

A Familiar Example

Remember None.

x = None
y = None

Now:

x is y

↓

True

because there is only one None object.

That's why we always write:

if x is None:

instead of:

if x == None:
Comparing Strings
"apple" == "apple"

↓

True

because the values match.

"apple" < "banana"

What do you think?

It returns:

True

Python compares strings alphabetically (technically, lexicographically, based on Unicode code points).

Comparing Numbers
10 > 3

↓

True
10 < 3

↓

False

Simple enough.

Here's a Surprise

What does this return?

1 == True

Think before reading on.

The answer is:

True

Why?

Remember Chapter 4?

bool is a subclass of int.

Conceptually:

True

behaves like:

1

and

False

behaves like:

0

So Python compares their values and considers them equal.

But now look at this:

1 is True

The result is:

False

Why?

Because they are not the same object.

One is an int object.

The other is the singleton True object.

This perfectly demonstrates the difference between equality and identity.

Chained Comparisons

Python allows this:

10 < x < 20

Instead of writing:

10 < x and x < 20

Python evaluates it as:

Is x greater than 10 and less than 20?

This is one of Python's nicest language features.

Engineer Thinking

Suppose:

x = 1000
y = int("1000")

Question:

Would you expect:

x == y

to be True or False?

What about:

x is y

Think in terms of:

value
object identity
object creation