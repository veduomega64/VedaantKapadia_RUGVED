n = int(input("Enter a number: "))
lst1 = []
lst2 = []
lst3 = []
lst5 = []
a = 0
b = 0

for i in range(0,len(str(n))):
    z = n%10
    n = n//10
    lst1.append(z)
while lst1[a]<=lst1[a+1]:
    lst2.append(lst1[a])
    a = a+1
i = a
while a<=i<=len(lst1)-1:
    lst3.append(lst1[i])
    lst5.append(lst1[i])
    i = i+1
lst4 = lst2
lst2.sort()
lst3.sort(reverse=True)
if lst4==lst2 and lst5==lst3 and lst1[0] == lst1[len(lst1)-1]:
    print("YES it is a hill number")
else:
    print("NO it is not a hill number")