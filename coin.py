# Coin Flipper
#author: Bo Meers

import random
number = 0
heads = 0
tails = 0

print("\tWelcome to coin flipper.")
print("\nA coin will be flipped 100 times")
print("The total of each side will be printed at the end.")
a = input("\nWould you like to play? (y/n) ")

if a == "y":
    while number != 100:
        b = random.randint(1,2) 
        if b == 1:
            number += 1
            heads += 1
        if b == 2:
            number += 1
            tails += 1
    print("You flipped", heads, "heads and", tails, "tails.")
elif a == "n":
    print("Ok then.")
