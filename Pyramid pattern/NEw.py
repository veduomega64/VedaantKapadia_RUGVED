n = int(input("enter a number "))
for i  in range (1,n+1):

    for j in range(-(n-i-2), 0):
        for k in range(0, -j):
            print(" ", end="")
    for k in range (1,i):
        print(k, end = "")
    for l in range (-i,0):
        print(-l, end = "")
    print("")