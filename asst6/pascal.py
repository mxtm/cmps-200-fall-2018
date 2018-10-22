# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Pascal's triangle

import math, sys

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def generate_pascal(n):
    pascal = [[1]]
    for i in range(1, n + 1):
        pascal.append([])
        for j in range(i + 1):
            pascal[i].append(nCr(i, j))
    return pascal

def print_triangle(coeffs):
    for i in generate_pascal(coeffs):
        [print(j, end=' ') for j in i]
        print()

print_triangle(int(sys.argv[1]))
