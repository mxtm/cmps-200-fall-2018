# Maxwell Richard Tamer-Mahoney ID #: 201804029

from disk import Disk

def construct_disk_list(file_name):
    disk_list = []
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()
            disk_list.append(Disk(values[0], values[1], values[2]))
    return disk_list

def sort_disk_list(disk_list):
    # The Python built-in sorting method uses the < operator which we defined so all we need is this
    disk_list.sort()

def count_intersecting_disks(disk_list):
    intersecting_disks = 0
    for i in range(0, len(disk_list)):
        # Starting j at i + 1 to not repeat checking if two disks intersect
        for j in range(i + 1, len(disk_list)):
            if disk_list[i].intersect(disk_list[j]):
                intersecting_disks += 1
    return intersecting_disks

def generate_bounding_box(disk_list):
    """We get the bounding box by the lower left corner and upper right corner,
    so we need: (lowest x point, lowest y point, highest x point, highest y point)"""
    assert disk_list == sorted(disk_list) and len(disk_list) > 1
    lowest_x_point = min([x.x() - x.radius() for x in disk_list])
    lowest_y_point = min([x.y() - x.radius() for x in disk_list])
    highest_x_point = max([x.x() + x.radius() for x in disk_list])
    highest_y_point = max([x.y() + x.radius() for x in disk_list])
    return (lowest_x_point, lowest_y_point, highest_x_point, highest_y_point)

if __name__ == '__main__':
    myDisks = construct_disk_list('data.txt')
    sort_disk_list(myDisks)
    print('Sorted disks:')
    [print(x) for x in myDisks]
    print('\nIntersecting pairs: {}'.format(count_intersecting_disks(myDisks)))
    print('\nBounding box: {}'.format(generate_bounding_box(myDisks)))
