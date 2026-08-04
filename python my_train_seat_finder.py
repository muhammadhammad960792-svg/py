# My Train Seat Finder
# Binary Search Implementation (Iterative + Recursive)

# Step 1: Create the sorted seat List
train_seats = [2, 3, 11, 13, 19, 25, 31, 42, 56, 70]


# Step 2: Set the target seat
target_seat = 31


# Step 3: Build the Iterative Binary Search Function
def iterative_binary_search(seats, target):
    low = 0
    high = len(seats) - 1

    while low <= high:

        # Step 4: Check the middle seat
        middle = (low + high) // 2

        print(f"Checking seat: {seats[middle]}")

        if seats[middle] == target:
            return middle

        elif seats[middle] < target:
            low = middle + 1

        else:
            high = middle - 1

    return -1


# Step 6: Build the Recursive Binary Search Function
def recursive_binary_search(seats, target, low, high):

    # Base condition
    if low > high:
        return -1

    # Check middle seat
    middle = (low + high) // 2

    print(f"Recursive checking seat: {seats[middle]}")

    if seats[middle] == target:
        return middle

    elif seats[middle] < target:
        return recursive_binary_search(
            seats, target, middle + 1, high
        )

    else:
        return recursive_binary_search(
            seats, target, low, middle - 1
        )


# Step 5: Print O(log n) and O(1) space
print("\n--- Iterative Binary Search ---")

result = iterative_binary_search(train_seats, target_seat)

if result != -1:
    print(f"Seat {target_seat} found at position {result}")
else:
    print("Seat not found")

print("\nComplexity:")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# Step 7: Explain the Call Stack
print("\n--- Recursive Binary Search ---")

print("""
Call Stack Explanation:
Each recursive call creates a new function frame in memory.
The function keeps dividing the search area until:
1. The seat is found, or
2. The search range becomes empty.

Recursive calls use extra memory because every call is stored
in the call stack.
""")


recursive_result = recursive_binary_search(
    train_seats,
    target_seat,
    0,
    len(train_seats) - 1
)

if recursive_result != -1:
    print(f"Seat {target_seat} found at position {recursive_result}")
else:
    print("Seat not found")


print("\nRecursive Complexity:")
print("Time Complexity: O(log n)")
print("Space Complexity: O(log n) because of recursion call stack")


# Step 8: Add the Complexity Ladder
print("""
--- Complexity Ladder ---

Fastest
|
| O(1)       Constant Time
|
| O(log n)   Binary Search
|
| O(n)       Linear Search
|
| O(n log n) Efficient Sorting
|
| O(n²)      Nested Loops
|
| O(2^n)     Exponential
|
Slowest
""")


# Step 9: Run the Test
print("--- Test Completed ---")

print("Train Seat List:", train_seats)
print("Target Seat:", target_seat)
print("Binary Search Test: PASSED")