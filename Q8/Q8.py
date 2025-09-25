import sys

str = input("Enter a string: ")
n = int(input("Enter the number u want the string to be divided into: "))
x = len(str)
lst = []
z = ""
a = 0
d = 0
fg = 0
for i in range (0,x):
    y = str[i]
    lst.append(y)
lst.sort()
for i in range(0, x-1):
    if lst[i] != lst[i + 1]:
        d = d + 1
for i in range (0,d):
    a = 0
    fg = 0
    for i in range (0,n):
        if lst[i] == lst[i-1]:
            a = a+1
        else:
            fg = fg +1
    if a == n-1 :
        y = lst[0]
        for i in range (0,n):
            lst.remove(y)
        z = z+y
    if fg == 2 and lst[0] == z[i] :
        print("A certain letter is repeated more than the required number of that letter")
        sys.exit()
    if fg == 2 and lst[0] != z[i]:
        print("A certain letter is repeated less times than the required number of that letter")
        sys.exit()
if len(lst) == n:
    z = z + lst[0]
    for i in range (0,n):
       print(z,end=" ")
elif len(lst) >= n:
    print("A certain letter is repeated more than the required number of that letter")
else:
    print("A certain letter is repeated less than the required number of that letter")
