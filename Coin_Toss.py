#! /usr/bin/python3
# Program Name: Coin_Toss.py
# Author Name: Thomas Morrissey
# Date Written: 10-7-2014

import random
import time

Toss=0
Heads=0
Tails=0

print("Welcome to Coin Toss!")
print("Today I will toss one coin one hundred times and you, the player, will guess the result!")
Continue = input("Are you Ready to play? (Y/N)")

if Continue=="N":
    print("Okay, then.")
    exit()
if Continue=="Y":
    print("Let's get this show on the road!")
    while Toss < 100:
        Coin=random.randint(1,2)
        if Coin == 1:
            Toss += 1
            Heads += 1
        if Coin ==2:
            Toss += 1
            Tails += 1
print("The results are "+str(Heads)+" heads and "+str(Tails)+" tails out of "+str(Toss)+" tosses.")            
            
        

    
        
    
      
