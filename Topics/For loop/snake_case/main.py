word = input()
result = ""
for i in word:
    if i.isupper() is True:
        result = result + "_" + i.lower()
    else:
        result += i

print(result)
