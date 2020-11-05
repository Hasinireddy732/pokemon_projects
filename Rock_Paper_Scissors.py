import random
from time import sleep

choice = ["Rock" , "Paper" , "Scissors"]
computer = random.choice(choice)

player = False

while player == False:
    print("Welcome to Rock,paper and scissors")
    print("\nPlease wait the game is loading.....")
    sleep(3)
    player = input("Which one do you want to choose?\n'Rock': 'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop': ")
    if player == computer:
        print("Please wait we are loading your results...")
        sleep(2)
        print("It's a Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You have lost!!")
        else:
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You Have Won!!")
    elif player == "Scissors":
        if computer == "Rock":
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You have lost!!")
        else:
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You have won")
    elif player == "Paper":
            if computer == "Scissors":
                print("\nplease wait we are loading your results...")
                sleep(2)
                print("You have lost!!")
        else:
            print("\nplease wait we are loading your results...")
            sleep(2))
            print("You have won")
    elif player == "Stop":
            print("Thanks for playing")
            break
    else:
        print("That's not a valid play!!")
        break

player == False
