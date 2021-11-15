word = input()

list1 = list(word)

list2 = []
i = len(word)
i -= 1
while i >= 0:
    c = list(word)[i]
    list2.append(c)
    i -= 1

if str(list1) == str(list2):
    print("Palindrome")
else:
    print("Not palindrome")
