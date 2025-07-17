#merge one dictionary to other dictionary

# 1.update()
# 2.**

a={1:"python",2:"java"}
b={3:".net",4:"sql"}
a.update(b)
# print(a)

c={**a,**b}
print(c)

