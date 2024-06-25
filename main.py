from bankAccount import *

account1 = BankAccount("Ali", 15)
account2 = BankAccount("khalid",20)
print(account1.info())
print(account2.info())
print(account1.deposit(15))
print(account1.withdraw(10))
print(account1.info())
print(account1.get_balance())
print(account1.get_account_holder())
print(account1.get_account_number())