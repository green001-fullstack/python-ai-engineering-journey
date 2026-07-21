Membership Operators

Python has two membership operators.

Operator	Meaning
in	Is this value contained in this object?
not in	Is this value not contained in this object?

Notice something important.

The question is not:

"Are these objects equal?"

Nor is it:

"Are they the same object?"

Instead, Python asks the object itself:

"Do you contain this value?"

Membership in a List

Suppose:

numbers = [10, 20, 30]

Now:

20 in numbers

Python asks the list:

"Do you contain the value 20?"

The list checks its elements one by one.

10

↓

20

↓

Found!

Result:

True

Now:

40 in numbers

The list checks:

10

↓

20

↓

30

↓

End of list

Nothing found.

Result:

False
Membership in a String

Now suppose:

language = "Python"

Question:

"th" in language

Python searches the string.

Python

Py

yt

th

Found!

Result:

True

Notice:

Strings don't search objects.

They search substrings.

Another example:

"Java" in "Python"

↓

False
Membership in a Dictionary

This surprises almost everyone.

Suppose:

person = {
    "name": "Alice",
    "age": 30
}

Now ask:

"name" in person

Result:

True

Why?

Because dictionaries check keys.

Now:

"Alice" in person

Many beginners expect:

True

But Python returns:

False

Because "Alice" is a value, not a key.

If you want to search values:

"Alice" in person.values()

↓

True
Membership in a Set

Suppose:

fruits = {"apple", "banana", "orange"}

Question:

"banana" in fruits

↓

True

Unlike lists, sets use hashing.

That means membership checks are usually much faster.

We'll learn why when we study dictionaries and sets in depth.

not in

This is simply the opposite.

5 not in [1, 2, 3]

↓

True

because 5 isn't there.

What Does Python Actually Do?

When Python sees:

x in obj

It conceptually asks the object:

"Can you determine whether you contain x?"

Different object types answer differently.

Object	Meaning of in
List	Search elements
Tuple	Search elements
String	Search substring
Dictionary	Search keys
Set	Search elements using hashing

Same operator.

Different behavior.

That's polymorphism.

Engineer Thinking

Imagine Python had different operators.

contains_in_list()

contains_in_string()

contains_in_dictionary()

contains_in_set()

Programming would become much harder.

Instead, Python says:

Use one operator.

Let each object decide how to answer.

Elegant.

Complexity (A Sneak Peek)

You already know Big O from Go and data structures.

Membership isn't equally fast everywhere.

Type	Typical Complexity
List	O(n)
Tuple	O(n)
String	Approximately O(n)
Dictionary	Average O(1)
Set	Average O(1)

Why?

Lists search sequentially.

Sets and dictionaries use hash tables.

We'll study hash tables later, so don't worry if that feels mysterious right now.

Connecting to Previous Lessons

Notice how every operator asks a different question.

Arithmetic:

"What is the result of this calculation?"

Comparison:

"Are these values equal?"

Identity:

"Are these the same object?"

Membership:

"Does this object contain this value?"

Each operator family has a unique purpose.

Real Python Examples

Checking user permissions:

if "admin" in roles:

Checking file extensions:

if ".pdf" in filename:

Checking dictionary keys:

if "email" in user:

Checking prohibited words:

if word in banned_words:

You'll see these patterns constantly in production code.