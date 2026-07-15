Question 2: What is the job of the Program Counter (PC)?
The PC is a special register that holds the memory address of the next instruction to be executed. Its entire job is to keep track of "where we are" in a program's execution sequence, so the CPU always knows what to fetch next. After each instruction executes, the PC updates (usually incrementing) to point to the following instruction — unless a jump, branch, or function call explicitly changes it to point somewhere else.
Question 3: PC = 200. What happens during the fetch stage?

The CPU takes the address currently in the PC (200)
It sends that address to RAM (via the address bus) and requests the instruction stored there
RAM returns the instruction located at address 200 (via the data bus)
That instruction is loaded into the Instruction Register (IR)
The PC then updates — typically incrementing to 201 (or 204, 208, etc., depending on instruction size) — so it's ready to point to the next instruction once this one finishes executing

So fetch is essentially: "go get the instruction sitting at the address the PC is pointing to, then update the PC to point past it."
Question 4: Why copy data into registers instead of working directly from RAM?
Speed, primarily — and by a huge margin:

Registers live inside the CPU itself, built from extremely fast circuitry, and can be accessed in a single clock cycle
RAM is physically separate from the CPU, connected via a bus, and accessing it takes dramatically longer (tens to hundreds of clock cycles) due to physical distance and the way memory is architected
The CPU's arithmetic/logic unit (ALU) is also wired to operate on registers directly — it can't perform operations straight on RAM addresses
If the CPU had to fetch from RAM for every single operation, performance would collapse — this is the whole reason the "memory hierarchy" (registers → cache → RAM → disk) exists, trading off speed against capacity/cost

Registers are small and expensive, but blazing fast — RAM is large and cheap, but comparatively slow. Copying data into registers temporarily is a deliberate performance optimization baked into CPU design.
Question 5 (Critical Thinking): What if the PC stopped updating?
If the PC froze at some value — say it stayed at 200 forever — the CPU would keep fetching, decoding, and executing the same instruction at address 200 over and over, indefinitely.
The program would not continue normally. Here's why:

The CPU has no other mechanism for "knowing what's next" — the PC is the sequencing mechanism. Without it advancing, there is no next instruction; there's only ever "now."
You'd essentially get an infinite loop executing one single instruction repeatedly
Depending on what that instruction does, the effect differs: if it's something like ADD R1, R2, that operation would just repeat uselessly forever; if it were a jump instruction, it might jump to the same place ad infinitum
The rest of the program — every instruction after address 200 — would never execute, because the CPU has no way to reach it without the PC advancing

This is actually a great illustration of why the PC is so fundamental: it's not just bookkeeping, it's the literal mechanism that gives a program its sequence and forward motion. Without it, a CPU is just a machine that can do one operation, forever, with no concept of "next."