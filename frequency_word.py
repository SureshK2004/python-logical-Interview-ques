# Write a python Program to count the frequency of words apperaring in a string
#it will count the values of words in the given sentences

str=input("enter the sentences:")
li=str.split()
d={}
for i in li:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)
