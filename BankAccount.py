import random

class BankAccount:
    
    account_numbers = set()

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.unique_account_number()

    def unique_account_number(self):
        while True:
            account_number = str(random.randint(1000000000, 9999999999))
            if account_number not in BankAccount.account_numbers:
                BankAccount.account_numbers.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number
    

account1 = BankAccount("Alice", 1000)

print(f"Balance after deposit: {account1.deposit(500)}") #1500
print(f"Balance after withdrawal: {account1.withdraw(200)}")  #1300
#withdraw more than the balance
print(f"Balance after withdrawal: {account1.withdraw(1500)}")  # prints: Insufficient funds, Balance: 1300
# Get the current balance
print(f"Current Balance: {account1.get_balance()}")  #1300

print(f"Account Holder: {account1.get_account_holder()}")

print(f"Account Number: {account1.get_account_number()}")

