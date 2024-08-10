# Write a Python program to
# count the occurrences of each word in a given sentence


s1=input("Enter a sentance:")

s2=s1.split()
print(s2)
num={}

for i in s2:
    if i in num:
         num[i]+=1
    else:
         num[i]=1

print("The occurrences of each word is ", num)

