# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random

def quickselect(lst, k, start=0, end=None):
    if end == None:
        end = len(lst) - 1
    if start < end:
        p = partition(lst, start, end)
        smaller = lst[:p]
        pivot_value = lst[p]
        larger = lst[p + 1:]
        if len(smaller) == k:
            return pivot_value
        elif len(smaller) == 1 and len(smaller) > k:
            return smaller[0]
        elif len(smaller) > k:
            return quickselect(smaller, k)
        elif len(smaller) < k and len(larger) == 1:
            return larger[0]
        elif len(smaller) < k:
            return quickselect(larger, k - len(smaller) - 1)

def partition(L, start, end):
    k = random.randint(start, end)
    pivot = L[k]
    L[k], L[end] = L[end], pivot

    i = start
    j = end - 1
    while i <= j:
        while L[i] < pivot and i <= j:
            i += 1
        while not L[j] < pivot and j >= i:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]

    L[end] = L[i]
    L[i] = pivot
    return i

if __name__ == '__main__':
    l = random.sample(range(1, 100), 25)
    l_sorted = sorted(l)
    print(l_sorted[8])
    print(quickselect(l, 8))
