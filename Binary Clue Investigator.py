# ==========================================
#        BINARY CLUE INVESTIGATOR
# ==========================================

# ------------------------------------------
# STEP 1: Print the Program Title
# ------------------------------------------

print("====================================")
print("      BINARY CLUE INVESTIGATOR")
print("====================================")


# ------------------------------------------
# STEP 2: Test XOR Identity and Equality
# ------------------------------------------

print("\nSTEP 2: XOR Identity and Equality")

a = 10

print("a =", a)
print("a ^ 0 =", a ^ 0)      # XOR identity
print("a ^ a =", a ^ a)      # XOR equality


# ------------------------------------------
# STEP 3: Apply XOR Cancellation
# ------------------------------------------

print("\nSTEP 3: XOR Cancellation")

x = 5
y = 8

result = x ^ y ^ x

print("x =", x)
print("y =", y)
print("x ^ y ^ x =", result)

print("Because x ^ x = 0")
print("So x ^ y ^ x = y")


# ------------------------------------------
# STEP 4: Find One Odd Occurring Number
# ------------------------------------------

print("\nSTEP 4: Find One Odd Occurring Number")

arr1 = [2, 3, 5, 4, 5, 3, 4]

xor_result = 0

for num in arr1:
    xor_result = xor_result ^ num

print("Array:", arr1)
print("Odd occurring number:", xor_result)


# ------------------------------------------
# STEP 5: Find XOR of Two Odd Occurring Numbers
# ------------------------------------------

print("\nSTEP 5: Find XOR of Two Odd Occurring Numbers")

arr2 = [1, 2, 3, 2, 3, 1, 4, 5]

xor_all = 0

for num in arr2:
    xor_all = xor_all ^ num

print("Array:", arr2)
print("XOR of two odd occurring numbers:", xor_all)


# ------------------------------------------
# STEP 6: Split Using the Rightmost Set Bit
# ------------------------------------------

print("\nSTEP 6: Split Using the Rightmost Set Bit")

rightmost_set_bit = xor_all & -xor_all

print("XOR result:", xor_all)
print("Rightmost set bit:", rightmost_set_bit)

group1 = []
group2 = []

for num in arr2:

    if num & rightmost_set_bit:
        group1.append(num)
    else:
        group2.append(num)

print("Group 1:", group1)
print("Group 2:", group2)


# ------------------------------------------
# STEP 7: Identify Both Odd Occurring Numbers
# ------------------------------------------

print("\nSTEP 7: IDENTIFY BOTH ODD OCCURRING NUMBERS")

odd1 = 0
odd2 = 0

for num in arr2:

    if num & rightmost_set_bit:
        odd1 = odd1 ^ num

    else:
        odd2 = odd2 ^ num


print("First odd occurring number:", odd1)
print("Second odd occurring number:", odd2)


# ------------------------------------------
# FINAL RESULT
# ------------------------------------------

print("\n====================================")
print("           FINAL RESULT")
print("====================================")

print("The two odd occurring numbers are:")
print(odd1, "and", odd2)

print("\nBinary Clue Investigator Completed!")