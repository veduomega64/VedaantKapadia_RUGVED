#using the cipher such as A corresponds to X ..... Z corresponds to W
n = input("Enter a ceaser's cipher code which needs to be encrypted: ")
x = n.lower()
y = int(len(x))
lst = []
p = ""
for i in range (0,y):
    q = x[i]
    lst.append(q)

Cipher = {
    "x" : "a",
    "y" : "b",
    "z" : "c",
    "a" : "d",
    "b" : "e",
    "c" : "f",
    "d" : "g",
    "e" : "h",
    "f" : "i",
    "g" : "j",
    "h" : "k",
    "i" : "l",
    "j" : "m",
    "k" : "n",
    "l" : "o",
    "m" : "p",
    "n" : "q",
    "o" : "r",
    "p" : "s",
    "q" : "t",
    "r" : "u",
    "s" : "v",
    "t" : "w",
    "u" : "x",
    "v" : "y",
    "w" : "z",
    " " : " ",
}
for i in range (0,y):
    z = Cipher[lst[i]]
    p = p+z
print (p)
