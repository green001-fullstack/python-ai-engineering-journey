# Visualizing It


Carry In
     │
     ▼
  +---------+
A→|         |
B→| Full    |
  | Adder   |
  +---------+
     │
 ┌───┴─────┐
 ▼         ▼
Sum    Carry Out

# How Do We Build One?

This is the beautiful part.

We don't invent a completely new machine.

We build it from pieces we already know.

A Full Adder is made from:

Two Half Adders
One OR gate

That's it.

# Step 1 — First Half Adder

We first add:

A

+

B

Outputs:

Sum1

Carry1

## Diagram:

A ─────┐
       ▼
      Half
      Adder
       ▲
B ─────┘

↓

Sum1

Carry1


# Step 2 — Second Half Adder

Now we still need to add the incoming carry.

So we take: Sum1 + Carry In

Outputs:

Final Sum

Carry2

## Diagram:

Sum1 ───┐
         ▼
       Half
       Adder
         ▲
Carry In─┘

↓

Sum

Carry2

# Step 3 — Combine the Carries

Now we have:

Carry1

Carry2

If either carry is 1...

We should pass a carry to the next column.

Which gate should combine them?

Think.

We want:

"If Carry1 OR Carry2 is true..."

Exactly.

We use an OR gate.

Carry1 ─┐
         ▼
        OR
         ▲
Carry2 ──┘

↓

Carry Out

# The Entire Circuit

Putting everything together:

          A ───────┐
                   ▼
              +-----------+
B ───────────►| HalfAdder |
              +-----------+
                 │      │
              Sum1   Carry1
                 │
                 ▼
             +-----------+
Carry In ───►| HalfAdder |
             +-----------+
                │      │
             Sum   Carry2
                       │
Carry1 ────────────────┐
                       ▼
                     +----+
                     | OR |
                     +----+
                       │
                 Carry Out