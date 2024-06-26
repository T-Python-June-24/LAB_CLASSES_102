



from bank_accounts import BankAccount

def main():


    account1 = BankAccount("Bob", 500)
    account2 = BankAccount("Del", 333333)

    #1
    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Account Number: {account1.get_account_number()}")
    print(f"Initial Balance: {account1.get_balance()}")
    account1.deposit(200)
    print(f"Balance after deposit: {account1.get_balance()}")
    account1.withdraw(750)
    print(f"Balance after withdrawal: {account1.get_balance()}")

    #2
    print(f"\nAccount Holder: {account2.get_account_holder()}")
    print(f"Account Number: {account2.get_account_number()}")
    print(f"Initial Balance: {account2.get_balance()}")
    account2.deposit(300)
    print(f"Balance after deposit: {account2.get_balance()}")
    account2.withdraw(900)  
    print(f"Balance after attempted withdrawal: {account2.get_balance()}")

if __name__ == "__main__":
    main()
