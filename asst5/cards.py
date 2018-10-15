# Maxwell Richard Tamer-Mahoney ID #: 201804029
# Fun functions simulating a deck of cards

import random

ranks = tuple(range(2, 11)) + ('Jack', 'Queen', 'King',  'Ace')
suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

def deck():
    return [str(y) + ' of ' + x for x in suits for y in ranks]

def choose_cards(n):
    myDeck = deck()
    return [random.choice(myDeck) for x in range(n)]

def draw_cards(n):
    myDeck = deck()
    random.shuffle(myDeck)
    return [myDeck[x] for x in range(n)]

def suit_count(hand):
    spades = len([x for x in hand if x.endswith('Spades')])
    hearts = len([x for x in hand if x.endswith('Hearts')])
    diamonds = len([x for x in hand if x.endswith('Diamonds')])
    clubs = len([x for x in hand if x.endswith('Clubs')])
    return [spades, hearts, diamonds, clubs]

print(choose_cards(10))
print(suit_count(draw_cards(10)))
