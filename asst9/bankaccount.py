# Maxwell Richard Tamer-Mahoney ID #: 201804029

class BankAccount:
    """A class representing a bank account."""
    def __init__(self, balance=0):
        """Initializes an instance of the class with a balance, by default 0.
        Makes sure that the balance is not negative, and throws an exception if
        it is."""
        if balance < 0:
            raise ValueError('Illegal balance')
        else:
            self.bal = balance
    def withdraw(self, amount):
        """Withdrawls from an instance of the class. Makes sure that the
        withdrawal isn't greater than the balance, and throws an exception if
        so."""
        if amount > self.bal:
            raise ValueError('Overdraft')
        else:
            self.bal -= amount
    def deposit(self, amount):
        """Deposits into an instance of the class. Makes sure that the deposit
        isn't a negative amount, and throws an exception if so."""
        if amount < 0:
            raise ValueError('Negative deposit')
        else:
            self.bal += amount
    def balance(self):
        """Returns the balance of an instance of the class."""
        return self.bal
    def __eq__(self, other):
        """Returns a boolean that indicates whether this instance is equal to
        another (in the balance)."""
        return self.bal == other.bal
    def __str__(self):
        """Returns a string representation of this instance."""
        return '$' + str(self.bal)

if __name__ == '__main__':
    print('Creating an instance of BankAccount with balance $700')
    x = BankAccount(700)
    print('Checking if balance is correct:', x.balance() == 700)
    x.withdraw(70)
    print('Checking if balance is correct after withdrawing $70:', x.balance() == 630)
    x.deposit(7)
    print('Checking if balance is correct after depositing $7:', x.balance() == 637)
    print('Creating new instance of BankAccount with same balance')
    y = BankAccount(637)
    print('Checking if accounts are equal:', x == y)
    print('String representations of both accounts:', x, y)
