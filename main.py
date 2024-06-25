from bank_manager import AccountManager
from bank_account import BankAccount
manager = AccountManager()

while True:
    try:
        print("🏦 Bank Account Management System 🏦")
        print("1. 📝 Add Account")
        print("2. 📊 Display Accounts")
        print("3. 🔍 Search Account")
        print("4. 🗑️ Delete Account")
        print("5. 🔄 Update Account")
        print("6. 🚪 Exit")
        choice = input("Enter your choice: ")
        if choice == "6":
            print("Thank you for using our service. Goodbye! 👋")
            break
        elif choice == "1":
            account_holder: str = input("Enter the account holder's name: ")
            if not account_holder:
                raise ValueError("Account holder's name cannot be empty")
            account_balance: str = input("Enter the initial account balance: $")
            
            try:
                balance = float(account_balance)
                if balance < 0:
                    raise ValueError("Account balance must be non-negative")
                
                account = BankAccount(account_holder, balance)
                manager.add_account(account)
            except ValueError as e:
                raise ValueError(f"Invalid input: {e}")
        elif choice == "2":
            manager.display_accounts()
            
        elif choice == "3":
            account_number: str = input("Enter the account number to search: ")
            if len(account_number) != 10:
                raise ValueError("Account number must be 10 characters long")
            result = manager.search_accounts(account_number)
            print(result)
            
        elif choice == "4":
            account_number: str = input("Enter the account number to delete: ")
            if len(account_number) != 10:
                raise ValueError("Account number must be 10 characters long")
            result = manager.delete_account(account_number)
            print(result)
            
        elif choice == "5":
            account_number: str = input("Enter the account number to update: ")
            if len(account_number) != 10:
                raise ValueError("Account number must be 10 characters long")
            amount_str: str = input("Enter the amount to deposit or withdraw: $")
            try:
                amount = float(amount_str)
            except ValueError:
                raise ValueError("Invalid amount. Please enter a valid number.")
            result = manager.update_account(account_number, amount)
            print(result)
        else:
            raise ValueError("Invalid choice. Please try again.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        print("\n" + "="*40 + "\n")
