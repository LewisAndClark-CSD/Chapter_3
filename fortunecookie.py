# fortunecookie.py
# Created by: Zach Golik
############################
import random

print("This is a fortune cookie simulator!")
print("I will now read your fortune...")

fortune=random.randint(1,5)

if fortune == 1:
    print("\n\nYour nan will lose her legs in a week :(")
elif fortune==2:
    print("""\n\nYou will find some girls tomorrow and talk to them.
    But, you'll get turned down""")
elif fortune==3:
    print("\n\nYour mom will step on a crack, destroying the world :/")
elif fortune==4:
    print("\n\nUmmmm, you will get a ebola...")
elif fortune==5:
    print("\n\nNothing, your future is a dull one :p")
else:
    print("\n\nI cannot read your fortune. Sorry bud D:")

input("\n\nPress enter when done viewing your fortune! ")
