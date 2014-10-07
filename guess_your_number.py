# Guess your number
#author: Bo Meers
import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

the_number = int(input("What's your number? "))
tries = 1
b = random.randint(1,100)

if the_number > 100:
    the_number = int(input("I'm pretty sure i said 1 to 100... try again "))

elif the_number < 1:
    the_number = int(input("I'm pretty sure i said 1 to 100... try again "))
                     
while b != the_number:
    b = random.randint(1,100)
    tries += 1
    
print("\nI guessed it!  The number was", the_number)
print("And it only took me", tries, "tries!")
  
input("\nPress the enter key to exit.")
