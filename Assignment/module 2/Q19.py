"""
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string,
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
"""


string = input("Enter a string:")  


not1 = string.find("not")
poor = string.find("poor")

if not1 != -1 and poor != -1 and poor > not1:
     s1 = string[:not1] + "good" + string[poor + 4:]
else:
    s1 = string

print(s1)


