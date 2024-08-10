# Write a Python program to count occurrences of a substring in a string.

string=input("enter string:")
print(string)

substring=input("Enter substring:")
print(substring)


counts = string.count(substring)


print(f"The substring '{substring}' occurs {counts} times in the main string.")



