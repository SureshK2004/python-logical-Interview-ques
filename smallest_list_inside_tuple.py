#find the smallest values inside the tuple
n=[("a",10),("b",5),("c",12),("d",2)]
max_value=n[0]
for itm in n:
    if itm[1]>max_value[1]:
        max_value=itm
print(max_value)

