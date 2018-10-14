# Maxwell Richard Tamer Mahoney ID: 201804029
# Print the relative lengths of ruler subdivisions

def print_ruler_subdivisions(divisions):
    ruler = ' '
    for i in range(1, divisions + 1):
        ruler = ruler + str(i) + ruler
    print(ruler)

print_ruler_subdivisions(4)
