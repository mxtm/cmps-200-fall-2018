# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Dictionary statistics functions

def how_many(d):
    return len([y for x in d.values() for y in x])

def biggest(d):
    return max([x for x in d.items()])[0]

def dstats(d):
    return (how_many(d), len(max([x for x in d.values()], key=len)))

animals = { 'a': ['horse'], 'b': ['baboon'], 'c': ['giraffe']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
print(biggest(animals))
print(dstats(animals))
