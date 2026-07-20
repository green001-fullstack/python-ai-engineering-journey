Type Conversion

Let's start with a simple question.

Suppose we write:

age = 25

Later:

str(age)

Did Python change the integer object into a string?

Think about everything you've learned.

The answer is...

No.

Python never changes the integer object.

It creates a new string object.

This should already sound familiar.

Conversions Always Create New Objects

Let's visualize it.

Initially:

age
 │
 ▼
25

Type: int

Now:

text = str(age)

Python does not modify 25.

Instead:

age
 │
 ▼
25

Type: int


text
 │
 ▼
"25"

Type: str

There are now two different objects.

The Conversion Functions

Python provides several built-in functions.

int()

Creates an integer object.

int("25")

↓

25
float()

Creates a float object.

float("3.14")

↓

3.14
str()

Creates a string object.

str(42)

↓

"42"
bool()

Creates a boolean object according to Python's truthiness rules.

bool(1)

↓

True
bool(0)

↓

False
Remember input()?

Earlier we learned:

age = input("Age: ")

What does input() return?

Always:

str

Why?

Because the keyboard sends characters.

Not integers.

Not floats.

Characters.

So if the user types:

25

Python creates:

"25"

A string object.

Then What Happens?

Suppose we write:

age = int(input("Age: "))

Let's walk through the execution.

Step 1

The keyboard sends characters.

2
5
Step 2

input() creates:

"25"

Type: str
Step 3

Now Python evaluates:

int("25")

It reads the characters:

2
5

Recognizes them as a valid decimal integer, and creates a new int object:

25

Type: int
Step 4

Only now does assignment happen.

age
 │
 ▼
25

Type: int

Notice something important.

This answers the question you asked weeks ago:

"Does age first point to the string before becoming an integer?"

The answer is:

No.

The right-hand side is fully evaluated first.

Only after int(input(...)) returns the integer object does age get bound.

The intermediate string object exists, but age never points to it.

That was a brilliant question when you asked it, and now you have the tools to answer it yourself.

Invalid Conversions

Suppose we try:

int("hello")

Python raises:

ValueError

Why?

Because:

"hello"

cannot be interpreted as an integer.

Python cannot create a valid int object.

Boolean Conversions

These surprise beginners.

bool(100)

↓

True
bool(-5)

↓

True
bool(0)

↓

False

Python's rule is simple:

Zero → False
Non-zero numbers → True

Now strings.

bool("")

↓

False
bool("Python")

↓

True

Even:

bool("False")

returns:

True

Why?

Because "False" is not an empty string.

Python doesn't read the English word—it only checks whether the string is empty.

None
bool(None)

↓

False

Again, None is falsey.

Converting Booleans

Since bool inherits from int:

int(True)

↓

1
int(False)

↓

0

Likewise:

float(True)

↓

1.0
str(True)

↓

"True"

Each conversion creates a new object of the requested type.

Converting Floats
int(3.9)

returns:

3

Notice:

It does not round.

It truncates the fractional part.

Likewise:

int(-3.9)

returns:

-3

It truncates toward zero.

Engineer Thinking

Think about this carefully.

When you write:

str(42)

Python is not changing the integer.

It is asking:

"Please create a string object that represents this integer."

That's a profound difference.

Once again:

evaluate,
create a new object,
return it.

You've seen this pattern over and over.