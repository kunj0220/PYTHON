# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

string1=input("enter string 1:")
print(string1)

string2=input("enter string 2:")
print(string2)

nstr1 = string2[:2] + string1[2:]
nstr2 = string1[:2] + string2[2:]

new_string = nstr1 + " " + nstr2
print(new_string)

