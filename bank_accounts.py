# Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

# 1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
# - another attribute `account_number` should be set automatically inside the initializer , auto generated bank account number. make sure it is 10 numbers and unique (not generated before for another account)

# 2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
# 3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
# 4. A method called `get_balance` that returns the current account balance.
# 5. A method called `get_account_holder` that returns the name of the account holder.
# 6. A method called `get_account_number` that returns the number of the account holder.

# #### Note: OOP principle where applicable such as Encapsulation, Abstraction, etc. & Use modules (& packages if needed) to organize your code. 



import random



class BankAccount:
    account_numbers = set()


    def __init__(self, account_holder, initial_balance= 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = "".join(random.choices('0123456789', k=10))




    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive")



    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                print("Error: Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")



    def get_balance(self):
        return self.balance



    def get_account_holder(self):
        return self.account_holder



    def get_account_number(self):
        return self.account_number
