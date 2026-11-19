def max_mid(n):
    arr = [-1, n, -1]
    current = best = arr[0]

    for x in arr[1:]:
        if current < 0:
            current = x
        else:
            current = current + x

        if current > best:
            best = current

    return best


input("max_mid(n) finds the max subarray sum in [-1, n, -1]. Press Enter ")

print("  max_mid(3) =", max_mid(3))
print("  max_mid(4) =", max_mid(4))

n = int(input("Enter n (try 5 or 6): "))
guess = input("What is max_mid(" + str(n) + ")? ")