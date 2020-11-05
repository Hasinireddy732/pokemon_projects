import random
from time import sleep

choices = ["Charmender","Squirtle","Bulbasur"]

computer = random.choice(choices)

player = False

name = input("Hello please enter your name")

while player == False:
    print(f"Hello,{name}Welcome to the Pokemon Battles Game!!")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'")
    if player == computer:
        print("Tie!!")
    elif player == "Charmender":
        if computer == "Squirtle":
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You lose!!")
        else:
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You win!!")
    elif player == "Balbusar":
        if computer == "charmender":
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You lose!!")
        else:
            print("\nplease wait we are loading your results...")
            sleep(2)
            print("You win!!")
    elif player == "stop":
        print("Thanks for playing")
        break
    else:
        print("Thats not a valif play ")

        player = false
