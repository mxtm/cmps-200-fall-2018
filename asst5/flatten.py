# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Flatten multi dimensional lists

def flatten(lst):
    result = []
    [result.extend(i) if type(i) is list else result.append(i) for i in lst]
    if any(isinstance(x, list) for x in result):
        return flatten(result)
    else:
        return result

print(flatten([[[2]],9,[2,1,[[13],2]],8,[2,6]]))
