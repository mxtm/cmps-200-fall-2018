# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Palindromes, with while

import sys

def is_palindrome(st):
    """You could also do this but I don't think that's what y'all want
    return st == st[::-1]
    """
    ltr_counter = 0
    rtl_counter = len(st) - 1
    while rtl_counter >= 0:
        if st[ltr_counter] != st[rtl_counter]:
            return False
        ltr_counter += 1
        rtl_counter -= 1
    return True

print(is_palindrome(sys.argv[1]))
