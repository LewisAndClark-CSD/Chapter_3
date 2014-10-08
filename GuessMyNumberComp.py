#GuessMyNumberComp.py
#Karl Pearson
#10/8/2014
import random

tries=1
low=1
high=100
b=random.randint(low,high)
a=input('is your number '+str(b)+'? Higher or lower? ')

while a!='yes':
    if a=='higher':
        low=b
        b=random.randint(low,high)
        tries+=1
        a=input('is your number '+str(b)+'? Higher or lower? ')
    elif a=='lower':
        high=b
        b=random.randint(low,high)
        tries+=1
        a=input('is your number '+str(b)+'? Higher or lower? ')

print('\nI guessed it!, It was: '+str(b))
print('It only took me '+str(tries)+' tries!')

input('\n\nPress enter key to exit')
