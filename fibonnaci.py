#Write the python code for fibonnaci series:

n=int(input("enter:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


#methods 2
def fibbo():
    i = 0
    j = 1
    while True:
        c = i
        i, j = j, i + j
        yield c

f = fibbo()
for _ in range(10):
    print(next(f), end=" ")

