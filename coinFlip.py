#coinFlip.py
#By: Karlos Calvillo
#10/6/14
import random

number=0
heads=0
tails=0
while number !=100:
    coinFlip=random.randint(1,2)
    if coinFlip==1:
        number+=1
        heads+=1
    if coinFlip==2:
        number+=1
        tails+=1
heads2=str(heads)
tails2=str(tails)
print('Heads= '+heads2+' Tails= '+tails2)
