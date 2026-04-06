# classes6
# Fix the program so it prints `4`.

# hint: Restocking adds to the current count, and selling removes from it.
class Inventory:
    def __init__(self):
        self.count = 5

    def restock(self, amount):
        self.count = amount

    def sell(self, amount):
        if amount > self.count:
            return "not enough"
        self.count = self.count + amount
        return self.count


inventory = Inventory()
inventory.restock(3)
inventory.sell(4)
print(inventory.count)
