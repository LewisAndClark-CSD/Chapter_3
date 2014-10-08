#challenge16.py
#Karl Pearson
#10/1/14
import random
import time
print('Welcome to Guess The Number')
print('You have 5 tries to guess the number')
print('Good Luck')
number = random.randint(1, 100)
guess = int(input("Guess number: "))
tries = 1
while guess != number:
    if tries >4:
       print('You took to many guesses')
       number2=str(number)
       print('The number was: '+number2)
       time.sleep(5)
       exit()
    elif guess > number:
        print('Lower!')
    elif guess< number:
        print('Higher!')
    guess = int(input("Guess number: "))
    tries+=1
attempt=str(tries)
numberStr=str(number)
print("Nice job! It took you "+attempt+" tries to guess "+numberStr+"!")
