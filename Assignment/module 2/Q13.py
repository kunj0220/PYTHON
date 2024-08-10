# Write a Python program to count the number of characters
# (character frequency) in a string.

s=input("Enter a string:")
num={}

for i in s:
    if i in num:
         num[i]+=1
    else:
         num[i]=1

print("The number of character in a string is ", num)



