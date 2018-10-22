# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Greatest common divisor, recursively
def gcd(p, q):
    p, q = max(p, q), min(p, q)

    if p == 0 or q == 0:
        return max(p, q)
    elif p > q:
        return gcd(q, p % q)
    elif p == q:
        return p

print(gcd(102, 68))
