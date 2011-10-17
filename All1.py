import random

def TOS():
	print "Series: The Original Series"
	seasons = [1, 2, 3]
	season1 = []
	season2 = []
	season3 = []

	for i in range(1, 31):
		season1.append(i)

	for i in range(1, 27):
		season2.append(i)

	for i in range(1, 25):
		season3.append(i)

	random.shuffle(seasons)
	season = seasons[0]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[0]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[0]
	else:
		random.shuffle(season3)
		print "Episode: %d" % season3[0]
		
def TAS():
	print "Series: The Animated Series"
	seasons = [1, 2]
	season1 = []
	season2 = []

	for i in range(1, 17):
		season1.append(i)

	for i in range(1, 7):
		season2.append(i)

	random.shuffle(seasons)
	season = seasons[0]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[0]
	else:
		random.shuffle(season2)
		print "Episode: %d" % season2[0]

def TNG():
	print "Series: The Next Generation"
	seasons = [1, 2, 3, 4, 5, 6, 7]
	season1 = []
	season2 = []
	season3 = []
	season4 = []
	season5 = []
	season6 = []
	season7 = []

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

def DS9():
	print "Series: Deep Space Nine"
	seasons = [1, 2, 3, 4, 5, 6, 7]
	season1 = []
	season2 = []
	season3 = []
	season4 = []
	season5 = []
	season6 = []
	season7 = []

	for i in range(1, 21):
		season1.append(i)

	for i in range(1, 27):
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

def VOY():
	print "Series: Voyager"
	seasons = [1, 2, 3, 4, 5, 6, 7]
	season1 = []
	season2 = []
	season3 = []
	season4 = []
	season5 = []
	season6 = []
	season7 = []

	for i in range(1, 17):
		season1.append(i)

	for i in range(1, 27):
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

def ENT():
	print "Series: Enterprise"
	seasons = [1, 2, 3, 4]
	season1 = []
	season2 = []
	season3 = []
	season4 = []

	for i in range(1, 26):
		season1.append(i)

	for i in range(1, 27):
		season2.append(i)

	for i in range(1, 25):
		season3.append(i)
	
	for i in range(1, 23):
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

		
which_series = ["The Original Series","The Animated Series", "The Next Generation","Deep Space Nine","Voyager", "Enterprise"]

random.shuffle(which_series)
series = which_series[0]
print "Series: " + series

if series == "The Original Series":
	TOS()
elif series == "The Animated Series":
	TAS()
elif series == "The Next Generation":
	TNG()
elif series == "Deep Space Nine":
	DS9()
elif series == "Voyager":
	VOY()
else:
	ENT()

