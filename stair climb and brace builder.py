# ==========================================
# RECURSION PROJECT
# Climb Stairs + Balanced Parentheses
# ==========================================


# ------------------------------------------
# PART 1: CLIMB STAIRS
# ------------------------------------------

def climb_stairs(n):

    # Base case
    if n == 0:
        return 1

    if n < 0:
        return 0

    # Try taking 1 step
    one_step = climb_stairs(n - 1)

    # Try taking 2 steps
    two_step = climb_stairs(n - 2)

    # Total ways
    return one_step + two_step


n = 4

print("Climb Stairs")
print("Number of ways:", climb_stairs(n))


# ------------------------------------------
# PART 2: BALANCED PARENTHESES
# ------------------------------------------

def parentheses(s, left, right, position, n):

    # Base case
    if position == 2 * n:
        print("".join(s))
        return

    # Add opening bracket
    if left < n:
        s[position] = "{"
        parentheses(
            s,
            left + 1,
            right,
            position + 1,
            n
        )

    # Add closing bracket
    if right < left:
        s[position] = "}"
        parentheses(
            s,
            left,
            right + 1,
            position + 1,
            n
        )


n = 2
s = [""] * (2 * n)

print("\nBalanced Parentheses")
parentheses(s, 0, 0, 0, n)