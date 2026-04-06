# classes2
# Fix the program so it prints `15`.

# hint: Adding money should increase the balance, and spending should lower it.
class Wallet:
    def __init__(self):
        self.money = 10

    def add(self, amount):
        self.money = self.money + amount

    def spend(self, amount):
        self.money = self.money - amount


wallet = Wallet()
wallet.add(7)
wallet.spend(2)
print(wallet.money)
