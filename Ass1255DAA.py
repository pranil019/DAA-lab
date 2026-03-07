def karatsuba(x, y):

    # Base Case
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    a = x // 10**half
    b = x % 10**half
    c = y // 10**half
    d = y % 10**half

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    return (ac * 10**(2 * half)) + (ad_plus_bc * 10**half) + bd


# Testing with multiple large numbers
test_cases = [
    (123456789012345, 987654321098765),
    (999999999999999, 888888888888888),
    (123456789123456789, 987654321987654321)
]

for x, y in test_cases:
    print("Number 1:", x)
    print("Number 2:", y)
    print("Product :", karatsuba(x, y))
    print("-" * 50)

