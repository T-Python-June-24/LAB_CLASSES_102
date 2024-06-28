from colorama import Fore
from BankAccount import BankAccount, AccountManager
from art import text2art
from rich.console import Console
from rich.table import Table
import random
import os   

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isUnique(id):
    """
    Checks if the given id number is unique.
    This implementation simply checks against a list of used account numbers,
    but in a real-world scenario, you would likely need to check against a
    database of existing account numbers.
    """
    used_account_obj = []
    if id in used_account_obj:
        return False
    else:
        used_account_obj.append(id)
        return True
def generateUniqueId():
    """
    Generates a unique 10-digit bank account number.
    """
    # Generate a random 10-digit number
    id = ''.join(str(random.randint(0, 9)) for i in range(10))
    # Check if the generated number is unique
    while True:
        if isUnique(id):
            return id
        else:
            id = ''.join(str(random.randint(0, 9)) for i in range(10))
    
def main():

    Account_Manager = AccountManager()

    def add_account(): # لاتمتتة عملية الاضافه وعدم تكرار الكود عند الحاجة للاستدعاء
            obj_id = generateUniqueId()
            name = input("\nEnter name of account holder: ")
            userInput = input("\nEnter the balance of the account if there is one: ")
            if is_number(userInput):
                balance = float(userInput)
                obj_id = BankAccount(name,balance)
            else:
                obj_id = BankAccount(name)
            Account_Manager.add_account(obj_id)
            return obj_id

    while(True):
        clear_terminal()
        print(Fore.LIGHTMAGENTA_EX+text2art("Tuwaiq Bank ",font="small"))
        print(Fore.CYAN+"   1 - Display accounts                        ")
        print(Fore.CYAN+"   2 - Add new Account                         ")
        print(Fore.CYAN+"   3 - Deposit from account                    ")
        print(Fore.CYAN+"   4 - Withdraw from account                   ")
        print(Fore.CYAN+"   5 - Update the name of account number       ")
        print(Fore.CYAN+"   6 - Search of account                       ")
        print(Fore.CYAN+"   7 - Delete account                          ")
        print(Fore.CYAN+"   8 - Exit ",end="\n")
        print(Fore.LIGHTBLUE_EX)

        userInput = input("Enter a number from the above menu: ")

        if userInput == "1":
            try:
                print(Fore.GREEN,end=" ")
                Account_Manager.display_accounts()
                print(Fore.LIGHTBLUE_EX,end=" ")
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
                userInput = input("Do you want to add an account ? Enter 2: ")
                if userInput == "2":
                    try:
                        accont = add_account()
                    except Exception as e:
                        print(Fore.RED+"\nError:",e)
                        print(Fore.LIGHTBLUE_EX)
                    else:
                        print(Fore.GREEN+f"\nAccount number {accont.get_account_number()} has added successfully ")
                        print(Fore.LIGHTBLUE_EX)
    
        elif userInput == "2" :
            try:
                accont = add_account()
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\nAccount number {accont.get_account_number()} has added successfully ")
                print(Fore.LIGHTBLUE_EX)

        elif userInput == "3" :
            try:
                userInput = input("\nEnter account number: ")
                account = Account_Manager.search_account(userInput)
                amount = input("\nEnter amount of money to deposit: ")
                if is_number(amount):
                    amount = float(amount)
                    Account_Manager.deposit(account,amount)
                else:
                    raise Exception("Only provide integer or float number ")
                               
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\n{amount} SAR was deposit to number {userInput} successfully ")
                print(Fore.LIGHTBLUE_EX)

        elif userInput == "4" :
            try:
                userInput = input("\nEnter account number: ")
                account = Account_Manager.search_account(userInput)
                amount = input("\nEnter amount of money to withdraw: ")
                if is_number(amount):
                    amount = float(amount)
                    Account_Manager.withdraw(account,amount)
                else:
                    raise Exception("Only provide integer or float number ")      
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\n{amount} SAR was withdraw from number {userInput} successfully ")
                print(Fore.LIGHTBLUE_EX)

        elif userInput == "5" :
            try:
                account_num = input("\nEnter account number: ")
                updated_name = input("\nEnter new name: ")
                Account_Manager.update_account(account_num,updated_name)
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\nThe name of account number '{account_num}' has changed to '{updated_name}' successfully ")
                print(Fore.LIGHTBLUE_EX)
                
        elif userInput == "6" :
            try:
                userInput = input("\nEnter account number: ")
                account_num = Account_Manager.search_account(userInput)
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\nThe account number '{userInput}' exist ")
                print(Fore.LIGHTBLUE_EX)
                
        elif userInput == "7" :
            try:
                account_num = input("\nEnter account number: ")
                Account_Manager.delete_account(account_num)
            except Exception as e:
                print(Fore.RED+"\nError:",e)
                print(Fore.LIGHTBLUE_EX)
            else:
                print(Fore.GREEN+f"\nThe account number '{account_num}' has deleted successfully ")
                print(Fore.LIGHTBLUE_EX)
                
        elif userInput == "8":
            
            print(Fore.MAGENTA+"\nlogged out\n")
            break

        else:

            print(Fore.RED+"\nError: please enter a number between 1-8 only ")
            print(Fore.LIGHTBLUE_EX)

        input("\nPress enter to continue ")


try:
    
    main()
    
except Exception as e :

    print(Fore.RED+"Error: ",e)
