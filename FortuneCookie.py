#FortuneCookie.py
#By: Karlos Calvillo
#10/8/14

import random

print("YAY! You found a fortune cookie!")
print("It says-")

fortune = random.randint(1, 5)

if fortune == 1:
    print("You will soon find great treasure.")

elif fortune ==2:
    print("Great luck will come your way today.")

elif fortune ==3:
    print("Nothing bad will happen to you today.")

elif fortune ==4:
    print("A great opportunity will be given to you soon.")

elif fortune ==5:
    print("You will find something awesome today.")

else:
    print("Ouch...the cookie has no fortune...")
