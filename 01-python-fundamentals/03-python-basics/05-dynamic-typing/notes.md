# Dynamic Typing

Dynamic typing means that names are not restricted to one type of object. A name can be rebound to objects of different types during program execution.

Notice how this definition uses everything we've already learned.

It doesn't say:

"Variables change type."

Because variables don't have types.

Objects do.

Compare with Go

In Go:

var x int = 10

Later:

x = "Hello"

The compiler says:

❌ Error.

Why?

Because in Go:

The variable has a declared type (int).
Only integers can be assigned to it.

In Python:

x = 10
x = "Hello"
x = [1, 2, 3]
x = {"name": "Emmanuel"}

All of these are valid.

Why?

Because x is just a name.

Visualizing It
Step 1
x = 10
x
│
▼
[int object]
Step 2
x = "Hello"
[int object]

x
│
▼
[string object]
Step 3
x = [1, 2, 3]
[int object]

[string object]

x
│
▼
[list object]

The name keeps moving.

The objects stay what they are.

Why This Is Powerful

Imagine writing a function:

def show(value):
    print(value)

You can call it with:

show(10)
show("Hello")
show([1, 2, 3])
show(True)

The function doesn't care.

It simply receives a reference to an object.

But Isn't This Dangerous?

Good question.

If Python lets you do anything...

What happens if you write:

x = 10
x.append(5)

Python doesn't silently ignore it.

It raises an error.

Why?

Because the object currently bound to x is an integer.

Integers don't support append().

Python checks the object's type at runtime.

Static vs Dynamic Typing
Static Typing (Go)	Dynamic Typing (Python)
Variables have declared types	Names have no type
Type checked mostly before running	Type checked while running
Compiler catches many type errors early	Runtime catches invalid operations when executed

Neither approach is "better." They make different trade-offs.

Dynamic Typing Does Not Mean "No Types"

This is a very common misunderstanding.

People sometimes say:

"Python has no types."

That's false.

Python has very strong typing.

Every object has a type.

The difference is when the type is checked.

Let's Connect Everything

Suppose you write:

x = 10

Python does:

Name
│
▼
Reference
│
▼
Object
Type: int

Later:

x = "Python"

Now:

Name
│
▼
Reference
│
▼
Object
Type: str

Nothing magical happened.

Only the binding changed.

Engineer Thinking

Imagine Python forced names to have types.

Then every assignment would require checking:

"Is this allowed?"

Python deliberately chooses flexibility.

Instead of typing the name, it types the object.

This design is one of the reasons Python is so expressive.