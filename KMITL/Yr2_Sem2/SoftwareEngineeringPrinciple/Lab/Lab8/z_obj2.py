import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import datetime

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
        self.transactions = persistent.list.PersistentList()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def deposit(self, amount):
        self.balance += amount        
        self.transactions.append(Transaction(amount, self, "Deposit"))

    @abstractmethod
    def withdraw(self, amount):
        pass

    def transfer(self, amount, account):
        self.withdraw(amount)
        account.deposit(amount)
        self.transactions.append(Transaction(amount, self, "Transfer"))

    def transferln(self, amount, account): #recieve from account
        self.deposit(amount)
        account.withdraw(amount)
        self.transactions.append(Transaction(amount, self, "Transfer"))

    @abstractmethod
    def accountDetails(self):
        return "of Customer : " + self.owner.name + " Balance : " + str(self.balance)

    def getBalance(self):
        return self.balance

    def printStatus(self):
        print(self.__str__() + " " + self.accountDetails())

    @abstractmethod
    def printTransactions(self):
        pass

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
        self.transactions.append(Transaction(amount, self, "Withdraw"))

    def printTransactions(self):
        for transaction in self.transactions:
            print(transaction)

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
        self.transactions.append(Transaction(amount, self, "Withdraw"))

    def printTransactions(self):
        for transaction in self.transactions:
            print(transaction)

class Transaction(persistent.Persistent):
    def __init__(self, amount, account, ttype):
        self.amount = amount
        self.ttype = ttype#if ttype == "Deposit" or ttype == "Withdraw" or ttype == "Transfer": ttype else: "Unknown"
        self.old_balance = account.getBalance()
        if self.ttype == "Deposit":
            self.new_balance = self.old_balance + self.amount
        elif self.ttype == "Withdraw":
            self.new_balance = self.old_balance - self.amount
        elif self.ttype == "Transfer":
            self.new_balance = self.old_balance - self.amount
        self.timestamp = datetime.datetime.now()

    def printDetail(self):
        return self.ttype + "\n    Amount :     " + str(self.amount) + "\n    Old Balance :     " + str(self.old_balance) + "\n    New Balance :     " + str(self.new_balance) + "\n    Timestamp :     " + str(self.timestamp)

    def __str__(self):
        return self.printDetail()

    def getAmount(self):
        return self.amount

    def getAccount(self):
        return self.account

    