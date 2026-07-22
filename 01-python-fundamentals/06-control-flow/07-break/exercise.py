for number in range(1, 11):
    print(number)
    if number == 6:
        break


count = 1
while True:
    print(count)
    if count == 4:
        break
    count += 1


for num in range(1, 100):
    print(num)
    if num == 8:
        print("Found")
        break


# Without running the code, determine the output.
for i in range(1, 6):
    if i == 4:
        break

    print(i)

print("Finished")

ANS : 1,2,3, "Finished"


# Without running the code, determine the output.
count = 1

while True:
    print(count)

    if count == 3:
        break

    count += 1

print("Loop Ended")

ANS : 1, 2, 3, "Loop Ended"