# ==========================================
#        SCORE LIST EXPLORER
# ==========================================

scores = [85, 90, 75, 95, 88]

# Step 1: Explore the head-tail pattern
# Head = first item
# Tail = remaining items

def head_tail(scores):
    if len(scores) == 0:
        return None, []

    head = scores[0]
    tail = scores[1:]

    return head, tail


# Step 2: Create a base case for the list
def is_empty(scores):
    if len(scores) == 0:
        return True
    return False


# Step 3: Check whether the list is sorted
def is_sorted(scores):
    if len(scores) <= 1:
        return True

    if scores[0] > scores[1]:
        return False

    return is_sorted(scores[1:])


# Step 4: Calculate the recursive sum
def recursive_sum(scores):
    if len(scores) == 0:
        return 0

    return scores[0] + recursive_sum(scores[1:])


# Step 5: Find the largest score
def largest_score(scores):
    if len(scores) == 1:
        return scores[0]

    largest_in_tail = largest_score(scores[1:])

    if scores[0] > largest_in_tail:
        return scores[0]
    else:
        return largest_in_tail


# Step 6: Complete Score List Explorer
print("===== SCORE LIST EXPLORER =====")

print("Scores:", scores)

head, tail = head_tail(scores)
print("Head:", head)
print("Tail:", tail)

print("Is list empty?", is_empty(scores))

print("Is list sorted?", is_sorted(scores))

print("Recursive sum:", recursive_sum(scores))

print("Largest score:", largest_score(scores))