number =int(input("Enter your number:"))
orignal_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if orignal_number == reversed_number:
    print(f"{orignal_number} is a palindrome")
else:
    print(f"{orignal_number} is not a palindrome")

