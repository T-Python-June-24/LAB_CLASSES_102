from bank_account import BankAccount
import pickle
import os


class AccountManager:
    def __init__(self, filename: str = "accounts.pkl"):
        # Initialize AccountManager with a filename for storing accounts
        self.__filename: str = filename
        self.__accounts: list[BankAccount] = self.__load_from_file()

    def add_account(self, bank_account: BankAccount) -> None:
        # Add a new bank account to the list
        if not isinstance(bank_account, BankAccount):
            raise TypeError("Only BankAccount objects can be added")
        self.__accounts.append(bank_account)
        print(f"🎉 Account {bank_account.get_account_number()} added successfully! 🎉")
        self.__save_to_file()

    def display_accounts(self) -> None:
        # Display all accounts in the list
        print("📊 Account Summary 📊")
        if not self.__accounts:
            print("🚫 No accounts found! 🚫")
        else:
            for account in self.__accounts:
                print(f"🔢 Account Number: {account.get_account_number()}, 👤 Account Holder: {account.get_account_holder()}, 💰 Balance: ${account.get_balance():.2f}")
    
    def search_accounts(self, account_number: str) -> str:
        # Search for an account by account number
        if not isinstance(account_number, str) or len(account_number) != 10:
            raise ValueError("Account number must be a 10-character string")
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return f"✅ Account {account_number} found!\n👤 Account Holder: {account.get_account_holder()}\n💰 Balance: ${account.get_balance():.2f}"
        return f"❌ Account {account_number} not found. Please check the number and try again."
    
    def delete_account(self, account_number: str) -> str:
        # Delete an account by account number
        if not isinstance(account_number, str) or len(account_number) != 10:
            raise ValueError("Account number must be a 10-character string")
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                self.__accounts.remove(account)
                self.__save_to_file()
                return f"🗑️ Account {account_number} deleted successfully!"
        return f"❌ Account {account_number} not found. Unable to delete."
    
    def update_account(self, account_number:str, amount:float)-> str:
        # Update an account's balance
        if not isinstance(account_number, str) or len(account_number) != 10:
            raise ValueError("Account number must be a 10-character string")
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.set_balance(account.get_balance() + amount)
                return f"🔄 Account {account_number} updated successfully!"
        return f"❌ Account {account_number} not found. Unable to update."

    def __save_to_file(self) -> None:
        # Save accounts to a file using pickle
        try:
            with open(self.__filename, "wb") as file:
                pickle.dump(self.__accounts, file)
            print(f"💾 Accounts saved successfully to {self.__filename}!")
        except (OSError, pickle.PickleError) as e:
            print(f"❌ Error saving accounts to file: {e}")
    
    def __load_from_file(self) -> list[BankAccount]:
        # Load accounts from a file using pickle
        if os.path.exists(self.__filename):
            try:
                with open(self.__filename, "rb") as file:
                    accounts: list[BankAccount] = pickle.load(file)
                print(f"📂 Accounts loaded successfully from {self.__filename}!")
                return accounts
            except (OSError, pickle.PickleError) as e:
                print(f"❌ Error loading accounts from file: {e}")
                return []
        else:
            print(f"📂 No existing accounts file found. Starting with an empty account list.")
            return []

    def __str__(self) -> str:
        # String representation of AccountManager
        return f"AccountManager managing {len(self.__accounts)} accounts."

    def get_accounts(self) -> list[BankAccount]:
        # Get the list of accounts
        return self.__accounts
