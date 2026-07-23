# Chapter 7.1 — Function Basics

## What is a Function?

A function is a reusable block of code that performs a specific task. Functions help reduce repetition, organize code, and make programs easier to read and maintain.

## Defining a Function

Functions are created using the `def` keyword.

```python
def greet():
    print("Hello!")
```

Defining a function only tells Python what the function should do. It does **not** execute the function.

## Calling a Function

A function runs only when it is called.

```python
def greet():
    print("Hello!")

greet()
```

Output:

```
Hello!
```

A function can be called multiple times without rewriting its code.

## Define vs Call

* **Define:** Create the function.
* **Call:** Execute the function.

This is one of the most important concepts in Python.

## Benefits of Functions

* Reduce duplicate code.
* Improve readability.
* Make programs modular.
* Allow code to be reused.

## Common Mistakes

* Forgetting to call a function after defining it.
* Calling a function before it has been defined.
* Forgetting parentheses (`greet()` vs `greet`).
* Incorrect indentation inside the function body.

## Key Takeaways

* Use `def` to define a function.
* A function does nothing until it is called.
* The same function can be called multiple times.
* Functions make programs cleaner and easier to maintain.
