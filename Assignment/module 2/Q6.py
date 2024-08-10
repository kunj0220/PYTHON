#Write python program that swap two number with temp variable. 

temp=0

num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

print(f"Before swapping num1 is {num1} and num2 is{num2}")

temp=num1
num1=num2
num2=temp

print(f"After swapping num1 is {num1} and num2 is{num2}")

#without temp variable.

num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))

print(f"Before swapping num1 is {num1} and num2 is{num2}")

num1=num1+num2
num2=num1-num2
num1=num1-num2

print(f"After swapping num1 is {num1} and num2 is{num2}")