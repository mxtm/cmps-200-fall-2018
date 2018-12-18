# Maxwell Richard Tamer-Mahoney ID #: 201804029

def subset(lst, value):
    if len(lst) == 1:
        return lst[0] == value
    else:
        return subset(lst[:len(lst) - 1], value) or subset(lst[:len(lst) - 1], value - lst[len(lst) - 1])

def subset2(lst, value, memo = {}):
    if (len(lst), value) in memo:
        return memo[(len(lst), value)]
    elif len(lst) == 1:
        result = lst[0] == value
    else:
        result = subset2(lst[:len(lst) - 1], value, memo) or subset2(lst[:len(lst) - 1], value - lst[len(lst) - 1], memo)
    memo[(len(lst), value)] = result
    return result

if __name__ == '__main__':
    print(subset2([1, 5, 3, 2], 8))
    print(subset2([1, 5, 3], 7))
    print(subset([1, 5, 3, 2], 8))
    print(subset([1, 5, 3], 7))
