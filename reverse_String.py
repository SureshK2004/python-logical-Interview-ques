#Write a python to print reverse the number

# methods-1
a=[1,2,3,4]
a.reverse()
print(a)

#methods-2 using slicing methods
b=[5,4,2,3,1]
lst=b[::-1]
print(lst)

#method- 3 using reversed

c=[1,3,4,5,6,6]
list2=list(reversed(c))
print(list2)

#Without using any build in function used to reverse the list

d=[11,22,3,4,5,6]
e=[]
for i in range(len(d)-1,-1,-1):#-1(start,stop,step)
    e.append(d[i])
print(e)