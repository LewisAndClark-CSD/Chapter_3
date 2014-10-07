# Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("Welcome to 'Guess Your Number'!\n")
print("I want you to think of a number between 1 and 100.\n")
print("I'll try to guess it in as few attempts as possible.\n")

# set the initial values
the_number= input("What is your number. I wont look.\n")
tries=1
minimum= 1
maximum= 100
guess= random.randint(1, 100)
# guessing loop
while int(the_number) != int(guess):
    print(guess)
    high_low = input("Is it higher or lower?")
# declares the maximum and minumum number the computer should be guessing between
    if high_low == "higher":
        minimum=guess
    elif high_low == "lower":
        maximum=guess
#this is the computer guessing the number
    if high_low == "higher":
        guess= random.randint(minimum, maximum)
    elif high_low== "lower":
        guess= random.randint(minimum, maximum)
#The may or may not be needed... idk if it is
    guess = int(guess)
#This is for tries when printed
    tries += 1
    
    
print("I guessed it!  The number was", the_number)
print("And it only took me", tries, "tries!\n")
  
input("Press the enter key to exit.")
