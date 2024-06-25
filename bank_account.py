class BankAccount:
    # Encapsulation
    __accounts_made = 0

    def __init__(self, account_holder:str, initial_balance:int=0) -> None:
        # Encapsulation
        self.set_account_holder(account_holder)
        self.set_balance(initial_balance)
        # Abstraction
        self.__create_account()
    
    # Encapsulation
    def set_account_holder(self, account_holder:str):
        if isinstance(account_holder, str) and account_holder.isalpha():
            self.__account_holder = account_holder
        else:
            raise Exception("The name has to be alphabetical.")

    # Encapsulation
    def get_account_holder(self):
        return self.__account_holder
    
    # Encapsulation
    def set_balance(self, initial_balance:int):
        if isinstance(initial_balance, int):
            self.__balance = initial_balance
        else:
            raise Exception("The balance must be a number.")
    
    # Encapsulation
    def get_balance(self):
        return self.__balance
    
    # Encapsulation
    def get_account_number(self):
        return self.account_number
        
    # Encapsulation
    def deposit(self, amount:int):
        if isinstance(amount, int) and amount > 0:
            self.__balance += amount
            self.get_balance()
        else:
            raise Exception("You can only deposit amounts greater than 0.")

    # Encapsulation
    def withdraw(self, amount:int):
        if isinstance(amount, int) and amount > 0 and amount <= self.get_balance():
            self.__balance -= amount
            self.get_balance()
        else:
            raise Exception("You can only withdraw an amount less than or equal to your balance.")

    # Abstraction
    def __create_account(self) -> str:
        BankAccount.__accounts_made += 1
        affix = str(self.__accounts_made)
        prefix = ""
        for x in range(10 - len(affix)):
            prefix += "0"
        self.account_number = prefix + affix


# account1 = BankAccount("Mohammed")
# print(account1.get_account_holder())  # Mohammed
# print(account1.get_balance())  # 0
# account1.deposit(500)
# print(account1.get_balance())  # 500
# account1.withdraw(5)
# print(account1.get_balance())  # 495
# print(account1.get_account_number())  # 0000000001

# account2 = BankAccount("Khalid", 5000)
# print(account2.get_account_holder())  # Khalid
# print(account2.get_balance())  # 5000
# print(account2.get_account_number())  # 0000000002

# account3 = BankAccount("Ahmad", 25)
# print(account3.get_account_holder())  # Ahmad
# print(account3.get_balance())  # 25
# account3.withdraw(25)
# print(account3.get_balance())  # 0
# print(account3.get_account_number())  # 0000000003
