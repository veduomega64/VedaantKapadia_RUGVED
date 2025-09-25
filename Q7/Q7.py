n = int(input("Enter the number till u want the fibonacci series: "))
x = 0
y = 1
a = int(n/2)
for i in range(0,a):
    print(x)
    print(y)
    x = x + y
    y = x + y


