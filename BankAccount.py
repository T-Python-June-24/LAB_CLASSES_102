import random

class BankAccount:
    account_num = set()

    def __init__(self, account_holder:int, initial_balance:int=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        while True:
            account_number = random.randint(1000000000, 9999999999)  # 10-digit number
            if account_number not in BankAccount.account_num:
                BankAccount.account_num.add(account_number)
                return account_number

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Deposit amount must be greater than zero.")
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient funds.")
                return self.balance
        else:
            print("Withdrawal amount must be greater than zero.")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number
    
