
class Transaction:
    def __init__(self, id, date, catagory, cost, notation):
        self.id = id
        self.date = date
        self.cost = cost
        self.notation = notation
        self.catagory = catagory
    
    def getId(self):
        return self.Id
    
    def getDate(self):
        return self.date
    
    def getCost(self):
        return self.cost
    
    def getNote(self):
        return self.notation
    
    def getCat(self):
        return self.catagory

    def print(self):
        print("Id: {}, Date: {}, Cat: {} Cost: {}, Notation: {}".format(self.id, self.date, self.catagory, self.cost, self.notation))


class TransactionManager:
    def __init__(self):
        self.TransactionList = []
        self.totalSpend = 0

    def add(self, Transaction):
        self.TransactionList.append(Transaction)

    def print(self):
        for transaction in self.TransactionList:
            transaction.print()

    def totalSpending(self):
        for transaction in self.TransactionList:
            self.totalSpend += transaction.getCost() 
        print(self.totalSpend)
    
    def totalSpendingByCat(self, cat):
        spending = 0
        for transaction in self.TransactionList:
            if( transaction.getCat() == cat):
                spending += transaction.getCost()
        print(spending)



One = Transaction( 1, 20, 1, 1000, "Duo")
Two = Transaction( 2, 20, 3, 3000, "Belasting")
Three = Transaction( 3, 20, 1, 1000, "swag")
Four = Transaction( 4, 20, 3, 3000, "swag")
Five = Transaction( 5, 20, 1, 1000, "swag")


Manager = TransactionManager()
Manager.add(One)
Manager.add(Two)
Manager.add(Three)
Manager.add(Four)
Manager.add(Five)

Manager.print()
Manager.totalSpending()
Manager.totalSpendingByCat(3)