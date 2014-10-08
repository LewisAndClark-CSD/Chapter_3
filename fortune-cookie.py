# Fortune Cookie.py
#Author: Brad Riley
import random
ranint = random.randint(1,5)
print("You have a fortune cookie.....")
print("It says....\n")
if ranint == 1:
    print("You are going to have a horrible day.")
elif ranint == 2:
    print("You are going to have the worst day of your life")
elif  ranint == 3:
    print("You are going to lose something very valuable today, like a limb.")
elif ranint == 4:
    print('A depressing chapter in your life will start today.')
else:
    print('You will survive today.')
