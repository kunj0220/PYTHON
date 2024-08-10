#Write a Python program to test whether a passed letter is a vowel or not.

letter=input("Enter a Letter :").lower()

if letter == 'a' and 'e' and 'i' and 'o' and 'u':
    print("A passed letter is vowel")
else:
    print("A passed letter is not vowel")