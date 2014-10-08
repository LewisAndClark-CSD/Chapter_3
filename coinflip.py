# coinflip.py
# Created by: Zach Golik

import random
flips=0
heads=0
tails=0

print("In this program, a coin will be flipped 100 times.")
print("We will tell you the ratio of heads to tails.")

while flips != 100:
    temp= random.randint(1,2)
    if temp == 1:
        heads=heads+1
    else:
        tails=tails+1
    flips=flips+1

print("\n\nThe ratio of heads to tails is ("+str(heads)+',',str(tails)+')')
