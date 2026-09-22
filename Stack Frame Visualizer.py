# ============================================================
# PYTHON RECURSION STACK FRAME VISUALIZER
# ============================================================

print("=" * 60)
print("       PYTHON RECURSION STACK FRAME VISUALIZER")
print("=" * 60)


# ------------------------------------------------------------
# STACK FRAME VISUALIZER
# ------------------------------------------------------------

stack = []


def show_frame(action, function_name, n):
    if action == "PUSH":
        stack.append(f"{function_name}({n})")

    elif action == "POP":
        if stack:
            stack.pop()

    print("\n" + action + ": " + function_name + "(" + str(n) + ")")
    print("+-----------------------------------+")

    if stack:
        for frame in reversed(stack):
            print("| " + frame.ljust(33) + " |")
    else:
        print("| " + "EMPTY".ljust(33) + " |")

    print("+-----------------------------------+")


# ------------------------------------------------------------
# 1. LINEAR RECURSION
# One recursive call
# ------------------------------------------------------------

def linear_recursion(n):

    show_frame("PUSH", "linear", n)

    if n > 0:
        linear_recursion(n - 1)

    show_frame("POP", "linear", n)


# ------------------------------------------------------------
# 2. TAIL RECURSION
# Recursive call is the last operation
# ------------------------------------------------------------

def tail_recursion(n):

    show_frame("PUSH", "tail", n)

    if n > 0:
        print("Processing:", n)

        tail_recursion(n - 1)

    show_frame("POP", "tail", n)


# ------------------------------------------------------------
# 3. HEAD RECURSION
# Recursive call happens before the other operation
# ------------------------------------------------------------

def head_recursion(n):

    show_frame("PUSH", "head", n)

    if n > 0:

        head_recursion(n - 1)

        print("Printing:", n)

    show_frame("POP", "head", n)


# ------------------------------------------------------------
# 4. INCREASING-DECREASING RECURSION
# First decreases, then increases
# ------------------------------------------------------------

def increasing_decreasing(n):

    show_frame("PUSH", "inc_dec", n)

    if n > 0:

        print("Decreasing:", n)

        increasing_decreasing(n - 1)

        print("Increasing:", n)

    show_frame("POP", "inc_dec", n)


# ------------------------------------------------------------
# 5. TREE RECURSION
# More than one recursive call
# ------------------------------------------------------------

def tree_recursion(n):

    show_frame("PUSH", "tree", n)

    if n > 0:

        print("Branch 1 from:", n)
        tree_recursion(n - 1)

        print("Branch 2 from:", n)
        tree_recursion(n - 1)

    show_frame("POP", "tree", n)


# ------------------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------------------

def final_summary():

    print("\n")
    print("=" * 60)
    print("                    FINAL SUMMARY")
    print("=" * 60)

    print("Linear Recursion")
    print("-> Function calls itself one time.")

    print("\nTail Recursion")
    print("-> Recursive call is the last operation.")

    print("\nHead Recursion")
    print("-> Recursive call happens before the other operation.")

    print("\nIncreasing-Decreasing Recursion")
    print("-> First goes down, then comes back up.")

    print("\nTree Recursion")
    print("-> Function calls itself more than one time.")

    print("=" * 60)


# ------------------------------------------------------------
# MAIN PROGRAM
# Run and Test Everything Together
# ------------------------------------------------------------

def main():

    n = 3

    print("\nStarting with n =", n)

    print("\n\n========== LINEAR RECURSION ==========")
    linear_recursion(n)

    print("\n\n========== TAIL RECURSION ==========")
    tail_recursion(n)

    print("\n\n========== HEAD RECURSION ==========")
    head_recursion(n)

    print("\n\n========== INCREASING-DECREASING RECURSION ==========")
    increasing_decreasing(n)

    print("\n\n========== TREE RECURSION ==========")
    tree_recursion(n)

    final_summary()

    print("\nProgram completed successfully! ✓")


# ------------------------------------------------------------
# START PROGRAM
# ------------------------------------------------------------

if __name__ == "__main__":
    main()