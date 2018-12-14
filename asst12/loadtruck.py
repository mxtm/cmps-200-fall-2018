# Maxwell Richard Tamer-Mahoney ID #: 201804029

import random

totalVolumes = lambda l: sum([x.volume() for x in l])
totalValues = lambda l: sum([x.value() for x in l])

def highestValue(lst):
    maximumValue = 0
    maximumValueIndex = -1
    for i in range(len(lst)):
        if lst[i].value() > maximumValue:
            maximumValue = lst[i].value()
            maximumValueIndex = i
    return maximumValueIndex

def powerset(lst):
    powerset = []
    needed_bits = len(bin(2 ** len(lst))[2:]) - 1
    for i in range(0, 2 ** len(lst)):
        temp = []
        binary_rep = bin(i)[2:].zfill(needed_bits)
        for j in range(len(binary_rep)):
            if binary_rep[j] == '1':
                temp.append(lst[j])
        powerset.append(temp)
    return powerset

def generateRandomItems(n):
    types = ['TVs', 'Desktop Computers', 'Lamps', 'Washing Machines', 'Beer', 'Wine',
             'Vodka', 'Whiskey', 'Gin', 'Coffee Machines', 'Coffee', 'Laptops',
             'Smartphones', 'Pocket Knives']
    return [Item(random.choice(types), random.randint(1, 10), random.randint(100, 1000)) for x in range(n)]

class Item:
    def __init__(self, itemType, itemVolume, itemValue):
        self.__itemType = itemType
        self.__itemVolume = int(itemVolume)
        self.__itemValue = int(itemValue)

    def __str__(self):
        return f'{self.type()}: ${self.value()}, {self.volume()} m^3'

    def type(self):
        return self.__itemType

    def setType(self, newType):
        self.__itemType = newType

    def volume(self):
        return self.__itemVolume

    def setVolume(self, newVolume):
        self.__itemVolume = newVolume

    def value(self):
        return self.__itemValue

    def setValue(self, newValue):
        self.__itemValue = newValue

class Truck:
    def __init__(self, truckID, volume):
        self.__truckID = str(truckID)
        self.__volume = int(volume)
        self.__loadedItems = []

    def __str__(self):
        return f'{self.truckID()}: {self.volume()} m^3'

    def truckID(self):
        return self.__truckID

    def setTruckID(self, newTruckID):
        self.__truckID = newTruckID

    def volume(self):
        return self.__volume

    def setVolume(self, newVolume):
        self.__volume = newVolume

    def getLoadedVolume(self):
        return totalVolumes(self.loadedItems())

    def loadedItems(self):
        return self.__loadedItems

    def loadItem(self, item):
        self.__loadedItems.append(item)

    def loadbf(self, items):
        possibleLoads = [x for x in powerset(items) if totalVolumes(x) <= self.volume()]
        bestLoad = max(possibleLoads, key=totalValues)
        [self.loadItem(x) for x in bestLoad]

    def loadgreedy(self, items, keyFunction=highestValue): 
        while self.getLoadedVolume() < self.volume():
            greedyChoice = keyFunction(items)
            if items[greedyChoice].volume() + self.getLoadedVolume() <= self.volume():
                self.loadItem(items.pop(greedyChoice))
            else:
                break

    def loaddp(self, items):
        def calcdp(items, remainingVolume=None, memo={}):
            if remainingVolume == None:
                remainingVolume = self.volume()

            if (len(items), remainingVolume) in memo:
                result = memo[(len(items), remainingVolume)]
            elif len(items) == 0 or remainingVolume == 0:
                result = (0, ())
            elif items[0].volume() > remainingVolume:
                result = calcdp(items[1:], remainingVolume, memo)
            else:
                nextItem = items[0]
                withVal, withToTake = calcdp(items[1:], remainingVolume - nextItem.volume(), memo)
                withVal += nextItem.value()
                withoutVal, withoutToTake = calcdp(items[1:], remainingVolume, memo)
                if withVal > withoutVal:
                    result = (withVal, withToTake + (nextItem,))
                else:
                    result = (withoutVal, withoutToTake)
            memo[(len(items), remainingVolume)] = result
            return result
        [self.loadItem(x) for x in calcdp(items)[1]]

if __name__ == '__main__':
    truckID = input('Please enter the truck ID: ')
    volume = input('Please enter the truck volume (in m^3): ')
    n = int(input('How many random items would you like to generate?: '))

    myTruck = Truck(truckID, volume)
    myItems = generateRandomItems(n)

    print('I have generated the following random items:')
    [print(x) for x in myItems]

    myTruck.loaddp(myItems)

    print('The truck is now loaded with the following items:')
    [print(x) for x in myTruck.loadedItems()]
