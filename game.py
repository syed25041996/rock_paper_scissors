import random

def game(arg):
        if arg == "R" and options_AI == "Paper":
            print("Computer wins")
        elif arg == "R" and options_AI == "Scissors": 
            print("You win")
        elif arg == "R" and options_AI == "Rock": 
            print("Draw")
        elif arg == "P" and options_AI == "Paper": 
            print("Draw")
        elif arg == "P" and options_AI == "Rock": 
            print("You win")
        elif arg == "P" and options_AI == "Scissors": 
            print("Computer Wins")
        elif arg == "S" and  options_AI == "Scissors": 
            print("Draw")
        elif arg == "S" and  options_AI == "Rock": 
            print("Computer wins")
        elif arg == "S" and options_AI == "Paper": 
            print("you win")
        else:
            print("You have given a wrong input! Wanna try again?")
            user_retry = input("If yes then press Y else press N: ")
            if user_retry == "Y":
                arg = input("Enter Rock Paper or Scissors as R, P or S: ")
                game(arg)   #Recursive fucntion
            else:
                print("Thank you for playing")

options_AI = ["Rock", "Paper", "Scissors"]
options_AI = random.choice(options_AI)
print("----------------Let's get started---------------\n","The rules are as follow \n"
, "--> Rock beats Scissors but looses to paper \n", "--> Paper beats rocks but looses to scissors \n", 
"--> Scissors beats paper but loses to rock\n")
user = input("Enter Rock Paper or Scissors as R, P or S: ")
game(user)
# print(options_AI) # To check what the computer has played

