# Maxwell Richard Tamer-Mahoney ID #: 201804029

def powerset(lst):
    powerset = []
    for i in range(0, 2 ** len(lst)):
        temp = []
        for j in range(len(bin(i)[2:])):
            if bin(i)[2:][j] == '1':
                temp.append(lst[j])
        powerset.append(temp)
    return powerset

print(powerset([1, 2, 3]))
