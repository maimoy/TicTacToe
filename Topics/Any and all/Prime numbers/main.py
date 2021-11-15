prime_numbers = [x for x in range(2, 1000) if all((x % j) != 0 for j in range(2, x - 1))]
