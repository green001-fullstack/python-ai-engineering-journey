# Chapter 7.2 — Parameters

## What are Parameters?

A parameter is a variable defined in a function that allows the function to receive input values. Parameters make functions flexible and reusable.

## What is an Argument?

An argument is the actual value passed to a function when it is called.

Example:

```python
def greet(name):
    print("Hello,", name)

greet("Emmanuel")
```

* `name` is the **parameter**.
* `"Emmanuel"` is the **argument**.

## Multiple Parameters

A function can accept more than one parameter.

```python
def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce("Dime", 25)
```

## Benefits of Parameters

* Make functions reusable.
* Reduce duplicate code.
* Allow the same function to work with different data.
* Improve code organization.

## Common Mistakes

* Forgetting to pass the required arguments.
* Passing too many or too few arguments.
* Confusing parameters with arguments.
* Swapping the order of arguments when position matters.

## Key Takeaways

* Parameters are variables inside a function definition.
* Arguments are the values passed to a function.
* Functions can have one or many parameters.
* Parameters make functions flexible and reusable.
