#write the python code to remove duplicate


a=[1,2,3,2,3,4,7,8,9,6]

#method -1 using set
print(set(a))

#method-2 remove duplicate using array

b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


#methods-3 using lambda functions
rem_duplicate=lambda a:list(set(a))
print(rem_duplicate(a))

#methods -4 remove duplicates from dictionary
d={
    'car':["ford",'benz','audi','BMW','ford'],
    'brand':["mustang","ranz","mustang","ranz"]

}
d1={}
for key,value in d.items():
    d1[key]=set(value)
print(d1) 

#method - 5 using symmetric difference - remove the duplicate elements

s={1,2,4,5}
s1={2,1,5,7}
removefunc=s.symmetric_difference(s1)
print(removefunc)



