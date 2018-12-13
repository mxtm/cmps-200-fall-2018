# Maxwell Richard Tamer-Mahoney ID #: 201804029

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

"""
The computational complexity of fastfib is O(n). The space complexity (storage
needed) is also O(n).
"""
def fastfib(n, values={0:1, 1:1}):
    print(values)
    if n in values.keys():
        return values.get(n)
    else:
        values[n] = fastfib(n - 1, values) + fastfib(n - 2, values)
        return values[n]

print(fib(34))
print(fastfib(34))
