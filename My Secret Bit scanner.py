# ==========================================
#       MY SECRET CODE BIT SCANNER
# ==========================================

# STEP 1: Set the Secret Code and Access Key
secret_code = 45
access_key = 27

print("==================================")
print("     MY SECRET CODE BIT SCANNER")
print("==================================")


# STEP 2: Create the Binary Helper Function
def show_binary(number):
    return bin(number)[2:]


# STEP 3: Display Bits and Binary
print("\n--- STEP 3: BINARY DISPLAY ---")
print("Secret Code:", secret_code)
print("Secret Code in Binary:", show_binary(secret_code))

print("Access Key:", access_key)
print("Access Key in Binary:", show_binary(access_key))


# STEP 4: Use AND and OR
print("\n--- STEP 4: AND and OR ---")

and_result = secret_code & access_key
or_result = secret_code | access_key

print("AND Result:", and_result)
print("AND Binary:", show_binary(and_result))

print("OR Result:", or_result)
print("OR Binary:", show_binary(or_result))


# STEP 5: Use NOT and XOR
print("\n--- STEP 5: NOT and XOR ---")

not_result = ~secret_code
xor_result = secret_code ^ access_key

print("NOT Secret Code:", not_result)
print("XOR Result:", xor_result)
print("XOR Binary:", show_binary(xor_result))


# STEP 6: Apply Left Shift and Right Shift
print("\n--- STEP 6: LEFT and RIGHT SHIFT ---")

left_shift = secret_code << 1
right_shift = secret_code >> 1

print("Left Shift:", left_shift)
print("Left Shift Binary:", show_binary(left_shift))

print("Right Shift:", right_shift)
print("Right Shift Binary:", show_binary(right_shift))


# STEP 7: Check Odd or Even with Bitwise Operation
print("\n--- STEP 7: ODD or EVEN CHECK ---")

if secret_code & 1:
    print(secret_code, "is ODD")
else:
    print(secret_code, "is EVEN")


# STEP 8: Count the Bits
print("\n--- STEP 8: COUNT ACTIVE BITS ---")

binary_code = show_binary(secret_code)
bit_count = binary_code.count("1")

print("Binary:", binary_code)
print("Number of 1 bits:", bit_count)


# STEP 9: Run and Test
print("\n==================================")
print("          SCAN COMPLETE")
print("==================================")