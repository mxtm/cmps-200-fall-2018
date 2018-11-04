# Maxwell Richard Tamer-Mahoney ID #: 201804029

def insertion_sort(right_hand):
    assert len(right_hand) > 0
    left_hand = [right_hand[0]]
    right_hand.pop(0)
    while len(right_hand) != 0:
        for j in range(len(left_hand)):
            if right_hand[0] <= left_hand[j]:
                left_hand.insert(j, right_hand[0])
                right_hand.pop(0)
                break
            else:
                left_hand.append(right_hand[0])
                right_hand.pop(0)
                break

    right_hand[:] = left_hand

print(insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(insertion_sort([500, 300, 700, 900, 10000]))
