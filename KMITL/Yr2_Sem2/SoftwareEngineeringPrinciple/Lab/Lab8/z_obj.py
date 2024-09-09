import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod

class Customer(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer Name: " + self.name
    
    def setName(self, name):
        self.name = name

    def addAccount(self, account):
        self.accounts.append(account)
        return account

    def getAccounts(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def printStatus(self):
        print(self)
        for account in self.accounts:
            print("", end="    ")
            account.printStatus()

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None):
        self.balance = balance
        self.owner = owner

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def deposit(self, amount):
        self.balance += amount        

    @abstractmethod
    def withdraw(self, amount):
        pass

    def transfer(self, amount, account):
        self.withdraw(amount)
        account.deposit(amount)

    def transferln(self, amount, account): #recieve from account
        self.deposit(amount)
        account.withdraw(amount)

    @abstractmethod
    def accountDetails(self):
        return "of Customer : " + self.owner.name + " Balance : " + str(self.balance)

    def getBalance(self):
        return self.balance

    def printStatus(self):
        print(self.__str__() + " " + self.accountDetails())

class SavingsAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interestRate = 1.0):
        Account.__init__(self, balance, owner)
        self.interestRate = interestRate

    def __str__(self):
        return "Saving Account"

    def accountDetails(self):
        return Account.accountDetails(self) + " Interest : " + str(self.interestRate)

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds")

    # def addInterest(self):
    #     self.balance += self.balance * self.interestRate

class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, overdraftLimit = -5000.0):
        Account.__init__(self, balance, owner)
        self.overdraftLimit = overdraftLimit

    def __str__(self):
        return "Current Account"

    def accountDetails(self):
        return Account.accountDetails(self) + " Limit : " + str(self.overdraftLimit)

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraftLimit:
            self.balance -= amount
        else:
            print("Insufficient funds")

