def count_paren(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r:
        total += count_paren(n, l, r + 1)
    if l < n:
        total += count_paren(n, l + 1, r)
    return total
input("Count_paren counts every valid {} sequence = returns 1 at each valid end. press Enter")
print(" count_paren(1) =", count_paren(1))
print(" count_paren(2) =", count_paren(2))
n=int(input("Enter number pf pairs (try 3 or 4): "))
print("count_paren(", n, ") =", count_paren(n))