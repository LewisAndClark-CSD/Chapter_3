# The *trully random Guess your Number
# Author: Brad Riley
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

# set the initial values
tries = 1
low = 1
high = 100
guess = random.randint(low,high)
initialResponse = input('Is the number ' + str(guess)+'? ')

# guessing loop
while initialResponse != 'yes':
    if initialResponse == 'higher':
        low = guess
        guess = random.randint(low,high)
        tries += 1
        initialResponse = input('Is the number ' + str(guess)+'? ')
        
    elif initialResponse == 'lower':
        high = guess
        guess = random.randint(low,high)
        tries += 1
        initialResponse = input('Is the number ' + str(guess)+'? ')
    else:
        print("You must type either 'lower' or 'higher' or 'yes'")
        initialResponse = input('Is the number ' + str(guess)+'? ')
        
print("The computer guessed", guess, "and it was correct!")

print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
