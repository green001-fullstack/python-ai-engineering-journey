# Question 1

### Explain the difference between: == and is using the words value and identity.

== → "Do these objects represent the same value?"
is → "Are these two references pointing to the exact same object?"

# Question 2

### Why is this the preferred style?

### if result is None:

### instead of:

### if result == None:

Because there is only one singleton None NoneType. == can be customized by objects (through the __eq__ method), is cannot.

# Question 3

### Suppose:

### a = [1, 2]
### b = a

### Predict:

### a == b

### and

### a is b

### Explain why.

True, True. Both names are pointing to the same object and so the values too are same

# Question 4

### Suppose:

### a = [1, 2]
### b = [1, 2]

### Predict:

### a == b

### and

### a is b

### Explain why.

True, False. Both are different objects containing same value

# Question 5 (Engineer Thinking)

### Suppose someone writes: if username is "admin":

### Explain why this is not the correct operator, even if it appears to work sometimes.

We are only interested if the text in username(value) matches the value in admin. It may fail because both of them are not the same object, so even if they contain the same value, the fact that is only compares there identity will make them fail because they are different objects.
Sometimes it appears to work because CPython may intern (reuse) some strings as an optimization. For example:

a = "admin"
b = "admin"

print(a is b)

might print True on one implementation.

But that's an implementation detail, not something your code should rely on.

The programmer's intent is:

"Does this username equal 'admin'?"

That's a value question, so == is the correct operator.