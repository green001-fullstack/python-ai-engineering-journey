# Question 1

### What does a type conversion function do? Does it modify an object or create a new one? Explain why.

A type conversion function creates a new object of the requested type. It does not modify the original object. This is consistent with Python's immutable built-in types.

# Question 2

### Walk through this line step by step: age = int(input("Age: "))

When the characters are typed on the keyboard, they are collected as strings because our keyboard does not know data types. the number collected is now converted into integer by creating a new object. The age variable will then bind to the result.

# Question 3

### Why does this return True? bool("False")

Because the string is not empty.

# Question 4

### Why does this fail? int("hello") What is Python trying to do?

Because the string does not contain convertible integers.

Python tries to interpret: "hello" as a decimal integer.

It can't. So it raises: ValueError because it cannot create a valid int object from those characters.

# Question 5 (Engineer Thinking )

Suppose Python allowed conversions to modify objects instead of creating new ones.

For example:

x = "25"

int(x)

actually changed the original "25" string object into the integer 25.

Can you think of two problems this would create?

Think about shared references and immutability.