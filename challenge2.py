import random

flipCount = 0
heads = 0
tails = 0


while flipCount < 100:
    coin = random.randint(1,2)
    flipCount += 1
    if coin == 1:
        heads += 1
        coin = random.randint(1,2)
    elif coin == 2:
        tails += 1
        coin = random.randint(1,2)

print("Heads:", heads)
print("Tails:", tails)
