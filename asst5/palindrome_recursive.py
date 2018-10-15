# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Palindrome checker, but recursive

import sys

def is_palindrome2(st):
    if len(st) > 1:
        if st[0] == st[-1]:
            return is_palindrome2(st[1:-1])
        else:
            return False
    else:
        return True

print(is_palindrome2(sys.argv[1]))
