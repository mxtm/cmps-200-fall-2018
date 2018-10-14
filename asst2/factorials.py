# Maxwell Richard Tamer Mahoney ID #: 201804029
# Prints the factorials of the odd numbers between 1 and 10.

def factorial(n):
    i = n
    for j in reversed(range(1, n)):
        i = i * j
    return i

for i in range(1, 11):
    if i % 2 != 0:
        print(factorial(i))
