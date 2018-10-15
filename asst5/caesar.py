# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Caesar cipher program which takes # of positions to shift and string to shift

import sys

k = int(sys.argv[1])
s = sys.argv[2]

def shift_character(k, c):
    return chr(ord(c) + k)

def crypt_string(k, s):
    return ''.join([shift_character(k, x) if x.isalpha() else x for x in s])

print(crypt_string(k, s))
