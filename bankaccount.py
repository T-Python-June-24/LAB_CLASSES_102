import random
import math
class BankAccount:
    def __init__(self,account_holder:str,intial_blance:int=0) -> None:
        self.__account_holder=account_holder
        self.__intial_blance=intial_blance
        self.__account_number= round(random.random()*10000000000)
    
    def deposit(self,amount):
        if isinstance(amount,int):
            self.__intial_blance+=amount
            print("Done succsfully")
        else:
            print("please try to enter a number")
    def withDraw(self,amount):
        if  not amount > self.__intial_blance:
            self.__intial_blance-=amount
        else:
            print(f"error your blance is {self.__intial_blance}")
    def get_blance(self):
        return self.__intial_blance
    def get_account_holder(self):
        return self.__account_holder
    def get_account_number(self):
        return self.__account_number