Integers

Let's begin with a question.

What is this?

42

Most people answer:

"A number."

That's not wrong.

But after everything we've learned...

Can we give a better answer?

What is 42?

42 is not just a number.

It is:

An integer object.

Remember our object model.

Object

Identity
Type
Value

So for 42:

Object

Identity: (unique)
Type: int
Value: 42

Immediately notice something.

42 is an object.

It is not merely bits floating around in memory.

Python wraps those bits inside an object.

Everything in Python is an Object

This is one of Python's biggest ideas.

All of these are objects:

42
3.14
"Hello"
True
None
[1, 2, 3]

Even functions are objects.

Even classes are objects.

We'll prove that later.

Creating an Integer Object

Suppose you write:

x = 42

Conceptually:

Namespace

x
│
▼
Reference
│
▼

Object

Type: int

Value: 42

Exactly the same model we've been using.

Integers are Immutable

Remember immutable?

Let's test it.

x = 42

Now:

x = x + 1

Did Python change 42?

No.

It created:

43

as a brand-new integer object.

Then:

Before

x

↓

42


After

42

x

↓

43

The name moved.

The object didn't change.

Why Are Integers Immutable?

Imagine if integers could change.

Suppose:

x = 42
y = x

Both names point to the same object.

If Python modified the integer itself:

x += 1

Then y would suddenly become:

43

That would be surprising and dangerous.

Immutability avoids this problem.

Integer Objects Have Methods

Here's something many beginners don't realize.

x = 42

is an object.

Objects have behavior.

Let's ask Python.

dir(42)

You'll see dozens of methods.

For example:

(42).bit_length()

Output:

6

Why?

Because:

42

↓

101010

needs six bits.

Amazing.

An integer knows things about itself.

Python Integers Are Huge

Now compare Python with Go.

In Go:

int

is usually:

64 bits

Maximum:

9,223,372,036,854,775,807

After that?

Overflow.

Python?

Watch this:

x = 999999999999999999999999999999999999999999999999

Works.

Now:

x = x * x

Still works.

Why?

Python integers automatically grow.

Internally, Python allocates more memory when needed.

This is one reason Python is popular in fields like cryptography and scientific computing.

But Isn't That Slower?

Yes.

Everything has a trade-off.

Go:

Fixed size

↓

Fast

Python:

Flexible size

↓

More memory

↓

More work

Python chooses convenience.

Go chooses speed.

Negative Numbers

What about:

-42

Is that another type?

No.

Still:

type(-42)

returns:

int

It's still an integer object.

The value simply happens to be negative.

We'll later discuss how computers represent negative numbers internally using two's complement, connecting back to the hardware lessons.

Integers Support Operations

Python lets integer objects participate in many operations:

5 + 3
5 - 3
5 * 3
5 // 3
5 % 3
5 ** 3

Each of these creates a new integer object.

Notice the pattern again.

Objects aren't modified.

New objects are produced.

Everything Connects

Suppose we write:

x = 10
y = 20

z = x + y

Conceptually:

x ──► 10

y ──► 20

↓

+

↓

30

↓

z

Notice:

Neither 10 nor 20 changed.

A new integer object:

30

was created.

Engineer Thinking

Let's compare two worlds.

Mutable integers
10

↓

change

↓

11

One object changing constantly.

Immutable integers
10

↓

new object

↓

11

This makes reasoning about programs much simpler and safer.