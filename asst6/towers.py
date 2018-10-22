# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Towers of Hanoi
"""
Calling towers('A', 'C', 'B', 3) will return:
(A, C) (A, B) (C, B) (A, C) (B, A) (B, C) (A, C)
Recursive call structure:
towers('A', 'C', 'B', 3)
    towers('A', 'B', 'C', 2)
        towers('A', 'C', 'B', 1) YIELDS (A, C)
        towers('A', 'B', 'C', 1) YIELDS (A, B)
        towers('C', 'B', 'A', 1) YIELDS (C, B)
    towers('A', 'C', 'B', 1) YIELDS (A, C)
    towers('B', 'C', 'A', 2)
        towers('B', 'A', 'C', 1) YIELDS (B, A)
        towers('B', 'C', 'A', 1) YIELDS (B, C)
        towers('A', 'C', 'B', 1) YIELDS (A, C)

"""
def towers(orig, dest, aux, n):
    if n == 1:
        return [(orig, dest)]
    else:
        return towers(orig, aux, dest, n - 1) + towers(orig, dest, aux, 1) + towers(aux, dest, orig, n - 1)

print(towers('A', 'C', 'B', 4))
