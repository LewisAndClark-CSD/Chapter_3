# Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money
# Created by: Zach Golik
# Date: 10/7/14

import random

# set initial values

low=0
high=100
randomNum=random.randint(low,high)
response=''
tries=1

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")


# guessing loop
while response != "yes":
    print("Is the number "+str(randomNum)+"?")
    response=input()
    if response == 'higher':
        low = randomNum+1
        randomNum = random.randint(low,100)
        tries = tries+1
    elif response == 'lower':
        high = randomNum-1
        randomNum = random.randint(0,high)
        tries = tries+1 

print("I guessed it!  The number was",str(randomNum)+"!!!" )
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
