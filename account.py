import pickle
class BankAccount:
    def __init__(self,account_holder:str, initial_balance:float = 0.00)-> None:
        self.account_holder = account_holder
        self.initial_balance = initial_balance
        self.account_number = generator.getNextNumber()
    
    def deposit(self,amount:float):
        balance = self.initial_balance
        self.initial_balance += amount
        return balance
    
    def withdraw(self,amount:float):
        balance = self.initial_balance
        if balance >= amount:
            self.initial_balance -= amount
        else:
            print("Insufficient fund!")
        return balance

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.account_holder

    def get_account_number(self):
        return self.account_number
  
class AccountManager:
    def __init__(self) :
        self.bankAccounts = []  
    
    def add_account(self, bank_account: BankAccount):
        if isinstance(bank_account,BankAccount):
            self.bankAccounts.append(bank_account)
            print("Account has been added successfully.")
            input("Press any key to continue..")
        else: raise TypeError("Expected a bank account")
    
    def display_accounts(self):
        print("The following are all bank accounts added: ")
        for account in self.bankAccounts:
            print(f"Name: {account.account_holder} - Account Number: {account.account_number} - Balance: ${account.initial_balance}")
        input("Press any key to continue..")


    def search_accounts(self, account_number):
        found = False
        for account in self.bankAccounts:
            if account.account_number == int(account_number):
                found = True
                break
        if found:
            message = f"The account number: {account.account_number} belongs to: {account.account_holder}"
        else:
            message = f"This account number does not exist in the system!"
        return found, account,message

    def delete_account(self, account_number):
        found, account,message = self.search_accounts(account_number)
        if found:
            self.bankAccounts.remove(account)
            print(f"The account number: {account_number} has been deleted successfully.")
            input("Press any key to continue..")

    def save_to_file(self, filename: str):
        #Open a file and use dump() 
        with open(filename, 'wb') as bankAccountsFile: 
            #A new file will be created 
            pickle.dump(self.bankAccounts, bankAccountsFile)  

    def load_from_file(self, filename: str):
        #Open the file in binary mode 
        with open(filename, 'rb') as bankAccountsFile: 
            # Call load method to deserialze 
            self.bankAccounts = pickle.load(bankAccountsFile)




class accounNumberGenerator:
    def __init__(self,start = 1000000000) -> None:
        self.current = start
    
    def getNextNumber(self):
        accountNumber = self.current
        self.current += 1
        return accountNumber
generator = accounNumberGenerator()


