# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Functions involving pythagorean triplets

import sys

n = sys.argv[1]

def is_pythagorean_triplet(t):
    return t[0] ** 2 + t[1] ** 2 == t[2] ** 2

def is_multiple_of_smallest(t):
    return t[0] % 3 == 0 and t[1] % 4 == 0 and t[2] % 5 == 0

def generate_triplets(n):
    triplets = []
    for i in range(1, n):
        for j in range(i, n):
            if i + j >= n:
                break
            for k in range(j, n):
                if i + j + k >= n:
                    break
                if is_pythagorean_triplet((i, j, k)) and not is_multiple_of_smallest((i, j, k)):
                    triplets.append((i, j, k))
    return triplets

print(generate_triplets(int(n)))
