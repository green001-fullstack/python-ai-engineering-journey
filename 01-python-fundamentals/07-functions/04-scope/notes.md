# Chapter 7.4 — Scope

## What is Scope?

Scope determines where a variable can be accessed in a program.

Python mainly uses two types of scope:

* Global scope
* Local scope

## Global Variables

A global variable is created outside a function and can be accessed from inside functions.

```python
language = "Python"

def greet():
    print(language)

greet()
```

Output:

```
Python
```

## Local Variables

A local variable is created inside a function and only exists while that function is running.

```python
def student():
    name = "Dime"
    print(name)

student()
```

Trying to access `name` outside the function causes a `NameError`.

## Local vs Global Variables

A local variable can have the same name as a global variable.

```python
score = 90

def exam():
    score = 70
    print(score)

exam()
print(score)
```

Output:

```
70
90
```

The local variable does not change the global variable.

## Common Mistakes

* Trying to access a local variable outside its function.
* Assuming changing a local variable changes the global variable.
* Confusing variables with the same name in different scopes.

## Key Takeaways

* Global variables are defined outside functions.
* Local variables are defined inside functions.
* Functions can access global variables.
* Code outside a function cannot access local variables.
* Variables with the same name can exist in different scopes without affecting each other.
