# The Complete Table

A	B	XOR (Sum)	AND (Carry)	Final Answer
0	0	0	0	0
0	1	1	0	1
1	0	1	0	1
1	1	0	1	10


CPU

↓

Arithmetic Logic Unit (ALU)

↓

Adders

↓

Logic Gates

↓

Transistors

↓

Electricity

# Why XOR and AND together are enough to add two single bits

Adding two single bits requires calculating two values: a sum bit and a carry bit. An XOR gate perfectly calculates the sum bit because it outputs a 1 only when exactly one of the inputs is 1 (e.g., \(1 \oplus 0 = 1\) and \(0 \oplus 1 = 1\)), while correctly resulting in 0 when adding two ones (\(1 \oplus 1 = 0\)). Concurrently, an AND gate perfectly calculates the carry bit because it outputs a 1 only when both inputs are 1 (1 ⋅ 1 = 1), representing the value carried over to the next column. Together, these two gates form a half adder, combining logic to completely and accurately represent binary addition for two single bits