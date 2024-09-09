import persistent
import datetime
from abc import ABC, abstractmethod
class Customer(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self):
        return "Customer name : " + self.name
    
    def setName(self, name):
        self.name = name

    def addAccount(self, account):
        self.accounts.append(account)
        return account

    def getAccount(self,name):
        if 0 <= name < len(self.accounts):
            return self.accounts[name]
        return None

    def printStatus(self):
        print(self.__str__())
        for a in self.accounts:
            print("", end = "   ")
            a.printStatus()


class Account(ABC):
    def __init__(self, owner = "", balance = 0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = persistent.list.PersistentList()
        self.bankTransactions = persistent.list.PersistentList()
        
    @abstractmethod
    def __str__(self):
        raise NotImplementedError('user must define __str__ to use this base class')
    
    def accountDetails(self):
        return self.__str__()
    
    def deposit(self, amount,type = "Deposit"):
        self.balance += amount
        self.transactions.append(amount)
        self.bankTransactions.append(BankTransaction(amount, self.balance - amount, self.balance , type))
    
    def withdraw(self, amount, type = "Withdraw"):
        self.balance -= amount
        self.transactions.append(-amount)
        self.bankTransactions.append(BankTransaction(amount, self.balance + amount, self.balance , type))

    def getBalance(self):
        return self.balance

    def printStatus(self):
        print(self.accountDetails())
        # for t in self.transactions:
        #     print("", end = "   ")
        #     print(t)
    
    def printTransactions(self):
        for t in self.transactions:
            print(t)

    def printBankTransactions(self):
        for t in self.bankTransactions:
            print(t)
        
    def transfer(self, amount, toAccount):
        self.withdraw(amount , "Transfer to " + toAccount.getName())
        toAccount.deposit(amount , "Transfer from " + self.getName())
        self.transactions.append("Transfer : " + str(amount) + " to " + toAccount.getName())
    
    def transferIn(self, amount, fromAccount):
        self.deposit(amount , "Transfer from " + fromAccount.getName())
        fromAccount.withdraw(amount , "Transfer to " + self.getName())
        self.transactions.append("Transfer : " + str(amount) + " from " + fromAccount.getName())

    def printBankTranasactions(self):
        for t in self.bankTransactions:
            print(t)
    
    def getName(self):
        return self.owner

class SavingAccount(Account):
    def __init__(self, owner = "", balance = 0.0, interestRate = 1.0):
        super().__init__(owner, balance)
        self.interestRate = interestRate
    
    def __str__(self):
        return "Saving Account of Customer Name : "  + self.owner + "  Balance : " + str(self.balance) + "   Interest : " + str(self.interestRate)

    def addInterest(self):
        self.balance += self.balance * self.interestRate / 100


class CurrentAccount(Account):
    def __init__(self, owner = "", balance = 0.0, creditLimit = -5000.0):
        super().__init__(owner, balance)
        self.creditLimit = creditLimit
    
    def __str__(self):
        return "Current Account of Customer Name : " + self.owner + " Balance : " + str(self.balance) + " Limit : " + str(self.creditLimit)

    def withdraw(self, amount, type = "Withdraw"):
        if self.creditLimit <= amount and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(-amount)
            self.bankTransactions.append(BankTransaction(amount, self.balance + amount, self.balance , type))
        else:
            print("Insufficient funds")

class BankTransaction(persistent.Persistent):
    def __init__(self, amount , old_bal , new_bal , type):
        self.amount = amount
        self.old_bal = old_bal
        self.new_bal = new_bal
        self.time = datetime.datetime.now()
        self.ttype = type
    
    def __str__(self):
        return self.ttype + "\nAmount : " + str(self.amount) + "\nOld Balance : " + str(self.old_bal) + "\nNew Balance : " + str(self.new_bal) + "\nTime : " + str(self.time) + "\n"