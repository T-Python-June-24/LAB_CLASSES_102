from bank_account import BankAccount

account = BankAccount("Ahmed", 1000)
print(f"Account Number: {account.get_account_number()}")
print(f"Account Holder: {account.get_account_holder()}")
print(f"Balance: ${account.get_balance():.2f}")
