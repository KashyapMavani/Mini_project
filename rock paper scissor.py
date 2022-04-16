from pickle import TRUE
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

your_name = input("Enter your Name : ")
print("Hi",your_name,"Let's Start playing Rock Papaer Scissors")

while TRUE:
    user_input = input("choose your pick : rock / paper / scissors or Q to quite. : ").lower()
    if user_input == "q":
        print("You Won", user_wins, "times")
        print("Computer Won", computer_wins,"times")
        break

    if user_input not in options:
        print("Please choose the pick from the given options.")
        continue

    random_number = random.randrange(0,2)

    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "rock" and computer_pick == "paper":
        print("You Lose")
        computer_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "rock" and computer_pick == "rock":
        print("Same Pick no one wins")
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue


    if user_input == "scissors" and computer_pick == "paper":
        print("You Won")
        user_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "scissors" and computer_pick == "rock":
        print("You Lose")
        computer_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "scissors" and computer_pick == "scissors":
        print("Same Pick no one wins")
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue

    
    if user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "paper" and computer_pick == "scissors":
        print("You Lose")
        computer_wins += 1
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue
    if user_input == "paper" and computer_pick == "paper":
        print("Same Pick no one wins")
        print("Your score",user_wins)
        print("Computer score",computer_wins)
        continue  

# print("You Won", user_wins, "times")
# print("Computer Won", computer_wins,"times")
print("GoodByee", your_name+"!!", "See You next time.")
