# Maxwell Richard Tamer Mahoney ID #: 201804029
# Calculate which day of the week any day is, taking argument input in
# MM DD YYYY format

import sys

m, d, y = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

y0 = y-(14-m)//12
x = y0 + y0//4 - y0//100+y0//400
m0 = m+12*((14-m)//12)-2
d0 = (d + x + (31*m0)//12)%7

print (d0)
