#Coin_flip
#dennis gordick
#10/8/2014
import random
count= 0
heads= 0
tails= 0
coin=["Heads", "Tails"]
while count != 100:
    flip= random.choice(coin)
    if flip == "Heads":
        heads += 1
    elif flip == "Tails":
        tails += 1
    else:
        print("How? This is not possible!")

    count += 1

print("Heads: "+ str(heads))
print("Tails: "+ str(tails))
if int(heads) > int(tails):
    print("Heads win!")
elif int(heads) < int(tails):
    print("Tails win!")
elif int(heads)==int(tails):
    print("IT'S A TIE!")
else:
    print("Again! How do you keep doing this?")
