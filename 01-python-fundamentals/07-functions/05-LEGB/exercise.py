

name = "Global"

def show():
    print(name)

show()

Explain why.

# ANS : Global. name exists globally

# Exercise 2

# Predict the output.

name = "Global"

def show():

    name = "Local"

    print(name)

show()

print(name)

# Explain why the outputs are different.

# ANS : Local, then Global. 

# Exercise 3

# Predict the output.

def outer():

    message = "Python"

    def inner():
        print(message)

    inner()

outer()

# Which part of LEGB is used?
# ANS : Enclosed

# Exercise 4

# Without running the code:

number = 20

def demo():
    value = 10
    print(number)
    print(value)

demo()

# What prints?

# Why?

# 20 and then 10

# Exercise 5

# Without running the code:

def test():
    print(age)

test()

# Assume age has never been defined.

# What happens?

# Explain using LEGB.

# ANS : naming error. it will search local, enclosed, global and built-in. It wont find it so it will display that error. 