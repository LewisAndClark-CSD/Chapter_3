# Program Name: Bo's Guessing Machine
# Author: Bo Meers

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 attempts.\n")

the_number = random.randint(1, 100)
guess = int(input("Guess a number: "))
tries = 1
tr = 0

while guess != '':

    while tr < 11:

        if guess < the_number:

            tr += 1
            tries += 1
            guess = int(input("Guess higher: "))

        elif guess > the_number:

            tr += 1
            tries += 1
            guess = int(input("Guess lower: "))
    
        elif guess == the_number:
            print("You guessed it! The number was", the_number)
            print("And it only took you", tries, "tries!")
 
            guess = input("\n\nPress the enter key to exit.")

    print("Sorry. You didnt guess", the_number, "in 10 tries.")
