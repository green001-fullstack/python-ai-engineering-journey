# Question 1

### In your own words, what is cache?

Cache is a performance optimization which serves as a bridge between RAM and CPU registers by holding copies of recently or frequently accessed data that the CPU may need when running a program.

# Question 2

### Why isn't RAM alone enough for modern CPUs?

RAM alone will make CPU to be waiting for data every time it needs them from the RAM and if there are a lot of data that is needed, it will waste too much time getting them.

# Question 3

### Explain the difference between a cache hit and a cache miss.

Cache hit means if a data is need and it checks the cache and finds it, then it wont need to go and search for it in RAM. It will just make use of it there. For Cache miss, if it searches for it in cache and not find it, it will go in search of it in RAM and after finding it, it will save it in cache so that when next it needs same data, it wont have to start searching inside RAM again, it is already inside cache

# Question 4

### Suppose you're looping through a Python list:

### for x in numbers:
### print(x)

### Why does cache help this code run efficiently?

If it is already inside a small memory(cache), it does not have to go into RAM and be waiting for the values before printing them, it will just grab it from the memory.

# Question 5 (Critical Thinking)

### Imagine a computer with no cache. The CPU still has registers and RAM. Describe what happens when the CPU repeatedly needs data from RAM.

The CPU will have to wait every time it needs the data from RAM. This will affect the performance as it will be slower