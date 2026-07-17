# What Is an Object?

Now let's define it carefully.

An object is:

A piece of memory that contains data and information about itself.

Notice I didn't just say "data."

It also carries metadata—information about the data.

Think of a Passport

Imagine a passport.

It contains:

your name,
your date of birth,
your nationality,
your passport number.

Now imagine an object.

It also carries information about itself.

For example, the object representing 10 knows:

"I am an integer."
"These are my data."
"These are the operations I support."

Python doesn't have to guess.

The object tells Python what it is.

Every Object Has Three Fundamental Properties

This is one of the most important ideas in Python.

Every object has:

Identity
Type
Value

We'll spend entire lessons on the first two, but let's introduce them now.

1. Identity

Every object has a unique identity while it exists.

Think of it like a passport number.

Even if two people have the same name...

Their passport numbers are different.

Similarly:

10

has an identity.

2. Type

Every object knows what kind of object it is.

For example:

10

Type:

int

For:

"Hello"

Type:

str

Python doesn't guess.

The object knows its own type.

3. Value

Finally, the object has a value.

For:

10

Value:

10

For:

"Hello"

Value:

Hello
Let's Connect This

Imagine the object:

10

Conceptually, it looks like this:

+-------------------------+
| Identity: 0x...         |
| Type: int               |
| Value: 10               |
+-------------------------+

Notice that the identity isn't something you normally care about as a programmer, but Python keeps track of it internally.

Objects Know Their Type

Let's ask Python:

type(10)

Output:

<class 'int'>

Try another:

type("Hello")

Output:

<class 'str'>

Another:

type([1,2,3])

Output:

<class 'list'>

Python isn't inspecting the characters you typed.

It's asking the object:

"What type are you?"

Objects Know What They Can Do

Remember this:

"hello".upper()

How does Python know that strings have an upper() method?

Because the string object knows what operations belong to strings.

Similarly:

my_list.append(5)

Lists know how to append.

Integers don't.

Try this mentally:

10.append(5)

Python would complain because integer objects don't have an append() method.

This Is Different from C

In C, an integer is mostly just raw data.

In Python:

10

is a complete object with:

data,
type information,
supported operations.

This makes Python much more flexible.

Objects Live in Memory

Remember our RAM lesson?

Objects live there.

Conceptually:

RAM

+-------------------------+
| int object              |
| Value: 10               |
+-------------------------+

+-------------------------+
| str object              |
| Value: "Hello"          |
+-------------------------+

+-------------------------+
| list object             |
| Value: [1,2,3]          |
+-------------------------+

Variables simply give names to these objects.

Why This Matters

Consider:

x = 10

From last lesson:

x
│
▼

Now we can complete the picture:

x
│
▼
+-------------------------+
| Identity                |
| Type: int               |
| Value: 10               |
+-------------------------+

Notice how the object contains much more than just the number 10.