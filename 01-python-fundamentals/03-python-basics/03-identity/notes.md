# Identity

Let's begin with a simple question.

Suppose we have two people.

Alice
Bob

Both are:

27 years old
Dentists
Live in Lagos

Question:

Are they the same person?

Of course not.

They have the same properties, but they are still different individuals.

This is exactly the distinction Python makes.

Equality vs Identity

Python asks two completely different questions.

Question 1:

Do these two objects have the same value?

That's what == asks.

Question 2:

Are these literally the same object in memory?

That's what is asks.

These are different questions.

Think About Books

Imagine two books.

Book A

Python Basics

Book B

Python Basics

They have:

same title
same pages
same content

Are they the same physical book?

No.

That's the difference between equality and identity.

The Two Operators
==

Compares values.

Example:

10 == 10

Result:

True

Another:

"hello" == "hello"

Result:

True

Because the values are equal.

is

Compares identity.

It asks:

"Are these two names referring to exactly the same object?"

Not:

"Do they look the same?"

Example 1
x = [1, 2, 3]
y = x

What does memory look like?

           +-------------+
           | [1,2,3]     |
           +-------------+
             ▲         ▲
             │         │
             x         y

Question:

x == y

Answer:

True

Same list contents.

Question:

x is y

Answer:

True

Why?

Because both names refer to the same object.

Example 2

Now look carefully.

x = [1, 2, 3]
y = [1, 2, 3]

Memory:

      +-------------+      +-------------+
      | [1,2,3]     |      | [1,2,3]     |
      +-------------+      +-------------+
            ▲                     ▲
            │                     │
            x                     y

Now:

x == y

Result:

True

Because:

Both lists contain:

1
2
3

But:

x is y

Result:

False

Because:

They are different objects.

This is probably the most important diagram in today's lesson.

Identity is Like a Passport Number

Remember yesterday?

Every object has:

Identity
Type
Value

Imagine two passports.

Passport A

Name:
Emmanuel

Passport Number:
123456

Passport B

Name:
Emmanuel

Passport Number:
789101

Same name.

Different identity.

Python objects behave the same way.

How Python Checks Identity

Python provides:

id()

Example:

x = [1,2,3]

Now:

id(x)

Might return:

140648323252416

That number represents the object's identity during its lifetime.

Now:

y = x
id(y)

Returns the same number.

Because they're the same object.

Now compare:

x = [1,2,3]
y = [1,2,3]
id(x)

↓

140648323252416
id(y)

↓

140648325781184

Different identities.

Even though:

x == y

is

True
Why This Matters

Suppose:

x = [1,2,3]
y = x

Now:

y.append(4)

What happens?

Many beginners expect:

x

to remain:

[1,2,3]

But actually:

[1,2,3,4]

Why?

Because there was only one list object.

Two names.

One object.

Why None Uses is

Here's an important Python convention.

Instead of:

if x == None:

Python developers write:

if x is None:

Why?

Because there is only one None object.

We're asking:

"Is this object literally the singleton None?"

Not:

"Does it merely equal something?"

We'll revisit this when we study None.

A Surprise

Consider:

x = 100
y = 100

Sometimes:

x is y

returns:

True

But:

x = 1000
y = 1000

might return:

False

Why?

Because CPython interns (reuses) some small immutable objects like small integers for efficiency.

The important lesson is:

Never rely on this behavior.

Always remember:

== → compare values
is → compare object identity

# ENGINEERING THINKING

### Imagine Python did not have object identities. What kinds of problems do you think that would cause? Think about shared objects, references, and memory.

Imagine Python had no identities.

Suppose we have:

a = [1, 2]
b = a

Now:

b.append(3)

How would Python know whether to modify:

the original list, or
a completely different list that just happens to contain the same values?

Without identity, Python couldn't distinguish:

List A
[1,2]

from another independent:

List B
[1,2]

Identity allows Python to say:

"This exact object changed."