def fib(n):
    if n <=1:
        return n
    return fib(n -1) + fib(n - 2)
input("Tree recursion - two recursive calls per step.Press Enter")
print(" fib(5) =", fib(5))
print(" fib(6) =", fib(6))
n = int(input("Enter n (try 4 or 7): "))
