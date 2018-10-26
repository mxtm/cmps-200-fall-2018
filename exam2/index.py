# Maxwell Richard Tamer-Mahoney ID #: 201804029

import sys

# The first argument is the file in question
myFile = sys.argv[1]
# Everything else in the arguments list are the words we are looking for
wordsToIndex = sys.argv[2:]

# Make a dictionary with each of the words in the wordsToIndex list as keys,
# and empty lists as values
# myIndex = dict().fromkeys(wordsToIndex, [])

# An alternative method, because my dictionary is not agreeing with me
indexes = [[] for x in range(len(wordsToIndex))]

# with open(file, mode) is beautiful because then I don't have to close the file
with open(myFile, 'r') as file:
    # Start counting lines at 1
    lineCount = 1
    for line in file:
        for i in range(len(wordsToIndex)):
            if wordsToIndex[i] in line:
                indexes[i].append(lineCount)
        '''
        # Unpack the dictionary
        for in myIndex.items():
            # If the dictionary key (the word) is in the line
            if k in line:
                # Add the line number to the dictionary value
                myIndex.get(k).append(lineCount)
        
        for word in wordsToIndex:
            if word in line:
                myIndex.get(word).append(lineCount)
        '''
        # Before going to the next line, increase the count
        lineCount += 1
    # Same thing except this is intended for if the whole file was loaded into a list
    # fileContents = [x for x in file]

# Same thing except this is intended for if the whole file was loaded into a list
'''
for i in range(len(fileContents)):
    for k, v in myIndex.items():
        if k in fileContents[i]:
            v.append(i + 1)
'''

# Unpack our dictionary yet again and format it beautifully using some list
# comprehension-fu, which causes less than beautiful code
#for k, v in myIndex.items():
#    print('{} {}'.format(k, ', '.join([str(x) for x in v])))

# Today is not my dictionary day so I'm trying this list solution.
for i in range(len(wordsToIndex)):
    print('{} {}'.format(wordsToIndex[i], ', '.join([str(x) for x in indexes[i]])))
