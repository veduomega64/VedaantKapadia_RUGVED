str = input("Enter a string: ")
x = len(str)
lst = []
str2 = ""
for i in range (0,x):
    y = str[i]
    lst.append(y)
lst.sort()
for b in range (0,x):
    print(lst[b] + "'s count is ", end="")
    print(b)
    z = lst[b]
    str2 = str2 + z
print(str2)
