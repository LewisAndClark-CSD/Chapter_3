#! /usr/bin/python3
# Program Name: Guess_Your_Number.py
# Author: Luke Gosnell
# Date Writen: 10/8/2014

import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nThink of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

tries = 1
low = 1
high = 100

a = random.randint(low, high)
b = input("Is your number " + str(a) + "? (lower/higher/yes) ")

while b != "yes":
    if b == "higher":
        low = a
        a = random.randint(low, high)
        tries += 1
        b = input("Is your number " + str(a) + "? (lower/higher/yes)")
        
    elif b == "lower":
        high = a
        a = random.randint(low, high)
        tries += 1
        b = input("Is your number " + str(a) + "? (lower/higher/yes)")

print("I guessed it! The number was", b)
print("And it only took me", tries, "tries!")
exit()
