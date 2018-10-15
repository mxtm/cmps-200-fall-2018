# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Factorial, but recursive

def rfactorial(n):
    if n > 0:
        return n * rfactorial(n-1)
    else:
        return 1

print(rfactorial(10))
