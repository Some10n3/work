import ZODB , ZODB.config , transaction
import account , BTrees.OOBTree

path = "./config.xml"
db = ZODB.config.databaseFromURL(path)
connection = db.open()
root = connection.root()

root.customers = BTrees.OOBTree.BTree()