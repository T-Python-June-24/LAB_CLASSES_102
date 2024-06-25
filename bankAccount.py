import random
import string
class BankAccount:
    initialBalance = 0
    accountNumber = 0

    def __init__ (self, account_holder:str , initial_balance:int ):
        self.account_holder = account_holder
        self.initialBalance = initial_balance 
        self.accountNumber = ''.join(random.choices( string.digits, k=10))

    def info(self):
        return f"Name of account {self.account_holder} balance: {self.initialBalance} account Number: {self.accountNumber}"

    def deposit (self, depositMoney:int):
        self.initialBalance = self.initialBalance + depositMoney
        return self.initialBalance

    def withdraw(self, withdrawMoney:int):
        if withdrawMoney > self.initialBalance:
            raise Exception("Sorry, You are broke go to work!")
        self.initialBalance = self.initialBalance - withdrawMoney
        return self.initialBalance

    def get_balance(self):
        return f"Your Balance is :{self.initialBalance}"

    def get_account_holder(self):
        return f"Account holder name is : {self.account_holder}"
    def get_account_number(self):
        return f"Account number is :{self.accountNumber}"
