

# ==========================================
# BINARY POWER SET BUILDER
# ==========================================

# Step 1 & 2: Store items and count them
items = input("Enter items separated by spaces: ").split()
n = len(items)

print("\nItems:", items)
print("Number of items:", n)

# Total number of subsets = 2^n
total_subsets = 2 ** n

print("Total subsets:", total_subsets)


# Step 3, 4 & 5: Binary masks + bitwise operation + two loops
print("\n--- Binary Mask Table and Subsets ---")

for mask in range(total_subsets):

    subset = []

    # Show binary mask
    binary = format(mask, f"0{n}b")

    # Check every bit
    for i in range(n):

        # Bitwise operation
        if mask & (1 << i):
            subset.append(items[i])

    print(binary, "->", subset)


# Step 6: Calculate bit difference between two binary numbers
print("\n--- Bit Difference Calculator ---")

num1 = int(input("Enter first binary number: "), 2)
num2 = int(input("Enter second binary number: "), 2)

difference = num1 ^ num2

print("XOR result:", bin(difference))
print("Number of different bits:", difference.bit_count())