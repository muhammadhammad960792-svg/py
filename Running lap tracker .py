# ============================================================
#                RUNNING LAP TRACKER PROGRAM
# ============================================================

# ------------------------------------------------------------
# Step 1: Understand the Problem
# ------------------------------------------------------------
# Create a Running Lap Tracker that:
# 1. Asks the user for the number of laps.
# 2. Records the time for each lap.
# 3. Calculates the total running time.
# 4. Calculates the average lap time.
# 5. Displays all lap times.
# 6. Uses both a loop and a nested loop.
# 7. Demonstrates algorithm complexity.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 2: Set the Number of Laps
# ------------------------------------------------------------
num_laps = int(input("Enter the number of laps: "))

# Create variables
lap_times = []
total_time = 0

# ------------------------------------------------------------
# Step 3: Formula Method
# ------------------------------------------------------------
# Formula:
# Total Time = Sum of all lap times
# Average Time = Total Time / Number of Laps

# ------------------------------------------------------------
# Step 4: Loop Method
# ------------------------------------------------------------
# Use a for loop to input each lap time and calculate total.

for lap in range(1, num_laps + 1):
    time = float(input(f"Enter time for Lap {lap} (seconds): "))
    lap_times.append(time)
    total_time += time

# Calculate average time
average_time = total_time / num_laps

# ------------------------------------------------------------
# Display Results
# ------------------------------------------------------------
print("\n========== RUNNING LAP REPORT ==========")

for lap in range(num_laps):
    print(f"Lap {lap + 1}: {lap_times[lap]:.2f} seconds")

print("----------------------------------------")
print(f"Total Time   : {total_time:.2f} seconds")
print(f"Average Time : {average_time:.2f} seconds")

# ------------------------------------------------------------
# Step 5: Nested Loop Method
# ------------------------------------------------------------
# Print a progress pattern using a nested loop.

print("\nLap Progress")

for lap in range(1, num_laps + 1):
    print(f"Lap {lap}: ", end="")
    for star in range(lap):
        print("*", end="")
    print()

# ------------------------------------------------------------
# Step 6: Pseudocode Comments
# ------------------------------------------------------------
#
# START
#     Input number of laps
#     Set total_time = 0
#     Create an empty list called lap_times
#
#     FOR each lap
#         Input lap time
#         Store lap time in list
#         Add lap time to total_time
#     END FOR
#
#     Compute average_time
#
#     Display lap times
#     Display total time
#     Display average time
#
#     FOR each lap
#         FOR number of completed laps
#             Print "*"
#         END FOR
#     END FOR
#
# END
#

# ------------------------------------------------------------
# Step 7: Time and Space Complexity
# ------------------------------------------------------------
print("\n========== COMPLEXITY ANALYSIS ==========")
print("Input Loop Time Complexity   : O(n)")
print("Display Loop Time Complexity : O(n)")
print("Nested Loop Time Complexity  : O(n^2)")
print("Overall Time Complexity      : O(n^2)")
print("Space Complexity             : O(n)")
print("Reason: The program stores lap times in a list.")

# ------------------------------------------------------------
# Step 8: Run and Test
# ------------------------------------------------------------
print("\n========== PROGRAM TEST COMPLETE ==========")
print("The Running Lap Tracker executed successfully.")
print("You can test it again with different numbers of laps and lap times.")

# ============================================================
# End of Program
# ============================================================