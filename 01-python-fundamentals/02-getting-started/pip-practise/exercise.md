# Question 1

### What is pip?

It is a package manage. A package manager manages the lifecycle of packages: Install, Upgrade, Remove, List

# Question 2

### What is the difference between: pip install numpy and import numpy

pip helps to install the package from a third party while import is what helps to find it after installation

# Question 3

### Why is it recommended to activate your virtual environment before installing packages?

Because it will help to isolate it into the venv folder and not get installed into the system python environment. This helps to avoid dependency conflict.

# Question 4

### What is the purpose of a requirements.txt file?

A requirements.txt file tells another developer:

which packages the project needs,
which versions of those packages to install.

For example:

numpy==2.2.0
torch==2.8.0
pandas==2.3.0

This ensures that everyone working on the project has a consistent environment.

# Question 5 (Engineer Thinking)

### Suppose you clone an AI project from GitHub. It contains: requirements.txt but no venv folder. Why do you think the virtual environment itself is not usually committed to Git? Think about what you've learned regarding isolation, storage, and reproducibility.

Suppose you clone my AI project.

You download:

project/
    main.py
    requirements.txt

But not:

venv/

Why?

Think about these questions:

Question A

Can every developer create their own virtual environment by running:

python3 -m venv venv

Yes.

Question B

If they already have requirements.txt, can they recreate all the packages?

pip install -r requirements.txt

Yes.

Question C

If the virtual environment can always be recreated, do we really need to store thousands of installed package files in Git?

No.

That would make the repository unnecessarily large.

Instead, we store the recipe (requirements.txt), not the cooked meal (venv).

I like to use this analogy:

requirements.txt is like a shopping list.
The venv is like the groceries in your kitchen.

When I share a recipe with you, I don't ship my entire kitchen. I give you the shopping list so you can buy the ingredients yourself.

That's exactly what happens with Python projects.