#Fortune Cookie Cracker
#By: Bo Meers

import random
import time
timer = 10

print("I see you have a fortune cookie...")
time.sleep(2)
a = input("Want me to break it? (y/n) ")
if a == "y":
    print("WHAP!!!")
    time.sleep(1)
    print("Let's see...")
    time.sleep(2)
    b = random.randint(1, 5)
    if b == 1:
        print("oh...")
        time.sleep(1)
        print("Looks like your prone to dying...")
    elif b == 2:
        print("HAHA")
        time.sleep(1)
        print("It says you're going to be successful in life!")
        time.sleep(2)
        print("I did'nt know that fortune cookies could lie...")
    elif b == 3:
        print("Umm...")
        time.sleep(1)
        print("Yeah this one shoudnt be here...")
        a = input('a: "read it." b: "Oh well." (a/b)')
        if a == "a":
            print("You just lost the game.")
        elif a == "b":
            print("What a shame.")
    elif b == 4:
        print("You have the ability to destroy batman.")
        time.sleep(2)
        print("doubt it")
    elif b == 5:
        print("You've entered the deep part of the fortune cookie...")
        time.sleep(3)
        print("oh... oh no...")
        time.sleep(2)
        print("ALT+F4!!! ALT+F4!!! ALT+F4!!!")
        while timer != -1:
            print(timer)
            timer = timer - 1
            time.sleep(1)
        print("Obtaining user info...")
        time.sleep(2)
        print("Your social security number has been destributed! Have a nice day!")
elif a == "n":
    print("FINE!")
