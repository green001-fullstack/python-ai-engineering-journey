# Chapter 8.1 — Lists

## What is a List?

A list is an ordered, mutable collection of items. Lists can store multiple values in a single variable.

## Creating a List

```python
fruits = ["Apple", "Banana", "Orange"]
```

## Accessing Elements

Lists use zero-based indexing.

```python
print(fruits[0])   # Apple
print(fruits[-1])  # Orange
```

Negative indexing starts from the end of the list.

## Modifying Elements

Lists are mutable, so their elements can be changed.

```python
fruits[1] = "Mango"
```

## Adding Elements

Add to the end:

```python
fruits.append("Orange")
```

Insert at a specific position:

```python
fruits.insert(1, "Mango")
```

## Removing Elements

Remove by value:

```python
fruits.remove("Banana")
```

Remove by index:

```python
fruits.pop(0)
```

Remove the last item:

```python
fruits.pop()
```

## Finding the Length

```python
len(fruits)
```

Returns the total number of items in the list.

## Iterating Through a List

```python
for fruit in fruits:
    print(fruit)
```

## Key Takeaways

* Lists are ordered collections.
* Lists are mutable.
* Indexing starts at 0.
* Negative indexing counts from the end.
* `append()` adds to the end.
* `insert()` adds at a specific position.
* `remove()` removes by value.
* `pop()` removes by index (or the last item if no index is provided).
* `len()` returns the number of elements.
