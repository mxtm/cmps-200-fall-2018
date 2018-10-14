import sys

n = int(sys.argv[1])

for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print('o', end=' ')
        else:
            print('x', end=' ')
    print()
