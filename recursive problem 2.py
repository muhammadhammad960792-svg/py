def ways (stairs):
    if stairs  < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)
input ("Ways counts every distinct path up n stairs - 1 step or 2 steps at a time. Prees Enter")
print("Ways (3) =", ways(3))
print("Ways (4) =", ways(4))
n=int(input("Enter number of steps (try 5 or 6): "))
guess = input("What is ways (" + str(n) + ") ? ")
print("Ways (" + str(n) + ") =", ways(n)," your guess:", guess)