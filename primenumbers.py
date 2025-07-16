#Write a python program to print the prime numbers in the given number:

n=int(input("enter:"))
for i in range(2,n):
    is_prime=True
    for j in range(2,i):
        if i % j == 0:
            is_prime=False
            break
    if is_prime:
        print(i)

#Write a python program to print the given number is prime or not:

if n <=1:
    print("ithu prime number kedaiyathu")
else:
    is_prime=True
    for a in range(2,n):
        if n % a ==0:
            is_prime=False
            break
if is_prime:
    print(f"Ithu prime number:{n}")
else:
    print(f"Ithu prime number kedaiyathu: {n}")

