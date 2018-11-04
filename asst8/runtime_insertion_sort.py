# Maxwell Richard Tamer-Mahoney ID #: 201804029

import time, random

def insertion_sort(right_hand):
    assert len(right_hand) > 0
    left_hand = [right_hand[0]]
    right_hand.pop(0)
    while len(right_hand) != 0:
        for j in range(len(left_hand)):
            if right_hand[0] <= left_hand[j]:
                left_hand.insert(j, right_hand[0])
                right_hand.pop(0)
                break
            else:
                left_hand.append(right_hand[0])
                right_hand.pop(0)
                break

    right_hand[:] = left_hand

n = 10000
ntrials = 10
start = time.time()
for k in range(ntrials):
    lst = [random.randint(0, 1e4) for i in range(n)]
    insertion_sort(lst)
end = time.time()
print('time to sort (sorting unique lists):', (end-start)/ntrials, 'seconds')

start = time.time()
lst = [random.randint(0, 1e4) for i in range(n)]
for k in range(ntrials):
    insertion_sort(lst)
end = time.time()
print('time to sort (list already sorted):', (end-start)/ntrials, 'seconds')
