# Maxwell Richard Tamer Mahoney ID #: 201804029
# Accepts m and n as arguments, and prints an m x n grid in column major order.
import sys

m = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(m):
    for j in range(n):
        print(str(i + m * j) + ' ', end="")
    print()
