def cardinality(n, c):
    if c == 0:
        return 0
    if c == 1:
        return 1
    if 2 * c > n:
        return 0
    return cardinality(n - 1, c) * c + cardinality(n - 1, c - 1) * (n - 2 * c + 1)

for c in range(1, 11):
    print(20, c, cardinality(20, c) * 2**(-c))
