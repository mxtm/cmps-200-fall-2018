# Maxwell Richard Tamer Mahoney ID #: 201804029
# Some vowel related functions, then take a string input from the command line,
# returning the count of the vowels in it.
import sys

vowels = ['a', 'e', 'i', 'o', 'u']

def is_vowel(c):
    return c.lower() in vowels

def is_vowel2(c):
    c = c.lower()
    if c == 'a':
        return True
    elif c == 'e':
        return True
    elif c == 'i':
        return True
    elif c == 'o':
        return True
    elif c == 'u':
        return True
    else:
        return False

# The first is_vowel function is much better because it is much more concise
# and efficient, as checking the presence of a string in a list (3 lines) takes up much less
# time and resources than checking a string against 5 other strings (13 lines). It's also
# substantially more readable.

def count_vowels(string):
    count = 0
    for i in string:
        if is_vowel(i.lower()):
            count += 1
    return count

print(count_vowels(sys.argv[1]))
