from BankAccount import BankAccount
import pickle

class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, bank_account):
        self.accounts.append(bank_account)

    def display_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.get_account_number()}, Account Holder: {account.get_account_holder()}, Balance: {account.get_balance()}")

    def search_accounts(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def delete_account(self, account_number):
        account = self.search_accounts(account_number)
        if account:
            self.accounts.remove(account)
            BankAccount.existing_acc_nums.remove(account_number)
            return True
        return False

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.accounts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.accounts = pickle.load(file)
                # Update existing_acc_nums 
                BankAccount.existing_acc_nums = {acc.get_account_number() for acc in self.accounts}
        except FileNotFoundError:
            print(f"No file found with the name {filename}.")
