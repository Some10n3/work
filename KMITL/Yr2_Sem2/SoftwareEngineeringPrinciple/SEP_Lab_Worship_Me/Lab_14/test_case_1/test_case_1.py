from multiprocessing import connection
import ZODB, ZODB.FileStorage
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction

from accounts import *

storage = ZODB.FileStorage.FileStorage("mydata.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers['Jone'] = Customer("Jone")
    j = root.customers["Jone"]
    j.printStatus()

    print()
    a = j.addAccount(SavingAccount(400, j))
    b = j.addAccount(CurrentAccount(200, j))
    a.printStatus()
    b.printStatus()
    j.printStatus()

    print()
    b.withdraw(100)
    j.printStatus()

    a.transfer(150, b)
    j.printStatus()

    print()
    a.deposit(500)
    j.printStatus()

    transaction.commit()