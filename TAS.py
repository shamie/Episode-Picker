import random

seasons = [1, 2]
season1 = []
season2 = []

# creates a list of each episode in each season

for i in range(1, 17):
	season1.append(i)

for i in range(1, 7):
	season2.append(i)

# picks and prints random season
random.shuffle(seasons)
season = seasons[0]
print "Season: %d" % season

# picks and prints random episode based on season
if season == 1:
	random.shuffle(season1)
	print "Episode: %d" % season1[0]
else:
	random.shuffle(season2)
	print "Episode: %d" % season2[0]
