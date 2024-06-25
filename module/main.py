from displayAccounts import DisplayAccounts as DA
from bank_account import BankAccount as BA

account1 = DA("Abdullah in Tuwaiq", 50000)
account2 = DA("Saad", 1000)
account3 = DA("Mo", 100000)
account4 = DA("Ibrahim", 100900)

account1.display_menu()
print("\nAccount Details 👨🏻‍💻:")
account1.display_account()
account2.display_account()
account3.display_account()
account4.display_account()
print("\nGenerated Account Numbers✅: ")
print(BA.generated_account_numbers)
