scores = [12, 25, 33,41,50,67, 72, 85 ,91, 98]
n, target = len(scores), 98
print("=== Quiz Score Finder (n=", n, "scores) ===")
print("Scores:",scores, "| Target:", target)
print()
steps = 0
for i in range(n):
    steps += 1
    if scores[i] == target:
        print("Linear search  : index =", i,"| steps =", steps, "| 0(n)")
        break
print()
lo, hi, steps =0, n-1,0
while lo <= hi:
    mid = (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print("Binary search  : index =", mid,"| steps =", steps, "| O(log n)")
        break
    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print()


def binary_search_rec(scores,lo,hi,target,calls=0):
    calls += 1
    if lo > hi:
        return -1, calls
    mid = (lo + hi) // 2
    if scores[mid] == target:
        return mid, calls
    elif scores[mid] < target:
        return binary_search_rec(scores, mid + 1, hi, target, calls)
    else:
        return binary_search_rec(scores, lo, mid - 1, target, calls)
result, calls = binary_search_rec(scores, 0, n - 1, target)
print("Recursive binary search: index =", result, "| calls =",calls, "| O(log n)")
print()