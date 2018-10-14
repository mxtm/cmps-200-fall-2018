# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Construct list of floats, return smallest of positive floats list

import sys

def string2floats(ls):
    listOfFloats = []
    for i in ls:
        listOfFloats.append(float(i))
    return listOfFloats

def positive_min(lf):
    return min([x for x in lf if x >= 0])

myArguments = []
for i in range(1, len(sys.argv)):
    myArguments.append(sys.argv[i])

print('positive minimum is: ' + str(positive_min(string2floats(myArguments))))
