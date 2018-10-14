# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Fun functions with triangles
import math, sys

x, y, z = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

def is_valid(s1, s2, s3):
    return (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2)

def area(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

if is_valid(x, y, z):
    print('Valid triangle. Area is ' + str(area(x, y, z)))
else:
    print('Invalid triangle.')
