Lesson 4
Strings

Let's begin with a familiar line.

name = "Emmanuel"

Most people would say:

"name stores the string."

But after everything we've learned...

Can we describe it more accurately?

What is "Emmanuel"?

It is not just text.

It is:

An immutable Python object of type str.

Exactly like:

42

creates an int object,

and

True

creates a bool object,

this:

"Emmanuel"

creates a str object.

Conceptually:

Namespace

name
 │
 ▼
Reference
 │
 ▼

Object

Type: str

Value:

"Emmanuel"

Notice something.

Our object model still hasn't changed.

Only the object's type has.

What Is Inside a String Object?

A string object contains:

Type: str

Value:

H
e
l
l
o

You can imagine it as an ordered sequence of characters.

Each character has a position called its index.

 H   e   l   l   o
 0   1   2   3   4

Python lets us access them.

word = "Hello"

print(word[0])

Output:

H

Negative indexes count backward.

 H   e   l   l   o
 0   1   2   3   4

-5 -4 -3 -2 -1

So:

word[-1]

returns:

o
Are Strings Mutable?

Let's test it.

name = "Emmanuel"

Can we do this?

name[0] = "A"

No.

Python raises an error.

Why?

Because strings are immutable.

Just like integers.

Why Are Strings Immutable?

Imagine this.

x = "hello"
y = x

Both names point to the same string object.

If Python allowed:

x[0] = "H"

Then what should y become?

Hello

or

hello

This is the exact same reasoning we used for integers and floats.

Immutability prevents surprising shared changes.

Then How Does This Work?

Suppose:

name = "Emmanuel"

name = name.upper()

Did upper() modify the original string?

No.

Let's reason it out.

Initially:

name
 │
 ▼

"Emmanuel"

Then:

name.upper()

creates a new string object:

"EMMANUEL"

Finally:

name
 │
 ▼

"EMMANUEL"

The original string object still exists until nothing references it anymore.

This pattern should feel very familiar by now.

Strings Have Methods

Since strings are objects, they have behavior.

name = "Emmanuel"

print(name.upper())

Output:

EMMANUEL

Other useful methods:

name.lower()
name.capitalize()
name.title()
name.strip()
name.replace("m", "M")

These methods all return new string objects.

None of them modify the original string.

String Concatenation

Suppose:

first = "Hello"
second = "World"

result = first + " " + second

What happens?

Python creates:

"Hello World"

A brand new string object.

Neither:

"Hello"

nor

"World"

changes.

String Repetition

Python allows:

print("Go! " * 3)

Output:

Go! Go! Go!

Again:

A new string object is created.

Slicing

One of Python's nicest features.

Suppose:

word = "Python"

Memory conceptually:

P y t h o n
0 1 2 3 4 5

Now:

word[0:2]

returns:

Py

Notice something important.

Python does not modify the original string.

It creates another string object.

Original

Python

↓

Slice

Py
Membership

Suppose:

"th" in "Python"

Output:

True

Python searches the string and returns a boolean object.

Again, notice how the data types are interacting:

Strings
Booleans

Nothing we've learned exists in isolation.

Equality vs Identity

Remember this?

a = "hello"
b = "hello"

Then:

a == b

asks:

Do they have the same value?

Whereas:

a is b

asks:

Are they the same object?

Just like with integers, it's important not to confuse value equality with object identity.

We'll revisit this in more depth when discussing Python's optimizations, but for now, remember the semantic difference.

Engineer Thinking

Why do you think Python made strings immutable?

Think about where strings are used:

Dictionary keys
File paths
URLs
Module names
JSON keys

If a string used as a dictionary key could suddenly change, the dictionary's internal organization could break.

Immutability makes strings reliable and safe to share.

Connecting Everything

Let's trace this program.

name = input("Name: ")

print(name.upper())

