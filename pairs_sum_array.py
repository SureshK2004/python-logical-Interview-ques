#find out paris with given sum value of an array
#i/p...arr=[5,4,7,3,19,21] sum=17 

#logics
# 1.set assign unique value irukka
# 2.emptylist variable assign pannanum
# 3.arr va loop kulla kondu varanum
# 4.athukull a onemore assign panni athula (target number- arr(loop var))
# 5.assign panna variable ah conditon la set kulla send pannanum
# 6.emptylist var kulla conditon(var),loop(var) kulla append pannanum
# 7.set var kulla loop(var) add pannanum


arr = [11,4,13,15,2,7,9,8,3]
target = 17
unique=set()
var1=[]
for i in arr:
    num=target-i
    if num in unique:
        var1.append((num,i))
    unique.add(i)
    
print(var1)
