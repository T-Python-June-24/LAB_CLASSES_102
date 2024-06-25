from BankAccount import BankAccount 

account_1=BankAccount("Nuha Mohammed ",12300)
account_2=BankAccount("Ali Mohammed ",26900)
account_3=BankAccount("Alya Saleh",224255)

#cheack conditions of withdraw func
print("-----------------")
print(account_2.withdraw(-700))
print(account_2.withdraw(700))
print(account_2.withdraw(700000))
print("-----------------")

print(account_3.deposit(2000))
print("-----------------")
print(account_1.get_account_number())
print("-----------------")

print(account_1.display())

    

        