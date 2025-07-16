#find the largest and smallest elemnt in tha given array

a=[12,23,34,6,45,88,90]

#smallest element
min=a[0]
size=len(a)
for i in range(size):
    if a[i] < min:
        min=a[i]
print(min)

#largest number
max=a[0]
size=len(a)
for i in range(size):
    if a[i]>max:
        max=a[i]
print(max)



