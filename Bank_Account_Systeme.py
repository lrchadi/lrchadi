#Main Function.
def main():
    global balance
    balance = float(input("Enter your balance: "))
    user_input = str()

    # Re-ask the user until he stop the Programm
    while user_input != 'End':
        print("=" * 30)
        print("Tap 'End' To Stop!")
        user_input = input("Choose one of these:\n1- Add to your Account.\n2- WithDraw money.\n3- See you Current Balance\n")
        if user_input == '1':
            Add_to_account()
        elif user_input == '2':
            Withdraw_money()
        elif user_input == '3':
            See_account()
        else:
            print("Please select one from the above!") if user_input != 'End' else "" 
    #End of the Programm  
    print("See you Later!")

#Add to Acc Function.
def Add_to_account():
    try:
        global balance
        add_money = float(input("Enter How much money you wanna add: "))
        balance += add_money
        if balance:
            print("Money was added Successfuly!")
    except ValueError:
        print("Something went wrong, Try again! (Try to Enter Numbers Only!)")

# Withdraw money Function.
def Withdraw_money():   
    global balance
    try:
        withdraw = float(input("How much money you want: "))
        if withdraw <= balance and withdraw >= 100 and withdraw <= 2000:
            balance -= withdraw
            print("Withdraw Successfuly!")
        elif withdraw < 100:
            print("You can't withdraw less than 100 MAD.")
        elif withdraw > 2000:
            print("You can't withdraw more than 2000 MAD.")
        elif balance == 0:
            print("Your account is EMPTY!")
        else:
            print("You don't have Enough money to Withdraw.")
    except ValueError:
        print("Something went wrong, Try again! (Try to Enter Numbers Only!)")

# See account balance
def See_account():
    print(f"Your current balance is {balance:.2f} MAD.") if balance >= 0 else "You have nothing in your account!"

#Main Function
main()
