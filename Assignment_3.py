import os
import random
from time import sleep

# Collections 
menu_options = {"Deposit": "D", "Withdraw": "W", "Quit": "Q"}
user_options = ""

# random balance
balance = random.uniform(1000, 10000)


while user_options != "Q":
    
    text_header = "*" * 40
    text_financial = "PIXELL RIVER FINANCIAL".center(40)
    text_simulator = "ATM Simulator".center(40)
    text_balance = f"Your current balance is: ${balance:.2f}".center(40)

    text_deposit = "Deposit: D".center(40)
    text_withdraw = "Withdraw: W".center(40)
    text_quit = "Quit: Q".center(40)
    text_invalid = "INVALID SELECTION".center(40)
    text_insufficient_funds = "INSUFFICIENT FUNDS".center(40)

    
    print(f"{text_header}"
          f"\n{text_financial}"
          f"\n{text_simulator}\n"
          f"\n{text_balance}\n"
          f"\n{text_deposit}"
          f"\n{text_withdraw}"
          f"\n{text_quit}"
          f"\n{text_header}")
    
    user_options = input("Enter your selection ").upper()
    
    if user_options not in menu_options.values(): 
        print(f"\n{text_header}"
              f"\n{text_invalid}"
              f"\n{text_header}")
        
    elif user_options == "D":
            money_increase = float(input("Enter your transaction amount: "))
            balance += money_increase
            
    elif user_options == "W":
        money_increase = float(input("Enter your transaction amount: "))
        
        if money_increase > balance:
              print(f"\n{text_header}"
                    f"\n{text_insufficient_funds}"
                    f"\n{text_header}")
        else:
            balance -= money_increase
            print(f"\n{text_header}")

    os.system('cls' if os.name == 'nt' else 'clear')

print("Program is shutting down")