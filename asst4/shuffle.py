# Maxwell Richard Tamer-Mahoney ID #: 201804029
# In-place shuffle and printing

import random
import sys

def shuffle(lst):
    for i in range(len(lst)):
        myRandom = random.randrange(0, len(lst))
        lst[i], lst[myRandom] = lst[myRandom], lst[i]

myList = []
for i in range(1, len(sys.argv)):
    myList.append(sys.argv[i])

shuffle(myList)

[print(x, end=' ') for x in myList]
print()
