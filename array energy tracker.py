
# ==========================================
# PROJECT: ARRAY ENERGY TRACKER
# ALGORITHM: KADANE'S ALGORITHM
# LANGUAGE: PYTHON
# ==========================================

# STEP 1: Print the program title

print("===================================")
print("       ARRAY ENERGY TRACKER")
print("       Using Kadane's Algorithm")
print("===================================\n")


# STEP 2: Create the energy array

energy = [4, -3, 5, -2, 6, -8, 7, 2]

print("Energy Array:", energy)
print("\nStarting Energy Analysis...\n")


# STEP 3: Explore subarrays

print("STEP 3: Exploring Subarrays")

for i in range(len(energy)):
    for j in range(i, len(energy)):
        subarray = energy[i:j+1]
        print("Subarray:", subarray,
              "Sum:", sum(subarray))


# STEP 4: Show the drag of negatives

print("\nSTEP 4: Showing the Drag of Negatives")

current_sum = 0

for value in energy:
    current_sum += value
    print("Energy:", value,
          "| Running Sum:", current_sum)


# STEP 5: Reset the running sum

print("\nSTEP 5: Resetting the Running Sum")

current_sum = 0
print("Running Sum Reset To:", current_sum)


# STEP 6: Track the maximum sum so far

print("\nSTEP 6: Tracking Maximum Sum")

max_sum = energy[0]
current_sum = energy[0]

for value in energy[1:]:
    current_sum = max(value, current_sum + value)
    max_sum = max(max_sum, current_sum)

    print("Current Sum:", current_sum,
          "| Maximum So Far:", max_sum)


# STEP 7: Build Kadane's Algorithm

print("\nSTEP 7: Kadane's Algorithm")

def kadane_algorithm(arr):

    current_sum = arr[0]
    max_sum = arr[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, arr[start:end+1]


# Calculate the result

maximum_energy, best_subarray = kadane_algorithm(energy)


# FINAL OUTPUT

print("\n===================================")
print("          FINAL RESULTS")
print("===================================")

print("Original Energy Array:", energy)

print("Maximum Energy Sum:", maximum_energy)

print("Best Continuous Subarray:", best_subarray)

print("===================================")
print("       PROGRAM COMPLETED!")
print("===================================")
