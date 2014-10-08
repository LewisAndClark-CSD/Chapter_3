#coinFlip.py
#Karl Pearson
#10/6/2014
import random
import time
print('Welcome to coin flip')
print('The coin will be flipped 100 times')
print('The results will be shown below')
number=0
heads=0
tails=0
while number != 100:
    coin=random.randint(1,2)
    if coin==1:
        tails+=1
        number+=1
    if coin==2:
        heads+=1
        number+=1
heads2=str(heads)
tails2=str(tails)
time.sleep(10)
print('heads= '+heads2+' tails= '+tails2)
    
