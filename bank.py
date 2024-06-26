import random

class BankAccount:

  # Checking if the account number exist
  account_number_exist = set()

  # constructor
  def __init__(self, holder_name:str, initial_balance:int=0) -> None:
        #addtributes/ properties
        self.holder_name =holder_name
        self.__balance = initial_balance
        self.account_number = self.generate_number


  def generate_number(self):
    while True:
      # generating random 10 digit number
      account_number = str(random.randint(1000000000, 9999999999)) 
      if account_number not in self.account_number_exist:
        self.account_number_exist.add(account_number)
        return account_number
      
  # setter
  def set_balance(self, balance):
     self.__balance

  
  # definig get balance method
  def get_balance(self):
        return self.__balance
      
  ## definig class methods

  # definig deposite function 
  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
    return self.__balance
  
  # definig withdraw method
  def withdraw(self, amount):
    if amount > self.__balance:
      print("Insufficient funds.")
    else:
      self.__balance -= amount
    return self.__balance

  # defining get account hloder method 
  def get_account_holder(self):
    return self.holder_name
  
  # definig get account number method 
  def get_account_number(self):
    return self.account_number
  
  
