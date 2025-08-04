#Write a python code to print the second max and min values 

lest=[12,12,34,32,65,45,67]
def second(lest):
    unique=list(set(lest))
    if len(unique)<2:
        return None
    unique.sort()
    return unique[-2]
g=second(lest)
print(g)


def mini_second(lest):
    unique=list(set(lest))
    if len(unique)<2:
        return None
    unique.sort()
    return unique[1]
d=mini_second(lest)
print(d)

