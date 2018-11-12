# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Find the longest palindrome inside a string

def is_palindrome(st):
    """Takes a string input and returns a boolean that tells whether it is
    equal to itself reversed (or, whether it is a palindrome)."""
    return st == st[::-1]

def construct_palindrome_list(st):
    """Takes a string input and returns a list constructed of palindromes inside
    the string. The list of palindromes is constructed by trying to expand the
    palindrome to the left or the right, starting with either a character (for
    odd-length) or an empty string 'between' characters (for even-length)."""
    palindromes = []
    for i in range(1, len(st)):
        # Handle odd-length palindromes
        currentLeftChar, currentRightChar = i - 1, i + 1
        palindrome = st[i]
        while currentLeftChar >= 0 and currentRightChar < len(st) and st[currentLeftChar] == st[currentRightChar]:
            palindrome = st[currentLeftChar] + palindrome + st[currentRightChar]
            currentLeftChar -= 1
            currentRightChar += 1
        palindromes.append(palindrome)
        # Handle even-length palindromes
        currentLeftChar, currentRightChar = i - 1, i 
        palindrome = ''
        while currentLeftChar >= 0 and currentRightChar < len(st) and st[currentLeftChar] == st[currentRightChar]:
            palindrome = st[currentLeftChar] + palindrome + st[currentRightChar]
            currentLeftChar -= 1
            currentRightChar += 1
        palindromes.append(palindrome)
    return palindromes

def longest_palin(st):
    """Takes a string input, and after constructing the list of palindromes
    inside the string using construct_palindrome_list(), picks the longest one."""
    return max(construct_palindrome_list(st), key=len)

print(longest_palin('racecara'))

"""
The complexity of this algorithm is O(n).
"""
