def gcd(a, b):
    m = min(a, b)
    if a % m == 0 and b % m == 0:
        return m
    else:
        for i in range(m, 0, -1):
             if a % i == 0 and b % i == 0:
                return i

# Test
gcd(9, 5)
gcd(10, 4)
gcd(1024, 9800)