# Maxwell Richard Tamer Mahoney ID #: 201804029
# Accepts a command line argument (a year), tells if it is a leap year or not
import sys

year = int(sys.argv[1])

isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400
                                                 == 0)

print(isLeap)
