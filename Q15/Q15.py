n = int(input("Order of the square matrix is:"))
lst_2 = []
a = 0
b = 0
lst_3 = []
lst_4 = []
for i in range(n):
    lst_1 = []
    for j in range(n):
        x = int(input("enter: "))
        lst_1.append(x)
    lst_2.append(lst_1)
    lst_4.append(lst_1)
print(lst_4)
n = len(lst_2)
for i in range(n):
    for j in range(i+1, n):
        lst_2[i][j], lst_2[j][i] = lst_2[j][i], lst_2[i][j]
print(lst_2)
for lst_1 in lst_2:
    lst_1.reverse()
print(lst_2)
c = len(lst_2)
d = len(lst_2[0])
k = 0
print(lst_4)
for f in range (1):

    for j in range(n - k):
        lst_3.append(lst_4[a][j])
    k = k + 1
    for i in range(n-k):
        i = i+1
        lst_3.append(lst_4[i][d - 1])
    for i in range(n-k):
        lst_3.append(lst_4[d - 1][n-2 - i])
    k = k+1
    for i in range(n-k):
        lst_3.append(lst_4[n - k][i])
#cannot figure this out



print(lst_3)