# Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero.

n1=int(input("enter 1st number :"))
n2=int(input("enter 2nd number :"))
n3=int(input("enter 3rd number :"))

if n1 == n2 or n2 == n3 or n3 == n1:
    print("sum is ",0)
else:
    sum=n1+n2+n3
    print("sum of 3 numbers is ",sum)
