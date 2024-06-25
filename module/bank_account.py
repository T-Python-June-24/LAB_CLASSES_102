'''

# LAB_CLASSES_102


Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
- another attribute `account_number` should be set automatically inside the initializer , auto generated bank account number. make sure it is 10 numbers and unique (not generated before for another account)


account_holder
initial_balance
account_number -> make sure it is 10 numbers and unique (not generated before for another account)


2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.
6. A method called `get_account_number` that returns the number of the account holder.

#### Note: OOP principle where applicable such as Encapsulation, Abstraction, etc. & Use modules (& packages if needed) to organize your code. 
'''

    
    
import random as rd

class BankAccount:
    
    generated_account_numbers = set()

    def __init__(self, account_holder: str, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance  # Use balance directly
        self.account_number = self._generate_account_number()



    def _generate_account_number(self):
        while True:
            account_number = "".join([str(rd.randint(0, 9)) for _ in range(10)])    #! 10 digits for account number that i want to generate
            if account_number not in BankAccount.generated_account_numbers:
                BankAccount.generated_account_numbers.add(account_number)   #! if the value is not in the set generated_account_numbers then you can add it to the set and account_number
                return account_number
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:  
            print("Error: Insufficient funds.")
            return self.balance
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number
    
    
if __name__ == "__main__":
    print("This was Imported from BankAccount class.")