from bank_account import BankAccount as BA

class DisplayAccounts(BA):
    def __init__(self, account_holder: str, initial_balance=0):
        super().__init__(account_holder, initial_balance)

    def display_account(self):
        print(f"Account Holder: {self.get_account_holder()}")
        print(f"Account Number: {self.get_account_number()}")
        print(f"Balance: {self.get_balance()}")

    def display_menu(self):
        while True:
            print("\n\n\n💰<----- Welcome to the Bank of Tuwaiq ----->💰\n\n\n")
            print("🏦<----- Account Information ----->🏦\n\n")
            self.display_account()
            print("\n🏦<----- Account Information Ended ----->🏦\n\n")
            
            user_add_money = input(
                "Do you want to add money to your account?? Press 1 \n"
                "Do you want to see the accounts?? Press 2 \n"
                "Type 'exit' to quit: ").lower()  #! to make the input case insensitive
                
            if user_add_money == "1":
                amount = float(input("Enter the amount you want to add: "))
                self.deposit(amount)
                print("Your new balance is: ", self.get_balance())
                
            elif user_add_money == "2":
                self.display_account()
                
            elif user_add_money in ["no", "exit", "quit"]:
                print("Thank you for using our bank services! 💰🎩")
                break  
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("This was Imported from DisplayAccounts class.")