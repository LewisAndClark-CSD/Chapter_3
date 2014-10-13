#modified_guess_my_number.py
#By: Karlos Calvillo
#10/7/14
import random

number=random.randint(1, 100)
guess=int(input("Guess number here: "))
tries = 1

while guess != number:
    if tries >4:
        print("Too bad. You suck at guessing.")
        print("The number was",number)
        exit()
    elif guess> number:
        print("Higher")

    elif guess< number:
        print("Lower")

    tries += 1
    guess = int(input("Guess number here: "))

    
print("YAY you got it! The right number was", number)
print("It only took you", tries, "tries!\n")


