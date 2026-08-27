# ==========================================
#       SMART WATCH - SMART SWITCH MONITOR
#       Bit Manipulation Python Project
# ==========================================


# ------------------------------------------
# STEP 1: CREATE THE SWITCH VALUE
# ------------------------------------------

# Each bit represents one smart switch
# 1 = ON
# 0 = OFF

switch_value = 0b10110110

print("==========================================")
print("       SMART WATCH SWITCH MONITOR")
print("==========================================")

print("\nSTEP 1: Switch Value")
print("Decimal Value:", switch_value)
print("Binary Value :", bin(switch_value))


# ------------------------------------------
# STEP 2: CREATE THE BINARY HELPER FUNCTION
# ------------------------------------------

def binary_helper(number, bits=8):
    return format(number, f"0{bits}b")


print("\nSTEP 2: Binary Helper Function")
print("8-bit Binary:", binary_helper(switch_value))


# ------------------------------------------
# STEP 3: COUNT SET BITS AND ZERO BITS
# ------------------------------------------

set_bits = binary_helper(switch_value).count("1")
zero_bits = binary_helper(switch_value).count("0")

print("\nSTEP 3: Count Set Bits and Zero Bits")
print("Set Bits (ON switches) :", set_bits)
print("Zero Bits (OFF switches):", zero_bits)


# ------------------------------------------
# STEP 4: COUNT SET BITS USING BITWISE LOGIC
# ------------------------------------------

def count_set_bits_bitwise(number):
    count = 0

    while number > 0:
        count += number & 1
        number >>= 1

    return count


bitwise_set_bits = count_set_bits_bitwise(switch_value)

print("\nSTEP 4: Count Set Bits Using Bitwise Logic")
print("Total Set Bits:", bitwise_set_bits)


# ------------------------------------------
# STEP 5: FIND THE FIRST SET BIT
# ------------------------------------------

def find_first_set_bit(number):
    if number == 0:
        return -1

    position = 1

    while (number & 1) == 0:
        number >>= 1
        position += 1

    return position


first_set_bit = find_first_set_bit(switch_value)

print("\nSTEP 5: Find the First Set Bit")
print("First Set Bit Position:", first_set_bit)


# ------------------------------------------
# STEP 6: BUILD BIT MASKS
# ------------------------------------------

print("\nSTEP 6: Build Bit Masks")

bit_masks = []

for i in range(8):
    mask = 1 << i
    bit_masks.append(mask)

    print(
        "Switch", i + 1,
        "| Mask:", binary_helper(mask)
    )


# ------------------------------------------
# STEP 7: CHECK EACH SMART SWITCH
# ------------------------------------------

print("\nSTEP 7: Check Each Smart Switch")

on_switches = []
off_switches = []

for i in range(8):

    mask = 1 << i

    # Check the bit using AND (&)
    if switch_value & mask:
        print("Switch", i + 1, "is ON")
        on_switches.append(i + 1)

    else:
        print("Switch", i + 1, "is OFF")
        off_switches.append(i + 1)


# ------------------------------------------
# STEP 8: PRINT THE FINAL SUMMARY
# ------------------------------------------

print("\n==========================================")
print("           FINAL SMART WATCH SUMMARY")
print("==========================================")

print("Switch Decimal Value :", switch_value)
print("Switch Binary Value  :", binary_helper(switch_value))

print("\nTotal ON Switches    :", set_bits)
print("Total OFF Switches   :", zero_bits)

print("\nON Switch Numbers    :", on_switches)
print("OFF Switch Numbers   :", off_switches)

print("\nFirst Set Bit Position:", first_set_bit)

print("\nIndividual Switch Status:")

for i in range(8):
    mask = 1 << i

    if switch_value & mask:
        print("Switch", i + 1, ": ON")

    else:
        print("Switch", i + 1, ": OFF")


print("\n==========================================")
print("     SMART WATCH MONITOR FINISHED!")
print("==========================================")