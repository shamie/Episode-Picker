import random

seasons = [1, 2, 3, 4]
season1 = []
season2 = []
season3 = []
season4 = []

# creates a list of each episode in each season
for i in range(1, 26):
	season1.append(i)

for i in range(1, 27):
	season2.append(i)

for i in range(1, 25):
	season3.append(i)
	
for i in range(1, 23:
	season4.append(i)

random.shuffle(seasons)
season = seasons[0]
print "Season: %d" % season

if season == 1:
	random.shuffle(season1)
	print "Episode: %d" % season1[0]
elif season == 2:
	random.shuffle(season2)
	print "Episode: %d" % season2[0]
elif season == 3:
	random.shuffle(season3)
	print "Episode: %d" % season3[0]
else:
	random.shuffle(season4)
	print "Episode: %d" % season4[0]
