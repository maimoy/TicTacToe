numbers = []

while True:
    a = input()
    if a != '.':
        a = float(a)
        numbers.append(a)
    else:
        break

min_number = min(numbers)
print(min_number)


