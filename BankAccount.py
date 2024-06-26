import random

class BankAccount:
    existing_acc_nums = set()

    def __init__(self, account_holder, initial_balance=0):
        self.acc_holder = account_holder
        self.balance = initial_balance
        self.acc_num = self.generate_acc_num()

    def generate_acc_num(self):
        while True:
            acc_num = str(random.randint(1000000000, 9999999999))
            if acc_num not in BankAccount.existing_acc_nums:
                BankAccount.existing_acc_nums.add(acc_num)
                return acc_num

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds.")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.acc_holder

    def get_account_number(self):
        return self.acc_num
