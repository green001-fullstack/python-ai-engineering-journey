# Python Iterators — The Iterator Protocol

## Iterable vs Iterator

### Iterable

An iterable is an object that can produce an iterator.

Examples:

- list
- tuple
- string
- dictionary
- set
- range
- file objects

An iterable stores data but does **not** track iteration state.

---

### Iterator

An iterator is an object that remembers the current position while traversing an iterable.

It provides values one at a time using the `next()` function.

```python
numbers = [10, 20, 30]

it = iter(numbers)
```

---

## The Iterator Protocol

Python iteration follows two fundamental operations:

1. Create an iterator

```python
it = iter(numbers)
```

2. Request the next value

```python
next(it)
```

When no values remain, the iterator raises:

```python
StopIteration
```

---

## How a `for` Loop Works

The statement

```python
for item in numbers:
    print(item)
```

is conceptually equivalent to:

```python
it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
```

The `for` loop silently catches the `StopIteration` exception to end iteration gracefully.

---

## Why Iterators Exist

Iterators allow Python to process data one element at a time.

Benefits:

- Low memory usage
- Streaming large datasets
- Processing files efficiently
- Supporting generators
- Foundation of data pipelines in AI

---

## Mental Model

Think of an iterable as a bookshelf.

Think of an iterator as a reader holding a bookmark.

The bookshelf stores books.

The reader remembers where they are.

---

# Key Takeaways

- Iterables produce iterators.
- Iterators remember position.
- `next()` advances the iterator.
- `StopIteration` signals completion.
- `for` loops are built on the iterator protocol.