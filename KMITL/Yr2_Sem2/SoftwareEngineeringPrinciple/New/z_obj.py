import ZODB , ZODB.config , transaction
import account , BTrees.OOBTree , z2_obj
path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers["Dave"] = account.Customer("Dave")
    d = root.customers["Dave"]
    root.customers["Jone"] = account.Customer("Jone")
    j = root.customers["Jone"]

    print("Create Account : Dave")
    b1 = d.addAccount(account.SavingAccount("Dave", 400))
    b2 = j.addAccount(account.CurrentAccount("Jone", 200))
    d.printStatus()
    j.printStatus()

    print("\nDeposit 500 to Jone's account")
    b2.deposit(500)
    b2.printStatus()

    print("\nWithdraw 200 from Dave's account")
    b1.withdraw(200)
    b1.printStatus()

    print("\nTransfer 150 from Jone's account to Dave's account")
    b2.transfer(150, b1)
    b1.printStatus()
    b2.printStatus()

    print("***************************************************")

    for customer in root.customers:
        obj = root.customers[customer]
        obj.printStatus()
        index = 0
        while obj.getAccount(index) != None:
            obj.getAccount(index).printBankTransactions()
            index += 1

    transaction.commit()