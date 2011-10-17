import random

seasons = [1, 2, 3, 4, 5, 6, 7]
season1 = []
season2 = []
season3 = []
season4 = []
season5 = []
season6 = []
season7 = []

# creates a list of each episode in each season
for i in range(1, 27):
	season1.append(i)

for i in range(1, 23):
	season2.append(i)

for i in range(1, 27):
	season3.append(i)
	
for i in range(1, 27):
	season4.append(i)

for i in range(1, 27):
	season5.append(i)

for i in range(1, 27):
	season6.append(i)
	
for i in range(1, 27):
	season7.append(i)

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
elif season == 4:
	random.shuffle(season4)
	print "Episode: %d" % season4[0]
elif season == 5:
	random.shuffle(season5)
	print "Episode: %d" % season5[0]
elif season == 6:
	random.shuffle(season6)
	print "Episode: %d" % season6[0]
else:
	random.shuffle(season7)
	print "Episode: %d" % season7[0]
