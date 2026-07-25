# Exercise 1

# Create a decorator that prints:

# Start

# before the function runs.

# Decorate:

# def hello():
#     print("Hello")

def decorator(function):
    def wrapper():
        print("Start")
        function()
    return wrapper

@decorator
def hello():
    print("hello")
hello()

# Exercise 2

# Modify the decorator so it prints:

# Start
# Hello
# End

def decorator(function):
    def wrapper():
        print("Start")
        function()
        print("End")
    return wrapper

@decorator
def hello():
    print("hello")
hello()

# Exercise 3

# Create a decorated function named:

# def welcome():
# that prints:

# Welcome to Python

def decorator(function):
    def wrapper():
        function()
    return wrapper

@decorator
def welcome():
    print("Welcome to Python")
welcome()

# Exercise 4

# Without running the code:

def decorator(function):

    def wrapper():
        print("Before")

        function()

        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()

# What is the output?

# Explain.

# ANS : Before, Hello, After

# Exercise 5

# Without running the code:

def decorator(function):

    def wrapper():
        print("Running")

        function()

    return wrapper


@decorator
def test():
    print("Python")


test()

# What prints?

# Why?

Running, Python