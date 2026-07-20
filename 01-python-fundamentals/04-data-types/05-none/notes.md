None

Let's start with a question.

What is this?

None

Many beginners say:

"Nothing."

That's a useful intuition, but it's not technically correct.

After everything we've learned about Python's object model, can "nothing" be an object?

No.

Instead:

None is a singleton Python object whose type is NoneType.

Let's unpack that.

None Is an Object

Consider:

x = None

What happens?

Conceptually:

Namespace

x
│
▼
Reference
│
▼

Object

Type: NoneType

Value: None

Notice the pattern.

Exactly like:

42

creates an int object,

and

"hello"

creates a str object,

this:

None

refers to a real object.

What Does None Mean?

It does not mean:

"There is no object."

Instead it usually means:

"There is currently no meaningful value."

Those are very different ideas.

Imagine a hospital system.

patient.middle_name

Some patients have one.

Some don't.

If there isn't one:

middle_name = None

That doesn't mean the variable disappeared.

It means:

"There is no middle name available."

None Is a Singleton

This is a new word.

A singleton means:

Only one instance of that object exists.

For integers:

1
2
3
4
...

Many objects can exist.

For strings:

"hello"
"python"
"AI"

Many objects can exist.

For None:

There is exactly one None object.

Every reference points to that same object.

Why Does This Matter?

Suppose:

x = None
y = None

Now ask:

x is y

What do you think the answer is?

It is:

True

Because both names point to the one and only None object.

Why We Use is

Earlier, we learned:

==

checks value equality.

and

is

checks object identity.

For None, Python recommends:

if x is None:

instead of:

if x == None:

Why?

Because we're checking whether x refers to the singleton None object.

Identity is exactly what we care about.

Where Does None Come From?

Many functions don't return useful data.

Example:

def greet():
    print("Hello!")

Now:

result = greet()

What is result?

Many beginners guess:

"Nothing."

Actually:

result is None

returns:

True

Every Python function returns something.

If you don't explicitly return a value, Python automatically returns the None object.

None Is Not False

This surprises people.

Look:

None == False

returns:

False

None is not the same object as False.

They represent different ideas.

False means a boolean value.
None means "no meaningful value."
But None Is Falsey

Although it isn't False, Python treats it as false in a boolean context.

bool(None)

returns:

False

So:

x = None

if x:
    print("Has value")
else:
    print("No value")

prints:

No value

Notice the distinction:

None is not equal to False.
But None behaves as false in conditions.

That's the same idea we saw with empty strings and empty lists.

Common Use Case — Default Values

Imagine you want to search for a user.

user = find_user("Emmanuel")

If the user exists:

user

might refer to a User object.

If not:

user

could be:

None

Now your program can distinguish between:

"We found a user."
"We didn't find a user."

without inventing fake values.

Why Not Use an Empty String?

Suppose:

name = ""

Does that mean:

The user exists but has an empty name?
The user wasn't found?

You can't tell.

But:

name = None

clearly communicates:

"There isn't a meaningful value here."

Engineer Thinking

Think back to memory.

When you write:

x = None

The variable still references an object.

It's just that the object is the unique None object.

So our object model still holds:

Variable

↓

Reference

↓

Object

Nothing about the model changes.

Connecting to Previous Lessons

Notice how all of these fit together:

42

↓

int

3.14

↓

float

True

↓

bool

"Python"

↓

str

None

↓

NoneType

Every literal you've seen so far creates or refers to an object.

The object model is remarkably consistent.