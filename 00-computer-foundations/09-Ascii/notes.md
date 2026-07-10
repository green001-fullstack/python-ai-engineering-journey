### How does a computer carry information? → Electricity
### How does it represent electrical states? → Binary
### What is the smallest unit? → Bit
### Why do we group them? → Byte

# ASCII

ASCII stands for: American Standard Code for Information Interchange.
The important idea is:
ASCII is a dictionary. It maps numbers to characters. 

# Think of ASCII as a Dictionary

## Imagine a dictionary like this:

### Number	Character
### 65	        A
### 66	        B
### 67	        C
### 68	        

# Engineer Insight 🔬

When you eventually write Python like this:

name = "AI"

Python stores the characters "A" and "I" internally using character encoding.

When Python needs to write that string to a file or send it over the internet, those characters become bytes.

Those bytes become bits.

Those bits become electrical signals.


"Characters are not stored directly. They are encoded into numbers, and those numbers are stored as binary."