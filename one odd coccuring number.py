input("XOR all numbers - pairs cancel, the odd one stays. Press Enter")
print(" list: [2, 3, 4, 3, 2]")
print(" Odd -occuring:", 2 ^ 3 ^ 4 ^ 3 ^ 2)
n =int(input("Enter a number ( try 7 or 11): "))
nums = [3, n, 5, 3, 5]
guess = int(input("Which number in " + str(nums) + " occurs only once? "))
result = 0
for x in nums:
    result ^= x
input("XOR cancles pairs - the odd one survives. Press Enter ")
print(" list:",nums, " odd -occuring:", result, " your guess:", guess)
