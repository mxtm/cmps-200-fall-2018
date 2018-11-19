# Maxwell Richard Tamer-Mahoney ID #: 201804029

from segment import Segment
import sys

segmentFile = sys.argv[1]
segments = []

with open(segmentFile, 'r') as file:
    for line in file:
        parsedLine = line.split()
        segments.append(Segment(parsedLine[0], parsedLine[1]))

segments.sort()

print('Sorted segments: {}\n'.format(' '.join([str(x) for x in segments])))

for i in range(len(segments)):
    for j in range(i, len(segments)):
        if segments[i].overlaps(segments[j]) and segments[i] != segments[j]:
            print('{} overlaps {}'.format(str(segments[i]), str(segments[j])))

boundingSegment = Segment(min([x.left() for x in segments]), max([x.right() for x in segments]))

print('\nBounding segment is: {}'.format(str(boundingSegment)))
