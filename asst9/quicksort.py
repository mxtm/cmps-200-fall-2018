# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random, operator, string

def quicksort(L, comparison=operator.__lt__, start=0, end=None):
    """Takes input of a list, optionally a comparison operator, start index,
    and end index. Defaults to indices covering the whole list and the less
    than operator. Sorts the list in-place. Uses the partition() function to
    divide up the list and sort portions."""
    if end == None:
        end = len(L) - 1
    if start < end:
        p = partition(L, comparison, start, end)
        quicksort(L, comparison, start, p - 1)
        quicksort(L, comparison, p + 1, end)

def partition(L, comparison, start, end):
    """Takes input of a list, comparison operator, start index, and end index.
    Picks a random pivot point around which the list is split, and then sorts
    elements from start to end based upon whether they are less than or greater
    than the pivot."""
    k = random.randint(start, end)
    pivot = L[k]
    L[k], L[end] = L[end], pivot

    i = start
    j = end - 1
    while i <= j:
        while comparison(L[i], pivot) and i <= j:
            i += 1
        while not comparison(L[j], pivot) and j >= i:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]

    L[end] = L[i]
    L[i] = pivot
    return i

letters = [x for x in string.ascii_lowercase]

quicksort(letters, operator.__gt__)

print(letters)

"""
We expect quicksort to have O(n log n) complexity in the best case. This
occurs when the pivot point is around the middle value in the list,
and the list, when partitioned, is divided into relatively equally
sized portions.
The corresponding recurrence equation is T(n) = 2T(n/2) + O(n)

Yes, quicksort can exhibit O(n^2) behavior in the worst case when either the
smallest or largest element is the pivot point and the partitioned list
becomes very unbalanced as a result.
The recurrence relation for this case is T(n) = T(n - 1) + O(n)
"""
