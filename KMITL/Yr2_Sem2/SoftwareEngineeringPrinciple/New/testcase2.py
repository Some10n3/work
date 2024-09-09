import ZODB, ZODB.config
import persistent
from abc import ABC, abstractmethod
import BTrees.OOBTree
import transaction
import z2_obj as z_obj

path = "./SoftwareEngineeringPrinciple/New/config.xml"

db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
    for customer in root.customers:
        obj = root.customers[customer]
        obj.printStatus()
        print()
        index = 0
        while obj.getAccounts(index) != None:
            obj.getAccounts(index).printTransactions()
            print()
            index += 1