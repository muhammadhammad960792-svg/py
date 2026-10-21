
# PROJECT: KEYPAD WORD GENERATOR
# Topics: Recursion, Tower of Hanoi, Keypad Mapping,
#         Word Generation, and Recursion Tree Tracing


# STEP 1: UNDERSTAND RECURSION

def countdown(n):
    if n == 0:  # Base case
        print("Finished!")
        return

    print(n)
    countdown(n - 1)  # Recursive call


# STEP 2: TOWER OF HANOI

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# STEP 3: PHONE KEYPAD MAPPING

keypad = {
    "0": "0",
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


# STEP 4: GENERATE KEYPAD WORDS

def generate_keypad_words(digits):
    if not digits:
        return []

    results = []

    def backtrack(index, current_word):
        if index == len(digits):
            results.append(current_word)
            return

        digit = digits[index]

        for letter in keypad[digit]:
            backtrack(index + 1, current_word + letter)

    backtrack(0, "")
    return results


# STEP 5: TRACE THE RECURSION TREE

def trace_recursion_tree(digits):
    def trace(index, current_word, depth):
        indent = "  " * depth

        if index == len(digits):
            print(f"{indent}BASE CASE: {current_word}")
            return

        digit = digits[index]
        print(f"{indent}Digit {digit}: {keypad[digit]}")

        for letter in keypad[digit]:
            next_word = current_word + letter
            print(f"{indent}Choose {letter} -> {next_word}")
            trace(index + 1, next_word, depth + 1)

    trace(0, "", 0)


# MAIN PROGRAM

def main():
    print("=" * 40)
    print("      KEYPAD WORD GENERATOR")
    print("=" * 40)

    # Step 1
    print("\nSTEP 1: RECURSION")
    countdown(3)

    # Step 2
    print("\nSTEP 2: TOWER OF HANOI")
    try:
        disks = int(input("Enter number of disks (1-10): "))

        if not 1 <= disks <= 10:
            print("Enter a number from 1 to 10.")
            return

        tower_of_hanoi(disks, "A", "B", "C")

    except ValueError:
        print("Please enter a valid whole number.")
        return

    # Step 3
    print("\nSTEP 3: PHONE KEYPAD")
    for number, letters in keypad.items():
        print(f"{number} -> {letters}")

    # Step 4
    print("\nSTEP 4: GENERATE KEYPAD WORDS")
    digits = input("Enter phone digits (0-9): ").strip()

    if not digits or any(digit not in keypad for digit in digits):
        print("Invalid input! Enter digits from 0 to 9.")
        return

    combinations = generate_keypad_words(digits)

    print("\nGenerated combinations:")
    for word in combinations:
        print(word)

    print(f"Total combinations: {len(combinations)}")

    # Step 5
    print("\nSTEP 5: RECURSION TREE")
    trace_recursion_tree(digits)

    print("\nAll five steps completed!")


if __name__ == "__main__":
    main()
