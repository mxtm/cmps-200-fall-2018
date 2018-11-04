# Maxwell Richard Tamer-Mahoney ID #: 201804029

def powerset(lst):
    powerset = []
    needed_bits = len(bin(2 ** len(lst))[2:]) - 1
    for i in range(0, 2 ** len(lst)):
        temp = []
        binary_rep = bin(i)[2:].zfill(needed_bits)
        for j in range(len(binary_rep)):
            if binary_rep[j] == '1':
                temp.append(lst[j])
        powerset.append(temp)
    return powerset

print(powerset([1, 2, 3]))
