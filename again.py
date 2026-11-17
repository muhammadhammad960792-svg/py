def max_zeros(n):
    arr = [1] + [0]*n + [1]
    streak = best = 0
    for x in arr:
        if not x:streak +=1
        else: streak = 0
        if streak > best: best = streak
    return best
input("max_zeros(n) finds the longest fun of 0s in [1,0..0,1.Press Enter]")
print("max_Zeros (3) =", max_zeros(3))

