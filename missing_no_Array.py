#Find the missing number in an array(using summation and xor operation)

#input: [1,2,4,5,6,7]

#logics
# sum of natural numbers
# formula : n*(n+1)//2
# sum of natural numbers=n*(n+1)/2=>Answer

# sum of all the number=>Anwers

# last step:
# sum of natural number answer-sum of all number answerssum of natural number answer-sum of all number answer

ip=[1,2,4,5,6,7,8]
n=ip[-1] #-1 last value in the array
sum1=0
total=n*(n+1)//2
sum1=sum(ip)
answer=total-sum1

print(answer)