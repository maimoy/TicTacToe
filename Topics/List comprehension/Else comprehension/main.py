# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [1 if x > 0 else 0 for x in old_list]  # your code here
print(binary_list)
