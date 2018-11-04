# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random, time

def linear_search(lst, x):
    assert len(lst) > 0
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return None

def binary_search(lst, x):
    assert len(lst) > 0
    lowerBound, higherBound = 0, len(lst) - 1
    while lowerBound != higherBound:
        middle = (higherBound + lowerBound) // 2
        if x > lst[middle]:
            lowerBound = (higherBound + lowerBound) // 2 + 1
        elif x < lst[middle]:
            higherBound = (higherBound + lowerBound) // 2
        elif x == lst[middle]:
            return middle
    if lst[lowerBound] == x:
        return lowerBound
    else:
        return None

n = 10000000
lst = [random.randint(0, 100 * n) for i in range(n)]

ntrials = 100

start = time.time()
for i in range(ntrials):
    myRandomInteger = random.randint(0, 10e8)
    linear_search(lst, myRandomInteger)
end = time.time()
print('time to search (linear): ', (end-start)/ntrials, 'seconds')

start = time.time()
lst.sort()
end = time.time()
print('time to sort: ', (end-start), 'seconds')

start = time.time()
for i in range(ntrials):
    myRandomInteger = random.randint(0, 10e8)
    binary_search(lst, myRandomInteger)
end = time.time()
print('time to search (binary): ', (end-start)/ntrials, 'seconds')
