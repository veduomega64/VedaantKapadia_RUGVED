n = int(input("Enter a number: "))
y = 0
z = 0
for i in range(-n+1,0):
    y = y+1
    for p in range(y):
        print("* ", end="")
    for q in range(-4*(i)-2):
        print(" ", end="")
    for r in range(y):
        print("* ", end="")
    print("",)

for i in range(2*n-1):
    print("* ", end="")
print("")
for i in range(-n+1,0):
    z = z+1
    for p in range(-i):
        print("* ", end="")
    for q in range(4*z-2):
        print(" ", end="")
    for r in range(-i):
        print("* ", end="")
    print("",)
