from BankAccount import BankAccount


if __name__ == "__main__":
    accont1 = BankAccount("osama", 1000)

    print(accont1.get_balance())  
    accont1.deposit(500)
    print(accont1.get_balance())  
    accont1.withdraw(300)
    print(accont1.get_balance())  
    accont1.withdraw(2000)  

    print("_"*15)


    print(accont1.get_account_holder()) 
    print(accont1.get_account_number())
    print("_"*15)


    accont2 = BankAccount("nora")


    print(accont2.get_account_holder())  
    print(accont2.get_account_number())  