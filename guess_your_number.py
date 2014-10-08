import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

# set the initial values

tries = 1
Low = 1
High =100
Guess = random.randint(Low,High)
response = " "
# guessing loop
response = input("Is "+str(Guess)+" your number(higher, lower, or equal)?")
while response != "equal":
    if response == "lower":
        tries += 1
        High = Guess 
        Guess = random.randint(Low,High)
    elif response == "higher":
        tries += 1
        Low = Guess
        Guess = random.randint(Low,High)
    else:
        print("Use higher, lower, or equal commands only?")

    print("low:", Low, "High:", High)
    response = input("Is "+str(Guess)+" your number (higher,lower, or equal)?")




print("I guessed it!  The number was", Guess)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
