
# ==========================================
# PROJECT TITLE: TARGET TRACKER LAB
# ==========================================

print("===================================")
print("       TARGET TRACKER LAB")
print("===================================")

# STEP 1: CREATE THE MAIN ARRAY

arr = [2, 4, 6, 3, 7, 1, 5, 2]

print("\nStep 1: Main Array")
print("Array:", arr)


# STEP 2: USE SLICES AND CALCULATE SUMS

print("\nStep 2: Slices and Sums")

left_slice = arr[:4]
right_slice = arr[4:]

left_sum = sum(left_slice)
right_sum = sum(right_slice)

print("Left Slice:", left_slice)
print("Right Slice:", right_slice)
print("Left Sum:", left_sum)
print("Right Sum:", right_sum)


# STEP 3: CHECK LEFT RIGHT BALANCE

print("\nStep 3: Check Left-Right Balance")

if left_sum == right_sum:
    print("Array is balanced!")
else:
    print("Array is not balanced.")


# STEP 4: FIND THE EQUILIBRIUM POINT

print("\nStep 4: Find Equilibrium Point")

total_sum = sum(arr)
left_sum = 0
equilibrium_found = False

for i in range(len(arr)):

    right_sum = total_sum - left_sum - arr[i]

    if left_sum == right_sum:
        print("Equilibrium Index:", i)
        print("Equilibrium Value:", arr[i])
        equilibrium_found = True

    left_sum += arr[i]

if not equilibrium_found:
    print("No equilibrium point found.")


# STEP 5: BUILD A SUBARRAY WINDOW

print("\nStep 5: Build a Subarray Window")

window_size = 3

for i in range(len(arr) - window_size + 1):

    window = arr[i:i + window_size]

    print("Window:", window, "Sum:", sum(window))


# STEP 6: SEARCH FOR THE TARGET SUM

print("\nStep 6: Search for Target Sum")

target = int(input("Enter the target sum: "))

found = False

for i in range(len(arr)):

    current_sum = 0

    for j in range(i, len(arr)):

        current_sum += arr[j]

        if current_sum == target:

            print("Target Sum Found!")
            print("Subarray:", arr[i:j + 1])
            print("Starting Index:", i)
            print("Ending Index:", j)

            found = True

if not found:
    print("Target sum not found in any subarray.")


# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\n===================================")
print("     TARGET TRACKER LAB FINISHED")
print("===================================")
