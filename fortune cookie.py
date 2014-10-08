#fortune cookie
#
#Author: Thomas Morrissey
#Date Written: 10-3-2014

import random

print("You just gained a fortune cookie")
print("Your fortune... ")

fortune = random.randint(1,6)

if fortune == 1:
    #good
    print("is very good. You will get one million dollars!")
elif fortune == 2:
    #okay
    print("is okay.")
elif fortune == 3:
    #odd
    print("is very confusing.")
elif fortune == 4:
    #bad
    print("is very bad. Do not leave your house tommorrow.")
elif fortune == 5:
    #Meh
    print("is mah. Nothing good, just a series of minor bad events.")
else:
    #boring
    print("is very boring. Plese do something.")



