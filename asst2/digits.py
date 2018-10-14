# Maxwell Richard Tamer Mahoney ID #: 201804029
# Functions to find the last and nth digits from the right of a number, used to
# print the last and next-to-last digits of all powers of 2 in the range 2^0 to
# 2^12.

def last_digit(number):
    return number % 10

def nth_digit(number, n):
    if n > 0:
        return int(number / int(10 ** n)) % 10
    else:
        return last_digit(number)

for i in range(13):
    powerOfTwo = 2 ** i
    print(last_digit(powerOfTwo), end=' ')
    print(nth_digit(powerOfTwo, 1))
