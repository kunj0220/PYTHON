# Write a Python program to check if a number is positive, negative or zero.

num = int(input("enter number :"))

if num > 0:
    print("positive number")

elif num < 0:
    print("negative number")

elif num == 0:
    print("zero")

else:
    print("invalid input")