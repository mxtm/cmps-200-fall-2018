# Maxwell Richard Tamer-Mahoney ID #: 201804029

def merge(l, r):
    mergedList = []
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            mergedList.append(l.pop(0))
        elif r[0] < l[0]:
            mergedList.append(r.pop(0))
        else:
            mergedList.append(l.pop(0))
            mergedList.append(r.pop(0))
    while len(l) != 0:
        mergedList.append(l.pop(0))
    while len(r) != 0:
        mergedList.append(r.pop(0))
    return mergedList

print(merge([1, 5, 6, 8], [2, 3, 4, 5, 9]))

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        l = merge_sort(lst[:len(lst) // 2])
        r = merge_sort(lst[len(lst) // 2:])
        return merge(l, r)

print(merge_sort([500, 100, 200, 900, 600, 300]))
