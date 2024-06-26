from BankAccount import BankAccount



account=BankAccount("naif", 10)
account1=BankAccount("ahmad", 200)
account2=BankAccount("salem", 1000)

print(account.deposit(40))
print("-"*5)
print(account1.withdraw(20))
print("-"*5)
print(account1.withdraw(300))
print("-"*5)
print(account2.get_balance())
print("-"*5)
print(account2.get_account_holder())
print("-"*5)
print(account2.get_account_number())

