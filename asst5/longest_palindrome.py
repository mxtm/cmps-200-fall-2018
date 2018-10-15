# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Find the longest palindrome inside a string

def is_palindrome(st):
    return st == st[::-1]

def longest_palin(st):
    return max([st[i:j+1] for i in range(0, len(st)) for j in range(i, len(st)) if is_palindrome(st[i:j+1])], key=len)

print(longest_palin('43xyyx1'))
