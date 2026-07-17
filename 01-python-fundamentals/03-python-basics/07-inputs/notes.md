Input

This is another lesson that most tutorials teach in about 2 minutes:

name = input("What is your name? ")

Then they move on.

We're not going to do that.

We're going to answer:

What actually happens when you press a key on your keyboard?

Imagine This Program
name = input("What is your name? ")

Suppose you type:

Emmanuel

How did those letters end up inside name?

Let's follow the journey.

Step 1 — The Keyboard

You press:

E

What happens?

Inside the keyboard are tiny electrical switches.

Pressing the key closes a circuit.

The keyboard's microcontroller detects:

"The E key was pressed."

It sends that information to the computer.

Step 2 — The Operating System

The operating system receives the keyboard event.

Something like:

Key Pressed

E

The operating system then delivers this event to the running Python program.

Notice something.

Python isn't reading the keyboard directly.

The operating system is helping.

Step 3 — Python is Waiting

When Python executes:

input(...)

It pauses.

Conceptually:

Python

Waiting...

Waiting...

Waiting...

The interpreter is blocked until the operating system provides the user's input.

Step 4 — Characters Become a String

Suppose you type:

Emmanuel

Python collects:

E
m
m
a
n
u
e
l

Then creates a string object.

Remember our object model.

Object

Type: str

Value:

"Emmanuel"

That object is placed in memory.

Step 5 — The Name is Bound

Now:

name = input(...)

becomes conceptually:

Namespace

name
 │
 ▼
Reference
 │
 ▼

String Object

"Emmanuel"

Does that diagram look familiar?

It should.

It's exactly the same object model we've been building.

Why Does input() Return a String?

This surprises almost everyone.

Suppose you type:

25

Python returns:

"25"

Not:

25

Why?

Because the keyboard doesn't know whether:

25

means:

a person's age,
a ZIP code,
a password,
a student ID,
or a number for calculation.

The keyboard only provides characters.

So input() always returns a string object.

Example
age = input("Age: ")

Suppose you type:

25

Memory:

age
 │
 ▼

Object

Type: str

Value:

"25"

Not:

Type: int
Converting It

If you actually want an integer:

age = int(input("Age: "))

What happens?

First:

input()

creates:

"25"

Then:

int()

creates:

25

Notice something.

int() does not change the string.

Remember immutable objects.

Instead:

"25"

↓

New Object

25

A new integer object is created.

Connecting Everything

Suppose:

age = int(input())

The journey looks like this:

Keyboard

↓

Operating System

↓

Python input()

↓

String Object

↓

int()

↓

Integer Object

↓

age

Everything we've learned connects beautifully.

What if the User Types This?
hello

Now Python tries:

int("hello")

Can Python convert:

hello

into an integer?

No.

It raises:

ValueError

We'll study exceptions later, but it's useful to see that Python protects you from invalid conversions.

Input is a Function

Remember:

input()

is just another function.

It:

waits,
receives text,
creates a string object,
returns a reference to it.

Just like:

len()

returns an integer,

or

type()

returns a type object.

Engineer Thinking

Imagine input() returned different types automatically.

Suppose you typed:

007

Should Python return:

7

or

"007"

What if it was a bank account number?

Or a product code?

Automatically guessing the type would cause subtle bugs.

Returning a string every time is simple, predictable, and leaves the decision to the programmer.