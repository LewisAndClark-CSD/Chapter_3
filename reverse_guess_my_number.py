import random

guess = 0
tries = 0
number = int(input("Pick a number between 1 and 100 for the computer to guess:"))

while number > 100 or number < 1:
    number = input("Pick a number between 1 and 100 for the computer to guess:")

while guess != number:
    guess = random.randrange(101)
    print ("The computer guessed", guess)
    tries += 1
    past = guess
while guess < number:
    guess = random.randrange(guess, 101)
    print ("The computer guessed", guess)
    tries += 1
while guess > number:
    guess = random.randrange(0, guess)
    print ("The computer guessed", guess)
    tries += 1

print ("The computer guessed your number after", tries, "tries.")
