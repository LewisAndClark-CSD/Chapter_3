#! /usr/bin/python3
# Program Name: CoinToss.py
# Author: Luke Gosnell
# Date Writen: 10/8/2014

import random
number = 0
heads = 0
tails = 0

print("Welcome to my coin flipping game!")
print("A coin will be flipped 100 times. The results will be posted at the end.")

while number != 100:
        a = random.randint(1,2) 
        if a == 1:
            number += 1
            heads += 1
        if a == 2:
            number += 1
            tails += 1
print(heads, "heads and", tails, "tails.")

