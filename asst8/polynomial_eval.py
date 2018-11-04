# Maxwell Richard Tamer-Mahoney ID #: 201804029

def peval1(a, x):
    solution = 0
    for i in range(len(a)):
        solution += a[i] * x ** i
    return solution

def peval2(a, x):
    if len(a) == 1:
        return a[0]
    else:
        return x * peval2(a[1:], x) + a[0]
        
print(peval1([1, 2, 2, 3, 5, 6], 10))
print(peval2([1, 2, 2, 3, 5, 6], 10))
