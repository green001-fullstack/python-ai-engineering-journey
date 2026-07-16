# Question 1

### In your own words, what problem do virtual environments solve?

The problem of multiple projects using different package versions. It helps to avoid dependency conflict.

# Question 2

### Why don't we simply install every package globally?

If we do, python environment can only contain one copy of my package at a time so if there is another project that needs a different version, it may break it.

# Question 3

### Explain this command: python3 -m venv venv. What does each part mean?

python3 means run python, -m means Run a Python module as if it were a program, venv is the module(built in), venv(second one) is the folder name.

# Question 4

### What changes after you activate a virtual environment? What doesn't change?

What changes:

Which Python interpreter is used.
Which packages Python can see.
Which pip installs packages.
Your shell prompt changes to show (venv).

What doesn't change:

CPU
RAM
SSD
Operating System
Terminal
Shell

# Question 5 (Engineer Thinking)

### Suppose you have: Project A, NumPy 1.24 and Project B, NumPy 2.0

### Explain why virtual environments allow both projects to work on the same computer without conflict.

Two separate venv will be created which will be isolated from each other. the different versions can be insatalled on the two venv separately and can run independently without breaking.