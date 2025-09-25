str1 = input("Enter a string: ")
x = len(str1)
lst1 = []
str2 = input("Enter a string: ")
p = len (str2)
lst2 = []

def anagram_():
    s = 0
    t = 0
    for i in range (0,x):
        y = str1[i]
        lst1.append(y)
    for i in range (0,p):
        q = str2[i]
        lst2.append(q)
    for a in range (x-1):
        if lst1[a] == " ":
            s = s+1
    for a in range (x-s):
        if lst1[a] == " ":
            lst1.remove(lst1[a])
    for a in range (p-1):
        if lst2[a] == " ":
            t = t+1
    for a in range (p-t):
        if lst2[a] == " ":
            lst2.remove(lst2[a])
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        print("YES it is an anagram")
    else :
        print("NO it is not a anagram")
anagram_()