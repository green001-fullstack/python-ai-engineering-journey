# Exercise 1

# Write a lambda function that squares a number.

# Store it in a variable called square.

# Call it with:

square = lambda x : x * x

print(square(6))

# Exercise 2

# Write a lambda function that adds two numbers.

# Call it with:

# print(add(10, 5))

# Expected output:

# 15

add = lambda x, y : x + y

print(add(10, 5))

# Exercise 3

# Write a lambda function that returns "Adult" if age is at least 18; otherwise "Minor".

# Call it with:

# print(check_age(20))
# print(check_age(15))

# Expected output:

# Adult
# Minor

check_age = lambda x : "Adult" if x > 18 else "Minor"

print(check_age(20))
print(check_age(15))


# Exercise 4

# Without running the code, determine the output.

# multiply = lambda a, b: a * b

# print(multiply(4, 5))

# Explain why.

# ANS : 20

# Exercise 5

# Without running the code, determine the output.

# greet = lambda name: "Hello " + name

# print(greet("Ada"))

# Explain why.

# ANS : Hello Ada