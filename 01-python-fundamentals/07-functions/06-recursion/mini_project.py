def sum_numbers(number):
    if number == 1:
        return 1
    return number + sum_numbers(number - 1)

print(sum_numbers())