keys = {'2' : 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
def count_combos(digits):
    if len(digits) == 0:
     return 1
    return len(keys[digits[0]]) * count_combos(digits[1:])
input("Count_combos multiples letter chices at each digit - e letters per step. Press Enter")
print(" count_combos('2') =", count_combos('2'))
print("count_combos('23') =", count_combos('23'))

