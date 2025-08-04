n=153
lenght=len(str(n))
temp=n
sum=0
while temp > 0:
    digit=temp % 10
    sum +=digit ** lenght
    temp=temp // 10
if sum == n:
    print("its a amstrong number")
else:
    print("its not an amstrong number")