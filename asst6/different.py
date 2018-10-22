# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Distinct entries in 2D table
# First flatten it, and then turn it in to a set so no duplicates

def different(table):
    return len(set([j for i in table for j in i]))

t = [[1,0,1],[0,1,0]]
print(different(t))
t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
print(different(t))
