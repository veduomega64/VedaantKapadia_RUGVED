n = int(input("enter a number: "))
y=0
i = n
v=0
for i in range (-n,0):
    y = y+1
    for p in range(0, -i):
        print(" ", end="")


    for z in range(0, y):
        print("* ", end="")
    print("")
for i in range (-n,0):
    v = v+1
    for p in range(0, v):
        print(" ", end="")


    for z in range(0, -i):
        print("* ", end="")
    print("")

