n = input("Enter your essay: ")
lst_1 = []
lst_2 = []
lst_3 = []
a = 0
b = 0
c = 0
for i in range(len(n)):
    if n[i]==" ":
        lst_1.append(n[a:i])
        a = i
number_of_words = len(lst_1)+1
for i in range(len(n)):
    if n[i]==".":
        lst_2.append(n[b:i])
        b = i
number_of_sentences = len(lst_2)+1
for i in range(len(n)):
    lst_3.append(n[i])
for i in range(len(lst_3)):
    if lst_3[i]==" ":
        c = c+1
for i in range (c):
    lst_3.remove(" ")
number_of_letters = len(lst_3)
CLI = 5.88*(number_of_letters/number_of_words) + 29.6*(number_of_sentences/number_of_words) - 15.8
if 1 > CLI > 0.0:
    print("kindergarden")
if 2 > CLI > 1:
    print("1st grade")
if 3 > CLI > 2:
    print("2nd grade")
if 4 > CLI > 3:
    print("3rd grade")
if 5 > CLI > 4:
    print("4th grade")
if 6 > CLI > 5:
    print("5th grade")
if 7 > CLI > 6:
    print("6th grade")
if 8 > CLI > 7:
    print("7th grade")
if 9 > CLI > 8:
    print("8th grade")
if 10 > CLI > 9:
    print("9th grade")
if 11 > CLI > 10:
    print("10th grade")
if 12 > CLI > 11:
    print("11th grade")
if 13 > CLI > 12:
    print("12th grade")
if 14 > CLI > 13:
    print("College freshman")
if CLI > 14:
    print("College 2nd year+")