#! /usr/bin/python3
# Program Name: FortuneCookie.py
# Author: Luke Gosnell
# Date Writen: 10/8/2014

import random

print("You got a fortune cookie!!")
print("Your fortune is...")

fortune = random.randint(1,5)

if fortune == 1:
    prnt("Your future stinks")

elif fortune == 2:
    print("Your future rocks!")

elif fortune == 3:
    print("Anything can kill you. Be prepared...")

elif fortune == 4:
    print("Everybody you love will die")

elif fortune == 5:
    print("Don't go near any blenders for the rest of the day.... Trust me...")
