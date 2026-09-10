def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)
input("Factorial - n! = n x (n-1) x ... x 1 base case: 0! = 1. Press Enter ")
print(" 4! =", factorial(4), " = 4 x 3 x 2 x 1")
print(" 5! =", factorial(5), " = 5 x 4 x 3 x 2 x 1")
