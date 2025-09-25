n = []
q = []
a = int(input("enter no of elements: "))
for i in range(a):
    b = int(input("enter a number: "))
    n.append(b)

for i in range (0,len(n)):
    for i in range(0,len(n)):
        if min(n) == n[i]:
            x = i
            break
    q.append(n[x])
    n.remove(n[x])
print(q, end="")
print(" is the sorted list")
