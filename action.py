
class Action:

    def __init__(self, name, price, benefit):
        self.name = name
        self.price = price
        self.benefit = benefit

    def __str__(self):
        return str(self.name) + ' ' + str(self.price) + ' ' + str(self.benefit)

    def __repr__(self):
        return str(self.name) + ' ' + str(self.price) + ' ' + str(self.benefit)
