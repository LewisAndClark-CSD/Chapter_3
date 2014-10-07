# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
#
#Last edited: Alton Stillwell
#- Added a limit to the number of guesses with 'limit'

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
limit = 6
end = ''
# guessing loop
while guess != the_number:
    if end != 'true':
        if tries != limit:
            if guess > the_number:
                print("Lower...")
            else:
                print("Higher...")
            
            guess = int(input("Take a guess: "))
            tries += 1
        else:
            end = 'true'
            guess = the_number
        
if end == 'true':
    print("\nYou suck really bad:(")
else:
    print("\nYou guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

input("\nPress the enter key to exit.")
