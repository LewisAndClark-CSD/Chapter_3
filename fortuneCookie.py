# Pg. 85 Challenge 1
#Author: Alton Stillwell
#################################
# generate random number
import random
fortune = random.randint(1, 5)
# greeting
print("\nWelcome to Alton's FORTUNE GENERATOR")
print("\n\nYou eat the cookie and find inside the message,")
print("it reads..\n")
# fortunes
if fortune == 1:
    print("A great event in your life awaits you soon.")
elif fortune == 2:
    print("You will make a new friend from an enemy.")
elif fortune == 3:
    print("Happiness awaits you at the end of your trife.")
elif fortune == 4:
    print("You will make someone's life better tomorrow.")
elif fortune == 5:
    print("Tommorow, luck will find its way to you.")
else:
    print("Ebola has found you:)")
input("\n\nPress <enter> to close")
