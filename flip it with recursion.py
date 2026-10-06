# ==========================================
#              FLUID IT PROJECT
#        Recursion in Python
# ==========================================

print("===================================")
print("          FLUID IT PROJECT")
print("===================================")


# STEP 1: Extract digits and words
def extract_digits(number):
    if number == 0:                 # Stopping condition
        return

    digit = number % 10
    print("Digit:", digit)

    extract_digits(number // 10)    # Recursion


# STEP 2: Constant digits using recursion
def count_digits(number):
    if number == 0:                 # Stopping condition
        return 0

    return 1 + count_digits(number // 10)


# STEP 3: Reverse a number using recursion
def reverse_number(number, reverse=0):
    if number == 0:                 # Stopping condition
        return reverse

    digit = number % 10
    reverse = reverse * 10 + digit

    return reverse_number(number // 10, reverse)


# STEP 4: Reverse a string using recursion
def reverse_string(text):
    if text == "":                  # Stopping condition
        return ""

    return reverse_string(text[1:]) + text[0]


# STEP 5: Calculate power using recursion
def power(base, exponent):
    if exponent == 0:               # Stopping condition
        return 1

    return base * power(base, exponent - 1)


# STEP 6: Two stopping conditions
def countdown(number):
    # Stopping condition 1
    if number == 0:
        print("Finished!")
        return

    # Stopping condition 2
    if number < 0:
        print("Number cannot be negative.")
        return

    print(number)
    countdown(number - 1)


# ==========================================
#              MAIN PROGRAM
# ==========================================

number = 12345

print("\nSTEP 1: Extract Digits")
extract_digits(number)

print("\nSTEP 2: Count Digits")
total = count_digits(number)
print("Total digits:", total)

print("\nSTEP 3: Reverse Number")
print("Original number:", number)
print("Reversed number:", reverse_number(number))

print("\nSTEP 4: Reverse String")
word = "FLUID"
print("Original string:", word)
print("Reversed string:", reverse_string(word))

print("\nSTEP 5: Power Using Recursion")
base = 2
exponent = 5
print(base, "^", exponent, "=", power(base, exponent))

print("\nSTEP 6: Two Stopping Conditions")
countdown(5)

print("\n===================================")
print("       FLUID IT PROJECT COMPLETE")
print("===================================")