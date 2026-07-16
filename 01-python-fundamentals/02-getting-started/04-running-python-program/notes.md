If you opened hello.py in a basic text editor like Notepad, you'd see:

print("Hello, World!")

Nothing more.

The .py extension simply tells humans—and many tools—that this file contains Python source code.

What Happens When You Run It?

Let's trace the entire journey.

You type:

python3 hello.py
Step 1 — The Terminal

The terminal receives your keystrokes.

Keyboard
      ↓
Terminal
Step 2 — The Shell

The shell reads:

python3 hello.py

It separates it into:

Program to execute:

python3

Argument:

hello.py

The shell then asks the operating system:

"Please start the program named python3 and give it this file."

Step 3 — The Operating System

The operating system finds the Python interpreter.

It loads it into memory.

Then it starts executing it.

Remember:

The interpreter itself is just another program.

Step 4 — Python Opens Your File

The interpreter reads:

print("Hello, World!")

from the text file.

At this point, it hasn't executed anything yet.

It has only read the source code.

Step 5 — Compilation to Bytecode

CPython compiles the source into Python bytecode.

Conceptually:

Source Code
      ↓
Bytecode

This happens automatically and very quickly.

Step 6 — Python Virtual Machine

The Python Virtual Machine begins executing the bytecode.

It encounters an instruction that corresponds to:

print("Hello, World!")
Step 7 — Calling print

This is an important moment.

print is not a keyword.

It is a function.

A function is simply a reusable piece of code that performs a task.

The task of print is:

Display text on standard output.

We'll study functions in depth later.

For now, think of print as asking Python:

"Please display this text."

Step 8 — Standard Output

Where does the text go?

The print function writes to something called standard output, often shortened to stdout.

In a terminal session:

stdout
      ↓
Terminal Window

That's why you see:

Hello, World!

appear in the terminal.

If you redirected stdout to a file instead, the text would go into that file.