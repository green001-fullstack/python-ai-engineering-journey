# Lesson 1 — Variables

Let's begin with a question.

Imagine I say:

Emmanuel lives in Lagos.

Now I ask:

What does the name Emmanuel represent?

Does it represent the actual human being?

Or is it simply a name that refers to a human being?

It's the second one.

The name isn't the person.

The name is how we refer to the person.

Keep that thought.

The Traditional Explanation

Most programming books draw this picture:

x
│
▼
+----+
| 10 |
+----+

They say:

"A variable is a box that stores a value."

This is a useful teaching model.

But in Python...

It isn't really true.

Think About Memory

Remember our lesson on RAM.

RAM contains:

bytes,
addresses,
objects.

It does not contain variables.

Think carefully.

When Python runs:

x = 10

Where does the integer 10 live?

In memory.

But where does the name x live?

That's today's mystery.

Let's Watch Python Think

Imagine Python executing:

x = 10

Does it first create the variable?

Or does it first create the integer object?

The answer is:

Create the integer object 10.
Bind the name x to that object.

Notice the wording.

I did not say:

Store 10 inside x.

I said:

Bind the name x to the object.

That single word—bind—is fundamental to Python.

Variables Are Names

In Python:

A variable is a name bound to an object.

Read that again.

Not:

A box.

Not:

A container.

A name.

Imagine Sticky Notes

Suppose we have an object in memory:

        Integer Object
      +-------------+
      |     10      |
      +-------------+

Now imagine putting a sticky note on it.

The sticky note says:

x

Now we have:

x
│
▼
+-------------+
|     10      |
+-------------+

The sticky note isn't the object.

It simply tells us which object we're talking about.

What Happens Next?

Now execute:

y = x

What happens?

Many beginners imagine:

x → 10

y → 10 (new copy)

But that's not what Python does.

Instead:

      +-------------+
      |     10      |
      +-------------+
        ▲         ▲
        │         │
        x         y

There is still one integer object.

Now there are two names referring to it.

Nothing was copied.

This idea is so important that we'll spend an entire lesson on references soon.

Rebinding

Now watch this carefully.

x = 10

Later:

x = 20

Did Python change the integer 10 into 20?

No.

Instead:

Before

x
│
▼
10

Then:

x = 20

After:

10

20
▲
│
x

The name moved.

The object didn't.

Python simply rebound the name x to a different object.

What Happened to 10?

Good question.

If nothing refers to it anymore:

10

Python is free to remove it later through garbage collection.

We'll study that much later.

Why This Matters

This explains something you've probably wondered about.

Suppose:

x = [1, 2, 3]
y = x

If variables were boxes...

Changing one shouldn't affect the other.

But in Python:

Both names refer to the same list.

We'll see this later:

y.append(4)

Now:

x

also appears changed.

Why?

Because there was only one list object.

Connecting to Go

You once asked me:

"Are Python variables behaving like pointers in Go?"

Now you have enough background to appreciate the answer.

They are similar in behavior, but not the same concept.

In Go:

x := &person

x explicitly stores an address (a pointer).

In Python:

x = person

x is a name bound to an object.

Python deliberately hides the underlying memory addresses from everyday programming.

So while the behavior often resembles pointers, Python's model is about names and object references, not explicit pointer manipulation.

We'll make this distinction crystal clear when we study references.

Common Beginner Mistakes
Mistake 1

Thinking:

Variables contain objects.

In Python, names refer to objects.

Mistake 2

Thinking:

y = x

copies the object.

Usually, it doesn't.

Mistake 3

Thinking:

x = 20

changes the integer 10.

It doesn't.

It simply changes which object the name refers to.

### 🧠 Engineer Thinking

Notice how this connects to our Computer Foundations course.

Earlier we learned:

RAM stores data.
Variables help us find data.

Python follows exactly that idea.

The object lives in memory.

The variable is the human-friendly name Python uses to refer to that object.

In other words:

RAM
│
├── Integer Object 10
├── Integer Object 20
└── List Object

Python Namespace
│
├── x
├── y
└── numbers

The namespace is like a dictionary of names that point to objects in memory.

# TAKE NOTE

We said RAM stores data.

Now let's imagine this Python code:

x = 10
name = "Emmanuel"
numbers = [1, 2, 3]

Your computer might conceptually look like this:

RAM
─────────────────────────────────

Address A
+----------------+
| Integer: 10    |
+----------------+

Address B
+----------------+
| String         |
| "Emmanuel"     |
+----------------+

Address C
+----------------+
| List           |
| [1, 2, 3]      |
+----------------+

Now, where are the variable names?

Not inside those objects.

Python keeps a separate mapping (often called a namespace):

Namespace

x       ─────────► Address A

name    ─────────► Address B

numbers ─────────► Address C

So when you write:

print(x)

Python doesn't search RAM for something literally called x.

It first looks in the namespace:

"What object is the name x bound to?"

The namespace answers:

"The integer object at Address A."

Then Python uses that object.

This is why I kept saying that variables are names, not storage boxes.