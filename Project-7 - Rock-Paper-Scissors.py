## Project 7: Rock - Paper - Scissor

import random

print("""Winning Rules:  \n
      "Rock vs paper => paper wins" \n
      "Rock vs scissor => Rock wins" \n
      "paper vs scissor => scissor wins \n""")

# Step 1: Conditions for the User

while True:
    print("Enter Choice 1. Rock 2. Paper 3. Scissor")
    
    user_choice = int(input("User Turn : "))
    
    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Enter valid input : "))
        
    if user_choice == 1:
        user_choice_name = "Rock"
    
    elif user_choice == 2:
        user_choice_name = "Paper"
    
    else:
        user_choice_name = "Scissor"
    
    print("User choice is : " + user_choice_name)
    print("\n Its computers Turn : ")
    
    
# Step 2: Conditions for the Computer

    comp_choice = random.randint(1, 3)    
    
    while comp_choice == user_choice:
        comp_choice = random.randint(1, 3)
    
    if comp_choice == 1:
        comp_choice_name = "Rock"        
    
    elif comp_choice == 2:
        comp_choice_name = "Paper"        
    
    else:
        comp_choice_name = "Scissor"        
    
    print("Computer choice is : " + comp_choice_name)    
    print(user_choice_name + " V/s " + comp_choice_name)


# Step 3: Condition of Winning !!!
    
# Step 3: Condition of Winning !!!
    
    if((user_choice == 1 and comp_choice == 2) or
      (user_choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
         
    elif((user_choice == 1 and comp_choice == 3) or
        (user_choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"

# Step 4: Printing the Winner
        
    if result == user_choice_name:
        print("** User wins **>")
    else:
        print("<** Computer wins **>")
         
    print("Do you want to play again? (Y/N)")
    ans = input()
 
 
# if user input n or N then Break
    if ans == 'n' or ans == 'N':
        break
     
print("\nThanks for playing")