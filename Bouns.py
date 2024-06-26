from bankaccount import BankAccount
import pickle
class AccountManger:
    def __init__(self,name:str) -> None:
        self.__bankAccounts:list=[]
    def add_account(self, bank_account: BankAccount):
        self.__bankAccounts.append(bank_account)
    def display_accounts(self):
        for bankAccount in self.__bankAccounts:
            print(f"Name: {bankAccount.get_account_holder()}- Blance: {bankAccount.get_blance()}")
    def search_accounts(self, account_number):
        for bankAccount in self.__bankAccounts:
            if bankAccount.get_account_number()==account_number:
                return f"Name: {bankAccount.get_account_holder()}- Blance: {bankAccount.get_blance()}"
    def delete_account(self, account_number):
        for bankAccount in self.__bankAccounts:
            if bankAccount.get_account_number()==account_number:
                self.__bankAccounts.remove()
    def save_to_file(self, filename: str):
        with open (f'{filename}','wb') as file:
            pickle.dump(self.__bankAccounts,filename)

    def  load_from_file(self, filename: str):
        with open (f'{filename}','rb') as file:
            pickle.dump(self.__bankAccounts,filename)
b1=BankAccount('saeed',100)
print()
b2=BankAccount('ali',500)
manger=AccountManger('ahmed')
manger.add_account(b1)
manger.add_account(b2)
print(manger.search_accounts(b2.get_account_number()))
manger.save_to_file('file.pickle')





