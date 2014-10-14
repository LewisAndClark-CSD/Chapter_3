#! /usr/bin/python3
# Program Name: Mod_Guess_My_Number.py
# Author: Luke Gosnell
# Date Writen: 10/8/2014

import random  

#Opening Remarks
print("Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if tries >= 5:
        print("Too many tries! GAME OVER!")
        exit()
    elif guess > the_number:
        print("Lower!")
    else:
        print("Higher!")
     
    tries += 1 
    guess = int(input("Guess a number: "))


print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")

#Program Closing  
input("Press the enter key to exit.")
