def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n-1) + fibonacci(n-2)
a = int(input("Enter the number till you want the fibonacci sequence to go to: "))
if a <= 0:
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(a):
       print(fibonacci(i))
