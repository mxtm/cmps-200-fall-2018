# Maxwell Richard Tamer-Mahoney ID #: 201804029

import math

def build_table(lst):
    # Our n (as in n x n) is the sqrt of the length of the list. If n ^ 2 is
    # not equal to the integer casting of this sqrt, it can't be a perfect
    # square.
    n = int(math.sqrt(len(lst)))
    assert n ** 2 == len(lst)
    # Make an empty table that is n x n using list comp.
    table = [[] for i in range(n)]
    # Go over the table appending each element in the list to it in the proper
    # position. lst[i * 3 + j] keeps us progressing along the original list and
    # not repeating any objects
    for i in range(n):
        for j in range(n):
            table[i].append(lst[i * 3 + j])
    return table

def transpose(table):
    # This is kind of a hacky solution, but if I just make an n x n table of 0s
    # that matches the dimensions of the other, switching it to reverse the
    # rows and columns is easy as pie.
    transposedTable = []
    for i in range(len(table)):
        transposedTable.append([])
        for j in range(len(table)):
            transposedTable[i].append(0)
    # Just setting the row and column of the new table to the column and row of
    # the old table, respectively.
    for i in range(len(table)):
        for j in range(len(table)):
            transposedTable[j][i] = table[i][j]

    return transposedTable

def transpose_inplace(table):
    # Because of the usage of [::] it will be modified in place, and will be given the
    # value returned from the other function, overwriting the old table w/ it
    table[::] = transpose(table)

myTable = build_table([1, 2, 3, 4, 5, 6, 7, 8, 9])
transpose_inplace(myTable)
print(myTable)
