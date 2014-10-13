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
number = int(input("Enter your number: "))
guess = random.randint(1,100)
print(guess)
tries = 1
highest = 100
lowest = 0



# guessing loop
while guess != number:
    x = input("Do i need to go higher or lower? ")
    if x == "lower":
        highest = guess - 1
        
    elif x ==  "higher":
        lowest = guess + 1
    guess = random.randint(lowest, highest)
    print(guess)
    tries += 1




print("I guessed it!  The number was", number)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
