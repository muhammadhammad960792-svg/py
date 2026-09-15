# My Countdown Timer Challenge

# Step 1: Print the program title
print("=== My Countdown Timer Challenge ===")


# Step 2: Understand recursion
# Recursion means a function calls itself.
# The function must have a base case so it knows when to stop.


# Step 3: Create the countdown function
def countdown(n):
    # Step 4: Add the base case
    if n <= 0:
        print("Time's up!")
        return

    print(n)
    countdown(n - 1)


# Step 5: Build and run
print("\nStarting the countdown...")


# Step 6: Count from 1 to 10
print("\nCount from 1 to 10:")
for number in range(1, 11):
    print(number)


# Step 7: Create the factorial function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Step 8: Add stack overflow safety demo
# A very deep recursive call can cause a RecursionError.
# We use a small, safe limit instead of making an unsafe deep call.
def safe_countdown(n, limit=10):
    if n < 1:
        print("Please enter a positive number.")
        return

    if n > limit:
        print(f"Safety limit reached. Using {limit} instead.")
        n = limit

    countdown(n)


# Step 9: Run and test
print("\nTesting countdown:")
safe_countdown(10)

print("\nTesting factorial:")
print("5! =", factorial(5))

print("\nProgram completed successfully!")
