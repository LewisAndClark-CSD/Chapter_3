import random

fortune = random.randint(1,5)

if fortune == 1:
    print("Something good will happen")
elif fortune == 2:
    print("Something good will not happen")
elif fortune == 3:
    print("Something bad will happen")
elif fortune == 4:
    print("Something bad will not happen")
elif fortune == 5:
    print("That wasn't chicken")
else:
    print("That isn't a fortune choice")

input("Press enter to leave")
