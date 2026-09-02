def is_power_of_two(n):
    """Step 1 & 2: n & (n-1) trick to check power of 2"""
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_four(n):
    """Step 3: check power of 4 (must be power of 2 AND remainder pattern on odd bit positions)"""
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0


def is_power_of_eight(n):
    """Step 4: check power of 8 (must be power of 2 AND exponent divisible by 3)"""
    if n <= 0 or (n & (n - 1)) != 0:
        return False
    exponent = n.bit_length() - 1
    return exponent % 3 == 0


def binary_exponentiation(base, exp, mod=None):
    """Step 5: fast power calculation using binary exponentiation"""
    result = 1
    base = base if mod is None else base % mod
    while exp > 0:
        if exp & 1:
            result = result * base if mod is None else (result * base) % mod
        base = base * base if mod is None else (base * base) % mod
        exp >>= 1
    return result


def scan_powers(limit):
    """Combined scanner: reports which numbers up to limit are powers of 2, 4, 8"""
    print(f"{'N':>6} | {'Pow2':>5} | {'Pow4':>5} | {'Pow8':>5}")
    print("-" * 34)
    for n in range(1, limit + 1):
        p2 = is_power_of_two(n)
        p4 = is_power_of_four(n)
        p8 = is_power_of_eight(n)
        if p2:  # only print numbers that are at least power of 2
            print(f"{n:>6} | {str(p2):>5} | {str(p4):>5} | {str(p8):>5}")


def run_tests():
    """Step 6: run and test the program"""
    print("=== Power of 2 tests ===")
    for n in [1, 2, 3, 4, 16, 18, 1024, 1023]:
        print(f"is_power_of_two({n}) = {is_power_of_two(n)}")

    print("\n=== Power of 4 tests ===")
    for n in [1, 4, 8, 16, 64, 100]:
        print(f"is_power_of_four({n}) = {is_power_of_four(n)}")

    print("\n=== Power of 8 tests ===")
    for n in [1, 8, 16, 64, 512, 100]:
        print(f"is_power_of_eight({n}) = {is_power_of_eight(n)}")

    print("\n=== Binary Exponentiation tests ===")
    print(f"2^10 = {binary_exponentiation(2, 10)}")
    print(f"3^13 = {binary_exponentiation(3, 13)}")
    print(f"7^500 mod 1000000007 = {binary_exponentiation(7, 500, 1000000007)}")

    print("\n=== Scanner (1 to 300) ===")
    scan_powers(300)


if __name__ == "__main__":
    run_tests()
