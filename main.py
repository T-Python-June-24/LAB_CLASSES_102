from BankAccount import BankAccount

# Create a new bank account with an initial balance
account = BankAccount("Ahad", 6000)

# Deposit money
print("Balance after deposit:", account.deposit(500))

# Withdraw money
print("Balance after withdrawal:", account.withdraw(300))

# Attempt to withdraw more money than available
print("Balance after attempting to withdraw too much:", account.withdraw(6500))

# Check balance
print("Current balance:", account.get_balance())

# Get account holder's name
print("Account holder:", account.get_account_holder())

# Get account number
print("Account number:", account.get_account_number())
