# Question 1

### In your own words, what is a register?

A register is a very small, extremely fast storage location inside the CPU used to hold data that the CPU is actively working with.

# Question 2

### Why are registers built from flip-flops?

Because each flip flop remembers exactly one bit. So it uses many flip flop working together.

# Question 3

### Suppose one flip-flop stores 1 bit. How many flip-flops are needed to build: a. A 1-byte register? b. A 32-bit register? c. A 64-bit register?

1-byte register → 8 flip-flops
32-bit register → 32 flip-flops
64-bit register → 64 flip-flops

# Question 4

### Arrange these from fastest to slowest: RAM, SSD, Register, Cache

Register → Cache → RAM → SSD

# Question 5 (Critical Thinking)

### Imagine a CPU with no registers. Every tiny calculation had to read from RAM and write back to RAM immediately. How do you think that would affect performance? Explain the chain of events, not just the final result.

It will be slower because operations will need to travel farther to the RAM.