import random

class BankAccount:
    

    def __init__(self,account_holder:str,balance:float) -> None:
        

        self.__account_holder = account_holder
        self.__account_number = self.__generateUniqueId()
        self.__balance = balance or 0 

        # self.__account_holder = {}
        # self.__account_holder[self.__account_number] = {"name":name, "balance": balance} #setting the balance to zero if the initial balance is not provided.
        
    # def deposit

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
        id = ''.join(str(random.randint(0, 9)) for _ in range(10))
        # Check if the generated number is unique
        while True:
            if self.__isUnique(id):
                return id
            else:
                id = ''.join(str(random.randint(0, 9)) for _ in range(10))

    def get_balance(self):

        return self.__balance

    def get_account_number(self):

        return self.__account_number

    def get_account_holder(self):

        return self.__account_holder
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient funds.")
            return self.__balance
    

