# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Palindromes

import sys

def is_palindrome(st):
    """You could also do this but I don't think that's what y'all want
    return st == st[::-1]
    """
    for i in range(len(st)):
        if st[i] != st[len(st) - i - 1]:
            return False
    return True

print(is_palindrome(sys.argv[1]))
