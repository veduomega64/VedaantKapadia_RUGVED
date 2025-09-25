from math import *
n = input("Enter your credit card number: ")
x = len(n)
b = 0
lst = []
lst_1 = []
lst_2 = []
lst_3 = []
p = 0
for i in range(x):
    lst.append(n[i])
for i in range(x):
    if lst[i] == " ":
        b = b+1
for i in range(b):
    lst.remove(" ")
y = len(lst)
for i in range(y):
    lst[i] = int(lst[i])
for i in range(y):
    if i%2 == 0:
        lst_1.append(lst[i])
    if i%2 != 0:
        lst_2.append(lst[i])
for i in range(len(lst_1)):
    lst_1[i] = 2*lst_1[i]

    if lst_1[i] <= 9:
        p = p+lst_1[i]
    else:
        lst_3.append(lst_1[i]%10)
        a = floor(lst_1[i]/10)
        lst_3.append(a)
for i in range(len(lst_3)):
    p = p+lst_3[i]
for i in range(len(lst_2)):
    p = p+lst_2[i]
if y == 16 or y == 12 or y == 13 or y == 14 or y == 15 and p%10 == 0:
    print("YES it is a valid credit card number")
else:
    print("NO it is not a valid credit card number")