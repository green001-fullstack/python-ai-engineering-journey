References

Let's start with a question.

Suppose I say:

"Go and tell Emmanuel."

Question:

Did I hand you Emmanuel?

No.

I gave you a way to find Emmanuel.

That's what a reference is.

A reference is not the object.

It is a way to refer to the object.

Think About Google Maps

Imagine your friend asks:

"Where is the restaurant?"

You don't pick up the restaurant and hand it to them.

You send them a Google Maps location.

The location is not the restaurant.

It simply tells you how to reach it.

References work the same way.

A Reference is...

Let's define it.

A reference is Python's internal way of referring to an object.

Notice something.

We said earlier:

A variable is a name.

Now we're saying:

That name is bound to a reference to an object.

Conceptually:

x
│
▼
Reference
│
▼
Object

In practice, Python hides the reference from you.

You normally just write:

x = 10

But internally, something like this is happening.

Let's Build the Picture

Suppose:

x = [1, 2, 3]

Memory conceptually:

Namespace

x
│
▼
Reference
│
▼

RAM

+----------------+
| List Object    |
| [1,2,3]        |
+----------------+

Now:

y = x

What gets copied?

Not the list.

Not the values.

The reference.

Now:

Namespace

x ─────┐
        │
        ▼
    Reference
        │
        ▼

+----------------+
| List Object    |
| [1,2,3]        |
+----------------+
        ▲
        │
    Reference
        ▲
        │
y ──────┘

There is still one list object.

This Explains Everything

Now:

y.append(4)

Did y modify its own private list?

No.

There was never a second list.

There was only:

+----------------+
| [1,2,3,4]      |
+----------------+

Both names still point to it.

So:

print(x)

prints:

[1,2,3,4]

This surprises almost every beginner.

But it won't surprise you anymore.

Why Integers Feel Different

Now compare:

x = 10
y = x

Diagram:

        +---------+
        | 10      |
        +---------+
          ▲     ▲
          │     │
          x     y

Now:

x = 20

Did Python modify 10?

No.

Remember what we learned.

Python rebinds the name.

Now:

        +---------+
        | 10      |
        +---------+
             ▲
             │
             y

        +---------+
        | 20      |
        +---------+
             ▲
             │
             x

Notice something.

No object changed.

Only a name changed.

Mutable vs Immutable

Now we're ready for a new word.

Some objects can change.

Some cannot.

Mutable

Can change after creation.

Example:

[]
{}
set()

Lists are mutable.

Immutable

Cannot change after creation.

Example:

10
3.14
True
"Hello"

When you write:

x = 20

Python doesn't change 10.

It creates a new integer object.

Then:

x

is rebound.

This Is Why Lists Behave Differently

Consider:

numbers = [1,2,3]

Now:

numbers.append(4)

The list object changes.

The reference stays the same.

But:

number = 10
number += 1

This does not modify the integer.

It creates:

11

and rebinds:

number
Connecting to Go

"Are Python variables like pointers in Go?"

Now we can answer it properly.

Go
x := &person

Here, x explicitly stores a memory address.

You can:

*x

Dereference it.

You can do pointer arithmetic in some languages like C.

Pointers are part of the language.

Python

Python deliberately hides all of that.

Instead, it gives you:

x = person

You never see the memory address.

You never dereference.

You never manipulate pointers.

Instead, Python automatically manages references.

So:

A Go pointer is an explicit language feature.
A Python reference is an implementation concept that the language exposes only indirectly.

That's why they feel similar but are not the same thing.