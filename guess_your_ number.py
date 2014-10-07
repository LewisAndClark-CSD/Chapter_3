# Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

# set the initial values
#1-have user select their number(1-100)
#2-have computer initially guess 50
#3-ask user if higher/lower/correct
#LOOP
#if correct, end
#elif lower was entered, guess previous number by /2 (round up if needed)
#elif higher was entered, guess previous number increased by 50%(round up if needed)
#elif correct was entered, end program, state number of tries
#else, go back to loop
#END LOOP

print("I guessed it!  The number was", the_number)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
