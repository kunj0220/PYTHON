# Write a Python program to get the Factorial number of given number.

f=1

num=int(input("enter number :"))

for i in range(num,0,-1):
   f=f*i

print("factorial of",num,"is",f)
