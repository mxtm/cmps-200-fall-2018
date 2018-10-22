# Maxwell Richard Tamer-Mahoney ID #: 201804029
# What number day of the year is MMM/DD?

import sys

days_in_months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31,
                  'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31,
                  'Nov': 30, 'Dec': 31}

def which_number_day(mmm, dd):
    number = 0
    for i, j in days_in_months.items():
        if i != mmm:
            number += j
        else:
            number += dd
            break
    return number

print(which_number_day(sys.argv[1].capitalize(), int(sys.argv[2])))
