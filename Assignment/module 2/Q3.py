# Write a Python program to get the Fibonacci series of given range.


x=0 
y=1
z=0

num=int(input("enter number :"))
for i in range (0,num):
    x=y
    y=z
    z=x+y
    print(z,end=" ")
   
