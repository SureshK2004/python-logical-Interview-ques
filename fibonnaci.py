#Write the python code for fibonnaci series:

n=int(input("enter:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
