# put your python code here
a = int(input())
b = int(input())

nums = [x for x in range(a, b + 1) if x % 3 == 0]
sums = sum(nums)
print(sums / len(nums))
