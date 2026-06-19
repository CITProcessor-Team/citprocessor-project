class BankAccount:
    def __init__(self, holder_name):
        self.holder = holder_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Create two accounts
account1 = BankAccount("Ravi")
account2 = BankAccount("Priya")

# Transactions for Ravi
account1.deposit(5000)
account1.withdraw(1500)
account1.withdraw(4000)  # Overdraft attempt

# Transactions for Priya
account2.deposit(3000)
account2.deposit(1000)
account2.withdraw(2000)

# Print balances
print("Ravi's Balance:", account1.get_balance())
print("Priya's Balance:", account2.get_balance())
