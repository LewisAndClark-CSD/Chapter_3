#GuessYourNumber.py
#By: Karlos Calvillo
#10/8/14

import random

tries=1
low=1
high=100
b=random.randint(low,high)

a=input("Is your number "+str(b)+"? Higher or lower?: ")

while a !="yes":
    if a == "higher":
        tries+=1
        low=b
        b=random.randint(low,high)
        a=input("Is your number "+str(b)+"? Higher or lower?: ")
    elif a == "lower":
        tries+=1
        high=b
        b=random.randint(low,high)
        a=input("Is your number "+str(b)+"? Higher or lower?: ")


print("I guessed it finally! The number was: "+str(b))
print("It took me: "+str(tries),"tries")
