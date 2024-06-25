import uuid

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        # Initialize account with holder name and balance
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__account_number = self.__generate_account_number()

    def __generate_account_number(self):
        # Generate a unique 10-character account number
        return str(uuid.uuid4())[:10]

    def deposit(self, amount):
        # Add money to the account
        if amount <= 0:
            raise ValueError("💸 Please enter a positive amount to deposit.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        # Take money from the account
        if amount <= 0:
            raise ValueError("💸 Please enter a positive amount to withdraw.")
        if amount > self.__balance:
            raise ValueError("❌ Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_account_holder(self):
        # Return the name of the account holder
        return self.__account_holder

    def get_account_number(self):
        # Return the account number
        return self.__account_number
    
    def get_balance(self):
        # Return the current balance
        return self.__balance

    def __str__(self):
        # String representation of the account
        return f"🏦 Account Number: {self.__account_number}, 👤 Holder: {self.__account_holder}, 💰 Balance: ${self.__balance:.2f}"

    def __repr__(self):
        # Representation of the account for debugging
        return f"BankAccount(account_holder='👤 {self.__account_holder}', initial_balance=💰 ${self.__balance:.2f})"

