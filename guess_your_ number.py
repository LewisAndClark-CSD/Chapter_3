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
number = input("Enter a number to guess(1-100): ")
guess = random.randint(1,100)
x = 1
y = 100
tries = 0
# guessing loop
while guess != number:
    if guess < number:
        print(guess)
        print("My guess was lower.")
        x = guess
        guess = random.randint(x,y)
        tries += 1
    elif guess > number:
        print(guess)
        print("My guess was higher.")
        y = guess
        guess = random.randint(x,y)
        tries += 1
print("I guessed it!  The number was", number)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
