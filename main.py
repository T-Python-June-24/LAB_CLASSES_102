
from account import BankAccount,AccountManager
accountManager = AccountManager()
while True:
    answer = input("Enter your choice:\nA to add a bank account.\nD to display bank accounts.\nR to remove a bank account.\nS to search for a bank account.\nE to exit.\n")
    if answer.upper() == "EXIT":
        print("Thank you for using our bank system, please come back again soon.")
        break
    elif answer.upper() == "A": 
        holder_name = input("Enter account holder name: ")
        account = BankAccount(holder_name)
        accountManager.add_account(account)
        accountManager.save_to_file("bankAccountsFile.pkl")
    elif answer.upper() == "D":
        accountManager.load_from_file("bankAccountsFile.pkl")
        accountManager.display_accounts()
    elif answer.upper() == "R":
        account = input("Enter the bank account number to be deleted: ")
        accountManager.delete_account(account)
        accountManager.save_to_file("bankAccountsFile.pkl")
        input("Press any kkey to continue..")
    elif answer.upper() == "S":
        account = input("Enetr the account number you're searching for: ")
        found, account, message = accountManager.search_accounts(account)
        print(message)
        input("Press any kkey to continue..")
