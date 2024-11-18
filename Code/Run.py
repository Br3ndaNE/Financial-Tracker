
class Transaction:
    def __init__(self, id, cost, notation):
        self.id = id
        self.cost = cost
        self.notation = notation
    
    def print(self):
        print("Id: {}, Cost: {}, Notation: {}".format(self.id, self.cost, self.notation))

Transaction one(1,1000, "Swag")
one.print()
