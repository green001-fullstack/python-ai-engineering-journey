Booleans

Let's begin with the simplest question.

What is this?

True

Most beginners answer:

"A boolean."

That's true.

But after everything we've learned...

A better answer is:

An immutable Python object of type bool.

Just like:

42

creates an int object,

and

3.14

creates a float object,

this:

True

creates a bool object.

There Are Only Two Boolean Objects

Unlike integers...

1
2
3
4
...

there are only two boolean values:

True
False

That's it.

Python doesn't have a third boolean value.

Booleans Are Objects
x = True

Conceptually:

Namespace

x
│
▼
Reference
│
▼

Object

Type: bool

Value: True

Exactly the same object model again.

Nothing has changed.

Where Did Booleans Come From?

Remember our logic gate lessons?

AND

1 AND 1 = 1

OR

1 OR 0 = 1

NOT

NOT 1 = 0

Computers make decisions using exactly these ideas.

Python simply gives those ideas names:

Hardware

1

↓

Python

True

and

Hardware

0

↓

Python

False
Comparison Operators Produce Booleans

Suppose:

5 > 3

Does Python return:

5

No.

Does it return:

3

No.

It creates:

True

Likewise:

10 < 2

creates:

False

Notice:

Comparisons don't modify numbers.

They produce new boolean objects.

Logical Operators

Remember these?

True and False

↓

False
True or False

↓

True
not True

↓

False

You already understand these because of our hardware lessons.

Python is simply exposing the same logic at a higher level.

The Big Surprise

Now try this.

True + True

Output:

2

Wait...

What?

Or this:

False + True

Output:

1

Why?

The Reason

Let's ask Python.

type(True)

returns:

<class 'bool'>

Now try:

isinstance(True, int)

Output:

True

Wait...

What?

Yes.

In Python:

bool is a subclass of int.

That means booleans inherit many behaviors from integers.

Conceptually:

object
   │
   ▼
int
   │
   ▼
bool

So internally:

False

↓

0

and

True

↓

1

Not merely "like" 0 and 1.

They behave as integer values in arithmetic.

Examples
True + True

↓

2

because

1 + 1
True * 5

↓

5

because

1 × 5
False * 100

↓

0

because

0 × 100
Why Did Python Do This?

Excellent question.

Imagine counting successful operations.

results = [True, False, True, True]

How many succeeded?

You can simply write:

sum(results)

Output:

3

Because:

True

↓

1

and

False

↓

0

This turns out to be incredibly useful in real programs.

Truthiness

Here's something even more interesting.

Not everything has to literally be True or False.

Python asks:

"Can this object be treated as true?"

For example:

bool(1)

↓

True
bool(0)

↓

False
bool("")

↓

False
bool("Hello")

↓

True
bool([])

↓

False
bool([1])

↓

True

Why?

Empty containers are considered "falsey."

Non-empty containers are considered "truthy."

We'll explore this much more when we study control flow.

Immutability

Are booleans mutable?

No.

Exactly like integers.

Suppose:

x = True

Later:

x = False

Python doesn't change the True object.

It simply rebinds x to the False object.