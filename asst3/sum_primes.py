# Maxwell Richard Tamer-Mahoney ID #: 201804029

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum_of_primes = 0

while True:
    given_number = int(input('Pick a positive integer: '))
    if given_number == 0:
        print('The sum of your entered primes is ' + str(sum_of_primes))
        break
    elif is_prime(given_number):
        sum_of_primes += given_number
