# Guess your number
#author: Bo Meers

import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

tries = 1
low = 1
high = 100
b = random.randint(low,high)

a = input("Is your number " + str(b) + " ? (higher/lower/yes) ")

while a != 'yes':

    if a == "higher":
        low = b
        b = random.randint(low, high)
        tries += 1
        a = input("Is your number " + str(b) + " ? (higher/lower/yes) ")

    elif a == "lower":
        high = b
        b = random.randint(low, high)
        tries += 1
        a = input("Is your number " + str(b) + " ? (higher/lower/yes) ")
        
print("\nI guessed it!  The number was", a)
print("And it only took me", tries, "tries!")
  
input("\nPress the enter key to exit.")
