# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Fun functions with substrings

def substring(s1, s2, k):
    return s2[k:k+len(s1)] == s1

def how_many(s1, s2):
    count = 0
    for i in range(len(s2)):
        if substring(s1, s2, i):
            count += 1
    return count

print(how_many('bob', 'azcbobobegghakl'))
