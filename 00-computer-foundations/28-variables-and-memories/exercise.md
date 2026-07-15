# Question 1

### In your own words, what is a variable?

A variable is a name that describes how to find a data in memory

# Question 2

### Which of these is closer to the truth in Python? A. A variable is a box that contains data. B. A variable is a name that refers to an object stored in memory.

B

# Question 3

### Suppose we execute: x = 42. List the journey of the data from the moment Python executes this line until the CPU performs a calculation using it.

42 is stored in RAM. x is a name that tells us how to find it. If it is needed for calculation, it may be copied into a register. When nothing refers to the object anymore (and if it's not one of Python's cached integers), Python can eventually reclaim the memory.

# Question 4

### Consider: x = 42, y = x. Do we necessarily have two separate copies of 42 in memory? Explain your reasoning.

No, we don't have two copies. Both x and y are pointing to the same object.

