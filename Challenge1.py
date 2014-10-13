# Fortune cookie

import random

print("Your forune is...")

fortune = random.randint(1, 5)

if fortune == 1:
    print("Great things are ahead for you.")
elif fortune == 2:
    print("You will meet with an old friend today.")
elif fortune == 3:
    print("You will recieve a prize soon.")
elif fortune == 4:
    print("Be careful bad things might arise soon.")
elif fortune == 5:
    print("You will find your true love soon")
else:
    print("Your fortune is unpredictable an error has been made")
input("\n\nPress the enter key to exit.")

