# Write a python program to sum of the first n positive integers.

num=int(input("enter a number :"))
sum=0
for i in range(num+1):
    sum+=i

print("sum is",sum)