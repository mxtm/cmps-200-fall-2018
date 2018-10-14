# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Longest substring

def longest_substring(str):
    alphabeticalSubstrings = ['']
    for i in range(1, len(str)):
        if str[i - 1] <= str[i]:
            alphabeticalSubstrings[-1] += str[i - 1]
        else:
            alphabeticalSubstrings[-1] += str[i - 1]
            alphabeticalSubstrings.append('')

    if str[len(str) - 2] <= str[len(str) - 1]:
        alphabeticalSubstrings[-1] += str[len(str) - 1]
    else:
        alphabeticalSubstrings.append(str[len(str) - 1])

    return max(alphabeticalSubstrings, key=len)

print(longest_substring('a'))
