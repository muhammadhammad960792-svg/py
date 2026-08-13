from math import sqrt
number = int(input("Enter your number"))
print("\n")
if number < 0:
    for i in range(2, int(sqrt(number)) +1):
      if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number")






def SieveOfErathosothenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
                p += 1


    for p in range(2, num+1):
            if prime[p]:
                print(p)


num = int(input("Enter a number"))
print("Following are the prime numbers smaller")
print("than or equal to", num)
SieveOfErathosothenes(num)

