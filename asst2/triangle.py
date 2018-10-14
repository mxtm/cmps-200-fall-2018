# Maxwell Richard Tamer Mahoney ID #: 201804029
# Accepts n, which creates a n x n triangular pattern as specified.
import sys

n = int(sys.argv[1])

for i in range(n):
    for l in range(i):
        print('. ', end='')
    for k in range(n - i):
        print('* ', end='')
    print()
