# Challenge2.py
#Flip a coin 100 times
#Tell how many times on head
#Tell how many times on tails

import random
flips = 0
heads = 0
tails = 0

print("\tThis is Sam's Mighty Coin Flipping Simulation")
print("\nIn this simulation, we will flip a coin 100 times")
print("We will tell you the amount of times the coin is heads or tails.\n")

while flips != 100:
    coin = random.randint(1, 2)
    if coin == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    flips = flips + 1

print("Heads:", heads)
print("Tails:", tails)
