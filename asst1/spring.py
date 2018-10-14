# Maxwell Richard Tamer Mahoney ID: 201804029
# Tells you if a date is in the spring, with MM DD input in args

import sys

month = int(sys.argv[1])
day = int(sys.argv[2])
spring = (month == 3 and day >= 21) or (4 <= month <= 5) or (month == 6 and day
                                                            <= 20)

print(spring)
