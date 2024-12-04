class BankAccount :
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance :
            self.balance -= amount
        else:
            print("Insufficient balance.")
    def check_balance(self):
        return self.balance
    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance : Rs{self.balance:.2f})"
    def __repr__(self):
        return self.__str__()
account = BankAccount("999038", "Aditya Bhatia", 10000)
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())
print(account)