## Project: 2

# Removing Vowels

vowels = ("a","e","i","o","u")

message = input("Enter the message: ")

new_message = ""

for letters in message:
    if letters not in vowels:
        new_message = new_message + letters
        
print("Message without vowels is : {} ".format(new_message))