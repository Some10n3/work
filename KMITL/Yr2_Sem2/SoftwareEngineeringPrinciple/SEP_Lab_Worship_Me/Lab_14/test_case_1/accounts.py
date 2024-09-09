import ZODB, ZODB.FileStorage
import persistent
from abc import ABC, abstractmethod
from datetime import datetime
from typing import *

class Customer(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()
    
    def __str__(self):
        return "Customer Name:" + self.name
    
    def addAccount(self, a):
        self.accounts.append(a)
        return a
    
    def account(self, n):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None
    
    def printStatus(self):
        print(self.__str__())
        print()
        for a in self.accounts:
            a.printStatus()

class BankTransaction(persistent.Persistent):
    def __init__(self, amount, balance, timestamp, ttype, direction = None, target = None):
        self.amount = abs(amount)
        self.old_balance = balance
        self.new_balance = self.old_balance + amount
        self.timestamp = timestamp
        self.ttype = ttype

        self.direction = direction
        self.target = target

    def printDetail(self):
        if self.ttype == "transfer":
            print(f"{self.ttype.title()} {self.direction} {self.target}")
        else:
            print(f"{self.ttype.title()}")
        print(f"\tAmount:    {self.amount:.2f}")
        print(f"\tOld Balance:\t{self.old_balance:.2f}")
        print(f"\tNew Balance:\t{self.new_balance:.2f}")
        print(f"\tTime Stamp:\t {str(self.timestamp)}")

class Account(ABC):
    def __init__(self, balance = 0.0, owner = None) -> None:
        self.balance = balance
        self.owner = owner
        self.bankTransaction = []
    
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError('users must define __str__ to use this base class')
    
    @abstractmethod
    def deposit(self, m):
        raise NotImplementedError('users must define deposit to use this base class')
    
    @abstractmethod
    def withdraw(self, m):
        raise NotImplementedError('users must define withdraw to use this base class')
    
    @abstractmethod
    def transfer(self, m, o):
        raise NotImplementedError('users must define transfer to use this base class')
    
    @abstractmethod
    def accountDetail(self):
        raise NotImplementedError('users must define accountDetail to use this base class')
    
    def transferIn(self, m, o):
        if issubclass(o.__class__, Account):
            self.balance += m
    
    def getBalance(self):
        return self.balance
    
    def printStatus(self):
        print(self.__str__())

    def printBankTransaction(self):
        self.printStatus()
        print()
        for t in self.bankTransaction:
            t.printDetail()
            print()

class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, interest = 1.0):
        Account.__init__(self, balance, owner)
        self.interest = interest
    
    def __str__(self):
        return f"Savings Account of Customer: {self.owner.name}  Balance : {self.balance:.2f} Interest : {self.interest:.2f}"
    
    def accountDetail(self):
        return self.__str__()
    
    def deposit(self, m : float):
        if m < 0:
            print("Cannot deposit negative balance")
            return
        transaction = BankTransaction(m, self.balance, datetime.now(), "deposit")
        self.bankTransaction.append(transaction)
        self.balance += m
    
    def getBalance(self):
        return super().getBalance()
    
    def printStatus(self):
        print(self.accountDetail())
    
    def transfer(self, m : float, o : Account):
        if m > self.balance:
            print("Not enough balance for transfer")
            return
        transaction = BankTransaction(
            -1 * m,
            self.balance,
            datetime.now(),
            "transfer",
            "to",
            o.owner.name
        )
        self.bankTransaction.append(transaction)
        self.balance -= m
        o.transferIn(m, self)
    
    def transferIn(self, m, o):
        transaction = BankTransaction(
            m,
            self.balance,
            datetime.now(),
            "transfer",
            "from",
            o.owner.name
        )
        self.bankTransaction.append(transaction)
        super().transferIn(m, o)
    def withdraw(self, m):
        if m > self.balance:
            print("Not enough balance for withdrawal")
        elif m < 0:
            print("Cannot withdraw negative balance")
        else:
            transaction = BankTransaction(-1 * m, self.balance, datetime.now(), "withdraw")
            self.bankTransaction.append(transaction)
            self.balance -= m

    
    def printBankTransaction(self):
        return super().printBankTransaction()

class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance = 0.0, owner = None, limit = -5000):
        Account.__init__(self, balance, owner)
        self.limit = limit
    
    def __str__(self) -> str:
        return f"Current Account of Customer : {self.owner.name}  Balance : {self.balance:.2f} Limit : {self.limit:.2f}"
    
    def accountDetail(self):
        return self.__str__()
    
    def deposit(self, m : float):
        if m < 0:
            print("Cannot deposit negative balance")
            return
        self.balance += m
    
    def getBalance(self):
        return super().getBalance()
    
    def printStatus(self):
        print(self.accountDetail())
    
    def transfer(self, m : float, o : Account):
        if self.balance - self.limit < m:
            print("Not enough balance & limit for transfer")
            return
        transaction = BankTransaction(
            -1 * m,
            self.balance,
            datetime.now(),
            "transfer",
            "to",
            o.owner.name
        )
        self.bankTransaction.append(transaction)
        self.balance -= m
        o.transferIn(m, self)
    
    def transferIn(self, m, o):
        transaction = BankTransaction(
            m,
            self.balance,
            datetime.now(),
            "transfer",
            "from",
            o.owner.name
        )
        self.bankTransaction.append(transaction)
        super().transferIn(m, o)
    
    def withdraw(self, m : float):
        if self.balance - self.limit < m:
            print("Not enough balance & limit to withdraw")
            return
        transaction = BankTransaction(
            -1 * m,
            self.balance,
            datetime.now(),
            "withdraw",
        )
        self.bankTransaction.append(transaction)
        self.balance -= m
    
    def printBankTransaction(self):
        return super().printBankTransaction()
