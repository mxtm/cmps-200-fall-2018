# Maxwell Richard Tamer-Mahoney ID #: 201804029

class Element:
    def __init__(self, name, atomicNumber, symbol, atomicWeight):
        self.__name = name
        self.__atomicNumber = int(atomicNumber)
        self.__symbol = symbol
        self.__atomicWeight = float(atomicWeight)

    def getName(self):
        return self.__name

    def getAtomicNumber(self):
        return self.__atomicNumber

    def getSymbol(self):
        return self.__symbol

    def getAtomicWeight(self):
        return self.__atomicWeight

class PeriodicTable:

    table = {}

    def __init__(self, file):
        with open(file, 'r') as elementsFile:
            for line in elementsFile:
                parsedLine = line.split()
                if parsedLine[0] != 'Element':
                    self.table[parsedLine[2]] = Element(parsedLine[0], parsedLine[1], parsedLine[2], parsedLine[3])

    def parseAtom(self, atom):
        element, occurences = '', ''
        for char in atom:
            if char.isalpha():
                element += char
            elif char.isdigit():
                occurences += char
        if occurences == '':
            occurences = 1
        return (element, int(occurences))

    def weight(self, molecule):
        resultWeight = 0
        parsedMolecule = molecule.split()
        for i in parsedMolecule:
            parsedAtom = self.parseAtom(i)
            resultWeight += self.table.get(parsedAtom[0]).getAtomicWeight() * parsedAtom[1]

        return resultWeight

if __name__ == '__main__':
    myTable = PeriodicTable('elements.txt')
    print(myTable.weight('H2 O'))
