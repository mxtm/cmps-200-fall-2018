# Maxwell Richard Tamer Mahoney ID #: 201804029
# Tell if numbers, taken from CLI args, are in order

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

inorder = (a < b < c) or (a > b > c)

print(inorder)
