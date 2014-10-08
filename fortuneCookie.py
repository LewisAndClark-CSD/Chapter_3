#fortuneCookie.py
#Karl Pearson
#10/3/2014
import random
import time

fortune=random.randint(0,5)
print('You open your fortune cookie...')
time.sleep(5)
if fortune == 1:
      print('You will hear good news today.')
elif fortune == 2 :
      print('Good things come to those who wait.')
elif fortune ==3 :
      print('Meeting adversity well is the source of your strength.')
elif fortune == 4:
      print('Inner balance is the key to happiness.')
elif fortune == 5:
      print('You will eat a Poptart today.')
else:
      print('Your cookie is empty...woops.')
