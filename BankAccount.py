'''
Create a Python class called `BankAccount` that simulates a simple bank account. 
The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`),
 setting the balance to zero if the initial balance is not provided.
- another attribute `account_number` should be set automatically inside the initializer , 
auto generated bank account number. make sure it is 10 numbers and unique (not generated before for another account)

2. A method called `deposit` that accepts an amount and adds it to the account balance, 
and then returns the updated balance.

3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, 
returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds,
 it should print an error message and leave the balance unchanged.

4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.
6. A method called `get_account_number` that returns the number of the account holder.

#### Note: OOP principle where applicable such as Encapsulation, Abstraction, etc.
 & Use modules (& packages if needed) to organize your code. 

'''
import random


class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float ) -> None:
     self.__account_holder=account_holder
     self.__account_number=self.generate_account_number()
     if initial_balance==None:
      self.initial_balance=0
     else:
      self.initial_balance=initial_balance
     
    def generate_account_number(self):
      account_number= ''.join(str(random.sample(range(10), 1)[0]) for _ in range(10))
      
      return account_number

    def deposit(self,amount:float):
     
      self.initial_balance+=amount
      return f"updated balnce : {self.initial_balance}"
    
    def withdraw(self,amount:float):
        if amount<0:
         print("the amount must be postive to be discounted from your balance ")
        else:
         if amount<=self.initial_balance:
          self.initial_balance-=amount
          return self.initial_balance 
         else:
          print(f"Error: Insufficient funds. Your current balance is {self.initial_balance}$, but you tried to withdraw {amount}$.")
        return self.initial_balance   

    def set_account_holder(self,account_holder): 
        
       return  self.__account_holder==account_holder
    def get_balance(self):
      return self.initial_balance
    def get_account_holder(self):
      return self.__account_holder
    def set_account_number (self,account):
      return self.__account_number==self.generate_account_number()
    def get_account_number(self):
      return self.__account_number


    def display(self):
      return f"Account holder: {self.get_account_holder()} Acoount number : {self.get_account_number() } Balance : {self.get_balance()}"