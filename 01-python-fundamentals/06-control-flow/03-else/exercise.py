# Exercise 1

# Create a variable age.

# If age is at least 18, print "Adult".
# Otherwise, print "Minor".

# Solution
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Exercise 2
# Create a variable password.

# If it equals "python123":

# Access Granted

# Otherwise:

# Access Denied

# Solution
password = "python123"

if password == "python123":
    print("Access Granted")
else:
    print("Access DEnied")


# Exercise 3
# Create a variable marks.

# Print:

# "Excellent" if marks are at least 90.
# "Good" if marks are at least 70.
# "Pass" if marks are at least 50.
# "Fail" otherwise.

# Solution
marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 70:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")



# Exercise 4
# Create a variable balance.

# If the balance is enough to withdraw 5000:

# Transaction Successful

# Otherwise:

# Insufficient Funds

# Solution
balance = 2000

if balance > 5000:
    print("Transaction Successful")
else:
    print("Insufficient funds")


# Exercise 5 (Tracing)

# Without running the code, determine the output.

temperature = 12

if temperature >= 35:
    print("Hot")

elif temperature >= 20:
    print("Warm")

else:
    print("Cold")

# Solution

Cold