#Rock-paper-scissor game
#Random Lib 
import random
#Variables.
user_score = 0
prog_score = 0
#The Number of Rounds
rounds = int(input("Select How many rounds to paly: "))
for i in range(1, rounds+1):
    #Game Rules and The Random Select
    rules = ['rock', 'paper', 'scissor']
    prog_select = random.choice(rules)
    print("=" * 30)
    user_input = input("Choose between (rock-paper-scissor): ")
    #Conditions..
    if user_input == 'rock':
        if prog_select == 'scissor':
            print(prog_select)
            print("You Won!")
            user_score += 1
        elif prog_select == 'paper':
            print(prog_select)
            print("The Programm has win!")
            prog_score += 1
        else:
            print(prog_select)
            print("You are Equals!")

    if user_input == 'paper':
        if prog_select == 'rock':
            print(prog_select)
            print("You Won!")
            user_score += 1
        elif prog_select == 'scissor':
            print(prog_select)
            print("The Programm has win!")
            prog_score += 1
        else:
            print(prog_select)
            print("You are Equals!")

    if user_input == 'scissor':
        if prog_select == 'paper':
            print(prog_select)
            print("You Won!")
            user_score += 1
        elif prog_select == 'rock':
            print(prog_select)
            print("The Programm has win!")
            prog_score += 1
        else:
            print(prog_select)
            print("You are Equals!")

print("=" * 30)
#Show the Score of the player and the Compture.
print(f"You Score is {user_score}.\nThe Computer Score is {prog_score}.")
if user_score > prog_score:
    print("You Won the Match, Yeaaahh!!!!")
else:
    print("The Proramm won the Match!!")