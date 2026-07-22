for num in range(1, 11):
    if num == 5:
        continue



for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)



count = 0
while count <= 4:
    count += 1
    if count == 4:
        continue
    print(count)


# Without running the code, determine the output.

for i in range(1, 6):

    if i == 2:
        continue

    print(i)

print("Done")

ANS : 1, 3, 4, 5, "Done"

# Without running the code, determine the output.

count = 0

while count < 5:

    count += 1

    if count == 4:
        continue

    print(count)

ANS : 1, 2, 3, 5