Assignment Operators

Most people think:

"= puts a value into a variable."

You already know that's not what happens.

What really happens is:

Assignment binds a name to an object.

This lesson is about how different assignment operators affect that binding.

The Basic Assignment (=)

Suppose we write:

x = 10

Does Python put 10 inside x?

No.

It creates (or finds) the integer object 10 and binds the name x to it.

x
│
▼
10

Now:

y = x

What gets copied?

Not the integer.

The reference gets copied.

x ───┐
     │
y ───┘
      │
      ▼
      10

Nothing new is created.

Augmented Assignment (+=)

Now consider:

x = 10
x += 5

Many people think Python literally rewrites this as:

x = x + 5

For integers, the effect is essentially the same:

Evaluate x + 5
Create a new integer object 15
Rebind x to the new object

The original 10 is unchanged.

Before:

x ─────► 10

After:

10   (still exists if referenced)

x ─────► 15
Why?

Because integers are immutable.

Python cannot modify the existing integer object.

It must create a new one.

Now Let's Change the Type

Suppose:

numbers = [1, 2]

Then:

numbers += [3]

Does Python create a new list?

Not necessarily.

Lists are mutable.

So Python can often modify the existing list object in place.

Conceptually:

Before:

numbers
│
▼
[1, 2]

After:

numbers
│
▼
[1, 2, 3]

Same list object.

Different contents.

Here's the Surprise
a = [1, 2]
b = a

a += [3]

What happens?

Many beginners expect:

a ─────► [1, 2, 3]

b ─────► [1, 2]

But that's not what happens.

Because a += [3] modifies the existing list.

Both names still point to that same list.

a ───┐
     │
b ───┘
      │
      ▼
[1, 2, 3]

This is one of the classic Python interview questions.

Compare with Integers

Now:

x = 10
y = x

x += 5

Result:

y ─────► 10

x ─────► 15

Why the difference?

Because integers are immutable.

+= creates a new integer object.

The General Rule

For immutable objects:

+=

usually creates a new object.

For mutable objects:

+=

may modify the existing object.

The exact behavior depends on the object's type and how it implements augmented assignment.

Other Assignment Operators

These work similarly:

x -= 2

Equivalent in effect (for integers) to:

x = x - 2
x *= 4

Equivalent in effect to:

x = x * 4
x /= 2

Equivalent in effect to:

x = x / 2

Remember:

/ always produces a float.

So:

x = 10

x /= 2

Now:

x

references:

5.0

A float object, not an integer.

Assignment Never Copies Objects

This is one of the most important principles in Python.

Suppose:

a = [1, 2]

b = a

No list is copied.

Only the reference.

This explains many "mysterious" bugs beginners encounter.

Engineer Thinking

Imagine Python copied every object during assignment.

big_list = [millions of items]

backup = big_list

If assignment copied the list every time:

It would take much longer.
It would use much more memory.

Python's reference model avoids that cost.

If you actually want a copy, you ask for one explicitly.


Immutable (int)

Before

x ───┐
     │
y ───┘
      │
      ▼
      10

After x += 5

y ─────► 10

x ─────► 15

Mutable (list)

Before

a ───┐
     │
b ───┘
      │
      ▼
   [1, 2]

After a += [3]

a ───┐
     │
b ───┘
      │
      ▼
 [1, 2, 3]