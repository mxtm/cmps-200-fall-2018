# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Diamonds

import sys

def diamond(n, c):
    for i in range(n):
        print(' ' * (n - i), end='')
        print('/', end='')
        print(c * (2 * i), end='')
        print('\\')
    for i in reversed(range(n)):
        print(' ' * (n - i), end='')
        print('\\', end='')
        print(c * (2 * i), end='')
        print('/')

diamond(int(sys.argv[1]), sys.argv[2])
