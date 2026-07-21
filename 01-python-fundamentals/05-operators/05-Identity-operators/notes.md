Identity Operators

Python has two identity operators:

Operator	Meaning
is	Are these the same object?
is not	Are these different objects?

Notice that identity operators are not about value.

They are about object identity.

Think Back to Chapter 3

Remember when we said every Python object has:

Data
Type
Identity
Operations

Today we're using the identity part.

Example 1
x = [1, 2]
y = x

Visualize it:

x ───┐
     │
y ───┘
      │
      ▼
   [1, 2]

Now ask:

x is y

Python asks:

"Do these names refer to the exact same list object?"

Answer:

True

Now:

x == y

Also returns:

True

Why?

Because:

Same object
Same value

Both happen to be true.

Example 2
a = [1, 2]
b = [1, 2]

Now visualize:

a ─────► [1, 2]

b ─────► [1, 2]

Two separate list objects.

Now:

a == b

↓

True

because the values match.

But:

a is b

↓

False

because they're different objects.

is not

This is simply the opposite of is.

Example:

a = [1]
b = [1]

a is not b

Result:

True

because they are different objects.

The Famous None

You already know this one.

result = None

Checking:

if result is None:

is the preferred style.

Why?

Because there is exactly one None object in Python.

You're asking:

"Is this object the singleton None?"

Not:

"Does this object compare equal to None?"

Why Not == None?

Imagine this class:

class Strange:
    def __eq__(self, other):
        return True

Now:

obj = Strange()

obj == None

returns:

True

because the class chose to define equality that way.

But:

obj is None

returns:

False

because obj is clearly not the None object.

Identity cannot be redefined.

That's why is None is the recommended style.

Identity Never Changes

Suppose:

numbers = [1, 2]

The list's contents may change:

numbers.append(3)

Now:

[1, 2]

became:

[1, 2, 3]

But it's still the same object.

Its identity didn't change.

Identity vs Mutability

These ideas are related but different.

A mutable object:

can change its contents,
without changing its identity.

An immutable object:

cannot change,
so "modifying" it creates a new object with a new identity.
A Common Beginner Mistake

Many beginners write:

if name is "Alice":

This is incorrect.

Why?

Because you're interested in whether the text matches, not whether the string objects happen to be the same object.

Correct:

if name == "Alice":

Use == for values.

Use is for identity.

Engineer Thinking

Imagine Python removed is.

Could we still check whether two names refer to the exact same object?

Not reliably.

Two different objects may compare equal with ==, even though they're distinct objects.

Identity answers a completely different question from equality.