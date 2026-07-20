# Question 1

### In your own words, what is None?

It is an immutable singleton python object with the data type NoneType

# Question 2

### What does it mean that None is a singleton?

It means there is only one instance of it.

# Question 3

### Why is this recommended? if x is None: instead of: if x == None:

Because there is just a single instance of None so identity is preferred to equality.

# Question 4

### What happens here? def greet():
###                     print("Hello")

### result = greet()

### What object does result reference? Why?

Result references the singleton None object because every Python function returns a value, and if no explicit return is given, Python returns None automatically.

# Question 5 (Engineer Thinking)

### Suppose a function returns a user's age. Would you rather return: 0 or None when the user doesn't exist? Why?


I would return None because 0 is still a value. If the age doesnt exist, it is proper to return a data type that represent something of no meaningful value and this is what None represents