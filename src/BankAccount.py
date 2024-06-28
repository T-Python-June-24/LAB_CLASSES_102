from rich.console import Console
from rich.table import Table
import random
import pickle

class BankAccount:
    
    def __init__(self,account_holder:str,balance:float=0.0) -> None:
        
        self.__account_holder = account_holder
        self.__account_number = self.__generateUniqueId()
        self.__balance = 0
        self.deposit(balance)

    def __isUnique(self,id):
        """
        Checks if the given id number is unique.
        This implementation simply checks against a list of used account numbers,
        but in a real-world scenario, you would likely need to check against a
        database of existing account numbers.
        """
        used_account_numbers = []
        if id in used_account_numbers:
            return False
        else:
            used_account_numbers.append(id)
            return True

    def __generateUniqueId(self):

        """
        Generates a unique 10-digit bank account number.
        """
        # Generate a random 10-digit number
        id = ''.join(str(random.randint(0, 9)) for i in range(10))
        # Check if the generated number is unique
        while True:
            if self.__isUnique(id):
                return id
            else:
                id = ''.join(str(random.randint(0, 9)) for i in range(10))

    def get_balance(self):

        return self.__balance
    
    def get_account_number(self):

        return self.__account_number

    def get_account_holder(self):

        return self.__account_holder

    def set_account_holder(self,new_holder):
        self.__account_holder = new_holder
        return True
    
    def deposit(self,amount):

        if not isinstance(amount, float) and amount < 0:
            raise Exception("The amount should be more than 0 otherwise not alloweded ")
        else:
            self.__balance += amount
            return True

    def withdraw(self,amount):
        if not isinstance(amount, float):
            raise Exception("Only provide valid numbers integer or float.")
        
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            raise Exception("Insufficient funds.")

class AccountManager():

    __file_name = "accounts.pickle"
    __number_of_accounts = 0

    def __init__(self):
        self.__accounts = {}
        AccountManager.__number_of_accounts += 1
        self.__load_from_file(AccountManager.__file_name)

    def get_number_of_accounts(self):
        return self.__number_of_accounts

    def add_account(self, bank_account: BankAccount):
        if not isinstance(bank_account,BankAccount):
            raise Exception("Only bankaccount objects are alloweded to add ")
        else:
            self.__accounts[bank_account.get_account_number()] = bank_account
            self.__save_to_file(AccountManager.__file_name)

    def display_accounts(self):
        if not self.__accounts: 
            raise Exception("There is no accounts in our database please add at least one account to display")
        else:
            
                console=Console()
                table=Table(title="Accounts records",border_style="dark_magenta",header_style="bold dark_magenta")
                table.add_column("Account Holder",justify="center",style="dark_blue")
                table.add_column("Account Number",justify="center",style="dark_blue",no_wrap=True)
                table.add_column("Account Balance",justify="center",style="dark_blue",no_wrap=True)
                for account in self.__accounts.values():
                    table.add_row(account.get_account_holder(),account.get_account_number(),str(account.get_balance()))
                    table.add_row("","")
                console.print(table)

    def search_account(self, account_number):
        if account_number not in self.__accounts:
            raise Exception("Account not in our database")
        else:
            return self.__accounts[account_number]

    def delete_account(self, account_number):
        account = self.search_account(account_number)
        if account:
            del self.__accounts[account_number]
            print(f"Account {account_number} deleted.")
            self.__save_to_file(AccountManager.__file_name)


    def update_account(self, account_number, new_holder):
        if account_number in self.__accounts:
            if new_holder:  
                name_updated = self.__accounts[account_number].set_account_holder(new_holder)
                self.__save_to_file(AccountManager.__file_name) # need it every time to save changes 
                return name_updated
        else:
            raise Exception("Account not found")
        
    def __save_to_file(self, filename: str):
        with open(filename, "wb") as file:
            pickle.dump(self.__accounts, file)

    def __load_from_file(self, filename: str):
        try:
            with open(filename, "rb") as file:
                self.__accounts = pickle.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def deposit(self,account,amount):

        if not isinstance(amount, float) or amount <= 0:
            raise Exception("The amount should be more than 0 otherwise not alloweded ")
        
        else:
            account.deposit(amount)
            self.__save_to_file(AccountManager.__file_name)

    def withdraw(self,account,amount):
        if not isinstance(amount, float) or amount <= 0:
            raise Exception("Only provide valid numbers integer or float.")
        else:
            account.withdraw(amount)
            self.__save_to_file(AccountManager.__file_name)

