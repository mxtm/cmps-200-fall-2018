import sys

st = sys.argv[1]

def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u']

def vcv(st):
    newString = ''
    for i in range(1, len(st) - 1):
        if is_vowel(st[i - 1]) and is_vowel(st[i + 1]):
            newString += st[i]
    print(str(len(newString)) + ' vcv characters: ' + newString)
    return newString

vcv(st)
