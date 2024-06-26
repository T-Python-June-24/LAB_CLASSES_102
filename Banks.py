from random import randint

class BankAccount:

    def __init__(self, account_holder:str, initial_balance:float = 0, account_number:int = randint(1000000000, 9999999999)) -> None:
        self.account_holder = account_holder
        self.initial_balance = initial_balance
        self.account_number = account_number

    def deposit(self, amount):
        amount = int(input("insert an amount to add to your acount: "))
        self.initial_balance += amount
        print("Your updated Balance is: ", self.initial_balance)

    def withraw(self, amount2):
        amount2 = int(input("insert an amount to withdraw from your acount: "))
        if self.initial_balance >= amount2:
            self.initial_balance -= amount2
            print("Your updated Balance is: ", self.initial_balance)
        else:
            print("There are insufficient funds")
        
    def get_balance(self):
        print(self.initial_balance)

    def get_account_holder(self):
        print(f"The account holder is {self.account_holder}")

    def get_account_number(self):
        print(f"The account number is {self.account_number}")