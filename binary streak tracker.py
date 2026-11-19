
# Project Title: Binary Streak Tracker

# Step 1: Create a Binary Array
binary_array = [1, 1, 0, 1, 1, 1, 0, 1, 1]

# Step 2: Build a Streak Counter with Reset
current_streak = 0
best_streak = 0

# Step 3: Track the Best Streak
# Step 4: Use Same Direction Two Pointers
read_pointer = 0

# Step 5: Apply the Write Pointer Pattern
write_pointer = 0

while read_pointer < len(binary_array):

    if binary_array[read_pointer] == 1:
        current_streak += 1

        if current_streak > best_streak:
            best_streak = current_streak

        binary_array[write_pointer] = binary_array[read_pointer]
        write_pointer += 1

    else:
        current_streak = 0

    read_pointer += 1

# Display Results
print("Binary Array:", binary_array)
print("Total Ones:", write_pointer)
print("Best Streak:", best_streak)
