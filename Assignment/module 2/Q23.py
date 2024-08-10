# Write a Python function to insert a string in the middle of a string.

s = input("Enter the string:")
s1 = input("Enter middle string:")

middle = len(s) // 2
str1 = s[:middle] + s1 + s[middle:]

print("New string is:", str1)
