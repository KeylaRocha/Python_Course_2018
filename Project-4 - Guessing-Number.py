## Project 4: Number Guessing Game !!!

import random

guess = []

cpu_num = random.randint(1,100)

player_num = int(input("Enter a number between 1 to 100 : "))

guess.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too High !")
    else:
        print("Too Low !")
    player_num = int(input("Enter a number between 1 to 100 : "))
    
    guess.append(player_num)
    
else:
    print("Well Done !!!")
    print("You have taken {} guesses ".format(len(guess)))
    print("Here are your guesses : ")
    print(guess)