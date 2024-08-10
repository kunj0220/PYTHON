"""
Write a Python function that takes a list of words 
and returns the length of the longest one
"""

words = ["phone" , "watch" , "car" , "perfume" , "bike"]

length = 0


for word in words:
   
    if len(word) > length:
        length = len(word)


print("The length of the longest word is:", length)



