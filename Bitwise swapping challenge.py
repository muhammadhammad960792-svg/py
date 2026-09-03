# Bitwise Swap Challenge

# Get two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nOriginal values:")
print("a =", a)
print("b =", b)

# 1. Swap without a third variable
a, b = b, a

print("\nAfter normal swap without third variable:")
print("a =", a)
print("b =", b)

# 2. XOR Swap
a = a ^ b
b = a ^ b
a = a ^ b

print("\nAfter XOR swap:")
print("a =", a)
print("b =", b)

# 3. Left shift to double the numbers
double_a = a << 1
double_b = b << 1

print("\nAfter left shift (doubling):")
print("a × 2 =", double_a)
print("b × 2 =", double_b)

# 4. Detect different signs using XOR
if (a ^ b) < 0:
    print("\nThe numbers have different signs.")
else:
    print("\nThe numbers have the same sign.")

# 5. Divide without using /
# Integer division using repeated subtraction
def divide_without_slash(x, y):
    if y == 0:
        return "Cannot divide by zero."

    negative = (x < 0) ^ (y < 0)

    x = abs(x)
    y = abs(y)

    quotient = 0

    while x >= y:
        x -= y
        quotient += 1

    if negative:
        quotient = -quotient

    return quotient


division = divide_without_slash(a, b)

print("\nDivision without /:")
print(a, "÷", b, "=", division)

print("\n✅ Bitwise Swap Challenge completed!")
