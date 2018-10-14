# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Computer guesses the number between 1 and 1000

lowerBound = 1
higherBound = 1000

while lowerBound != higherBound:
    theQuestion = input('Is your number less than or equal to ' + str((higherBound +
                                                        lowerBound) // 2) + '? ')
    if theQuestion == 'True':
        higherBound = (higherBound + lowerBound) // 2
    else:
        lowerBound = (higherBound + lowerBound) // 2 + 1

print('Your number is ' + str(lowerBound))
