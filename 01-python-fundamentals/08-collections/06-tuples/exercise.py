# Exercise 1

# Create a tuple named months containing:

# January
# February
# March

# Print the tuple.

months = (January, February, March)
print(months)

# Exercise 2

# Create:

# numbers = (10, 20, 30, 40)

# Print:

# the first element
# the last element using negative indexing

numbers = (10, 20 30, 40)
print(numbers[0])
print(numbers[-1])

# Exercise 3

# Without running the code, determine what happens.

# animals = ("Dog", "Cat", "Rabbit")

# animals[1] = "Lion"

# Explain why.

# ANS : Python raises an error. Reason is because tuples are immutable. 



# Exercise 4

# Create:

# person = ("Ada", 28, "Engineer")

# Unpack the tuple into:

# name
# age
# job

# Print all three variables.

person = ("Ada", 28, "Engineer")

name, age, job = person

print(name)
print(age)
print(job)

# Exercise 5

# Without running the code, determine the output.

# def student():
#     return ("John", 20)

# name, age = student()

# print(name)
# print(age)

# Explain why.

# ANS : John, 20