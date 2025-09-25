x = input("Enter either true or false: ")
y = input("Enter either true or false : ")
z = input("Enter either true or false : ")
x = x.lower()
y = y.lower()
z = z.lower()
def triple_and():
    if x == "true" and y == "true" and z == "true":
        print("True")
    else:
        print("false")
triple_and()