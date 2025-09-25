array_ = ["mango", "strawberry", "mango", "litchi", "apple", "mango", "banana" ]
array_2 = ["mango", "strawberry", "mango", "litchi", "apple", "mango", "banana" ]
n= len(array_)
array_2.sort()
for i in range(n):
    if array_2[i] == array_2[i+1]:
        print(array_.index(array_2[i]))
        break



