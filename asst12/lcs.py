# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random, sys

def generate_sequences(n, m):
    valid_chars = ('A', 'C', 'G', 'T')
    result = []
    for i in range(n):
        result.append('')
        for j in range(m):
           result[i] += random.choice(valid_chars)
    return result

def LCS(s1, s2):
    L = []
    for i in range(len(s1) + 1):
        L.append([])
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                L[i].append(0)
            elif s1[i - 1] == s2[j - 1]:
                L[i].append(L[i - 1][j - 1] + 1)
            elif s1[i - 1] != s2[j - 1]:
                L[i].append(max(L[i - 1][j], L[i][j - 1]))
    return L

def find_LCS(s1, s2, L):
    result = ''
    x, y = len(s1), len(s2)
    while x > 0 and y > 0:
        if L[x][y] == L[x - 1][y]:
            x -= 1
        elif L[x][y] == L[x][y - 1]:
            y -= 1
        else:
            assert s1[x - 1] == s2[y - 1]
            result = s1[x - 1] + result
            x -= 1
            y -= 1
    return result

seqs = generate_sequences(3, 10)
print(seqs[0], seqs[1])
print(find_LCS(seqs[0], seqs[1], LCS(seqs[0], seqs[1])))
