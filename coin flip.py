#Coin Flipper
#Author: Brad Riley
import random
count = 0
heads = 0
tails = 0
while count <= 100:
    count += 1
    flip = random.randint(1,2)
    if flip == 1:
        print('You flipped a heads')
        heads += 1
    else:
        print('You flipped a tails')
        tails += 1
print('You flipped', str(heads), 'heads'+' and '+str(tails)+' tails.')
