# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random

def shuffle(l):
    # If a list is length 1, the shuffled version is itself.
    if len(l) == 1:
        return l
    else:
        # Otherwise, we pick a halfway point using integer division
        halfway = len(l) // 2
        # We want to shuffle the two halves
        shuffled1, shuffled2 = shuffle(l[:halfway]), shuffle(l[halfway:])
        print(shuffled1, shuffled2)
        # Now we have to put back together our two halves into a result list
        result = []
        # While at least one list has an element...
        while len(shuffled1) != 0 or len(shuffled2) != 0:
            try:
                # Attempt to add the first element from the random list
                result.append(shuffled1.pop(random.randrange(len(shuffled1))))
                result.append(shuffled2.pop(random.randrange(len(shuffled2))))
            except ValueError:
                non_empty = shuffled1 if len(shuffled1) != 0 else shuffled2
                result.append(non_empty.pop(random.randrange(len(non_empty))))
        return result

lst1 = [i for i in range(20)]
print(shuffle(lst1))
