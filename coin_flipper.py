Python 3.2.3 (default, Feb 20 2013, 14:44:27) 
[GCC 4.7.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import random
coin_heads, coin_tails, times_flipped = 0, 0, 0
timesflipped = 0  # <-- here's what I added.
while timesflipped < 100:
	coin_flips = random.randrange( 2 )
	if coin_flips == 0:
		coin_heads += 1
	else:
		coin_tails += 1
	timesflipped += 1
	
print "Out of 100 flips, " + str(coin_heads) + " were heads and " + str(coin_tails) + " were tails."
