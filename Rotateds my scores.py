
# ==========================================
# PROJECT TITLE: ROTATE MY SCORES
# LANGUAGE: PYTHON
# ==========================================

# Step 1: Set Up the Project

def display_scores(scores):
    print("Scores:", scores)


# Step 2: Reverse Scores Using Two Pointers

def reverse_two_pointers(scores):
    left = 0
    right = len(scores) - 1

    while left < right:
        scores[left], scores[right] = scores[right], scores[left]
        left += 1
        right -= 1

    return scores


# Step 3: Reverse Scores in Groups

def reverse_in_groups(scores, k):
    n = len(scores)

    for i in range(0, n, k):
        scores[i:i+k] = scores[i:i+k][::-1]

    return scores


# Step 4: Left Rotate by 1

def left_rotate_by_one(scores):
    if len(scores) == 0:
        return scores

    first = scores[0]

    for i in range(len(scores) - 1):
        scores[i] = scores[i + 1]

    scores[-1] = first

    return scores


# Step 5: Left Rotate by N

def left_rotate_by_n(scores, n):
    size = len(scores)

    if size == 0:
        return scores

    n = n % size

    return scores[n:] + scores[:n]


# Step 6: Find Leaders in an Array

def find_leaders(scores):
    leaders = []
    maximum = float('-inf')

    for i in range(len(scores) - 1, -1, -1):
        if scores[i] >= maximum:
            leaders.append(scores[i])
            maximum = scores[i]

    leaders.reverse()

    return leaders


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("===================================")
    print("       ROTATE MY SCORES")
    print("===================================")

    scores = list(map(int, input(
        "Enter your scores separated by spaces: "
    ).split()))

    while True:

        print("\n========== MENU ==========")
        print("1. Reverse Scores Using Two Pointers")
        print("2. Reverse Scores in Groups")
        print("3. Left Rotate by 1")
        print("4. Left Rotate by N")
        print("5. Find Leaders in an Array")
        print("6. Display Original Scores")
        print("7. Exit")
        print("==========================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            result = reverse_two_pointers(scores.copy())
            print("Reversed Scores:", result)

        elif choice == "2":
            k = int(input("Enter group size: "))

            if k <= 0:
                print("Group size must be greater than zero.")
            else:
                result = reverse_in_groups(scores.copy(), k)
                print("Scores Reversed in Groups:", result)

        elif choice == "3":
            result = left_rotate_by_one(scores.copy())
            print("Scores After Left Rotation by 1:", result)

        elif choice == "4":
            n = int(input("Enter number of rotations: "))
            result = left_rotate_by_n(scores.copy(), n)
            print("Scores After Left Rotation by N:", result)

        elif choice == "5":
            result = find_leaders(scores)
            print("Leaders in Scores:", result)

        elif choice == "6":
            display_scores(scores)

        elif choice == "7":
            print("Thank you for using Rotate My Scores!")
            print("Program Closed Successfully.")
            break

        else:
            print("Invalid choice! Please select from 1 to 7.")


# Run the Program

if __name__ == "__main__":
    main()
