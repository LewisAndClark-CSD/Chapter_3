#Chapter 3 Challenge 2
#Coin Flipper
#Flips a coin 100 times and outputs the results
#Author: Alton Stillwell
##########################
import random
heads = 0
tails = 0
flips = 0
temp = 0

print("\tWelcome to Alton's amazing coin fliping program!")
print("\nThe coin has been flipped 100 times, here are the results:")

while flips < 100:
    temp = random.randint(1,2)
    if temp == 1:
        heads += 1
    elif temp == 2:
        tails += 1
    else:
        print("error")
    flips = flips + 1
print("\nHeads appeared", heads , "times.")
print("Tails appeared", tails, "times.")

    
