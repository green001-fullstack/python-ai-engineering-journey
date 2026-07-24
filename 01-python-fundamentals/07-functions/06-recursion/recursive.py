# Exercise 1

# Write a recursive function:

# def countdown(number):

# It should print numbers from the given number down to 1.

# Example:

# countdown(5)

# Output:

# 5
# 4
# 3
# 2
# 1

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)




# Exercise 2

# Write a recursive function:

# def countup(number):

# It should print numbers from 1 up to the given number.

# Example:

# countup(5)

# Output:

# 1
# 2
# 3
# 4
# 5

def countdown(number):
    if number == 0:
        return
    countdown(number - 1)
    print(number)
countdown(5)


# Exercise 3

# Complete the recursive factorial function:

# def factorial(number):
#     if number == 1:
#         return 1

#     # Complete this line

# Test it with:

# factorial(4)

# Expected output:

# 24

def factorial(number):
    if number == 1:
        return 1
    return n * factorial(number -1)



# Exercise 4

# Without running the code, determine the output.

# def hello(number):
#     print(number)

#     if number > 1:
#         hello(number - 1)

# hello(3)

# Explain each step.

# ANS : 3, 2, 1

# Exercise 5

# Without running the code:

# def test():
#     print("Python")
#     test()

# test()

# What happens?

# Why?

# ANS : It runs forever because there is no base case