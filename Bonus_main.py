from BankAccount import BankAccount
from AccountManager import AccountManager

manager = AccountManager()
filename = 'accounts.pkl'

while True:
    print("--------------MENU---------------")   
    print("1. Add a new bank account")
    print("2. Display all bank accounts")
    print("3. Search for a bank account")
    print("4. Delete a bank account")
    print("5. Save accounts to file")
    print("6. Load accounts from file")
    print("7. Exit")
    print("--------------------------------")    

    choice = input("Choose an option: ")

    if choice == '1':
        holder = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        account = BankAccount(holder, balance)
        manager.add_account(account)
        print(f"Account created with number: {account.get_account_number()}")

    elif choice == '2':
        manager.display_accounts()

    elif choice == '3':
        acc_num = input("Enter account number to search: ")
        account = manager.search_accounts(acc_num)
        if account:
            print(f"Account Number: {account.get_account_number()}, Account Holder: {account.get_account_holder()}, Balance: {account.get_balance()}")
        else:
            print("Account not found.")

    elif choice == '4':
        acc_num = input("Enter account number to delete: ")
        if manager.delete_account(acc_num):
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    elif choice == '5':
        manager.save_to_file(filename)
        print("Accounts saved to file.")

    elif choice == '6':
        manager.load_from_file(filename)
        print("Accounts loaded from file.")

    elif choice == '7':
        break

    else:
        print("Invalid choice. Please try again.")

