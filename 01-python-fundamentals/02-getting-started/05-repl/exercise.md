# Question 1

### What does REPL stand for?

R → Read
E → Evaluate
P → Print
L → Loop

# Question 2

### Why does this work without saving anything to a file?

>>> x = 10
>>> x
10

Because the interpreter process is still alive. The variable will still remain in memory until the interpreter exits or quits.
The interpreter is a running process.
Variables exist inside that process's memory.
When the process dies...
The memory disappears.


# Question 3

### What is the difference between these prompts? $ and >>>

$	Bash (Shell) is waiting for a command
>>>	Python REPL is waiting for Python code

Question 4

What happens to all your variables when you exit the REPL? Why?

It vanish from memory. Because:

The interpreter process ends.
The operating system reclaims its memory.
The variables no longer exist

Question 5 (Engineer Thinking)

Suppose the REPL did not loop.

Instead, after evaluating one line, it immediately exited.

Would it still be useful?

What would you lose?


It won't be useful. All the memory will be lost.