import random
which_series = ["TOS", "TAS", "TNG", "DS9", "VOY", "ENT"]

def TOS():
	print "Series: The Original Series"
	seasons = [1, 2, 3]
	season1 = []
	season2 = []
	season3 = []

	for i in range(1, 29):
		season1.append(i)

	for i in range(1, 26):
		season2.append(i)

	for i in range(1, 24):
		season3.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]
	else:
		random.shuffle(season3)
		print "Episode: %d" % season3[1]
		
def TAS():
	print "Series: The Animated Series"
	seasons = [1, 2]
	season1 = []
	season2 = []

	for i in range(1, 16):
		season1.append(i)

	for i in range(1, 6):
		season2.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	else:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]

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

	for i in range(1, 26):
		season1.append(i)

	for i in range(1, 22):
		season2.append(i)

	for i in range(1, 26):
		season3.append(i)
	
	for i in range(1, 26):
		season4.append(i)

	for i in range(1, 26):
		season5.append(i)

	for i in range(1, 26):
		season6.append(i)
	
	for i in range(1, 26):
		season7.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]
	elif season == 3:
		random.shuffle(season3)
		print "Episode: %d" % season3[1]
	elif season == 4:
		random.shuffle(season4)
		print "Episode: %d" % season4[1]
	elif season == 5:
		random.shuffle(season5)
		print "Episode: %d" % season5[1]
	elif season == 6:
		random.shuffle(season6)
		print "Episode: %d" % season6[1]
	else:
		random.shuffle(season7)
		print "Episode: %d" % season7[1]

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

	for i in range(1, 20):
		season1.append(i)

	for i in range(1, 26):
		season2.append(i)

	for i in range(1, 26):
		season3.append(i)

	for i in range(1, 26):
		season4.append(i)

	for i in range(1, 26):
		season5.append(i)

	for i in range(1, 26):
		season6.append(i)

	for i in range(1, 26):
		season7.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]
	elif season == 3:
		random.shuffle(season3)
		print "Episode: %d" % season3[1]
	elif season == 4:
		random.shuffle(season4)
		print "Episode: %d" % season4[1]
	elif season == 5:
		random.shuffle(season5)
		print "Episode: %d" % season5[1]
	elif season == 6:
		random.shuffle(season6)
		print "Episode: %d" % season6[1]
	else:
		random.shuffle(season7)
		print "Episode: %d" % season7[1]

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

	for i in range(1, 16):
		season1.append(i)

	for i in range(1, 26):
		season2.append(i)

	for i in range(1, 26):
		season3.append(i)
	
	for i in range(1, 26):
		season4.append(i)

	for i in range(1, 26):
		season5.append(i)

	for i in range(1, 26):
		season6.append(i)
	
	for i in range(1, 26):
		season7.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]
	elif season == 3:
		random.shuffle(season3)
		print "Episode: %d" % season3[1]
	elif season == 4:
		random.shuffle(season4)
		print "Episode: %d" % season4[1]
	elif season == 5:
		random.shuffle(season5)
		print "Episode: %d" % season5[1]
	elif season == 6:
		random.shuffle(season6)
		print "Episode: %d" % season6[1]
	else:
		random.shuffle(season7)
		print "Episode: %d" % season7[1]

def ENT():
	print "Series: Enterprise"
	seasons = [1, 2, 3, 4]
	season1 = []
	season2 = []
	season3 = []
	season4 = []

	for i in range(1, 25):
		season1.append(i)

	for i in range(1, 26):
		season2.append(i)

	for i in range(1, 24):
		season3.append(i)
	
	for i in range(1, 22):
		season4.append(i)

	random.shuffle(seasons)
	season = seasons[1]
	print "Season: %d" % season

	if season == 1:
		random.shuffle(season1)
		print "Episode: %d" % season1[1]
	elif season == 2:
		random.shuffle(season2)
		print "Episode: %d" % season2[1]
	elif season == 3:
		random.shuffle(season3)
		print "Episode: %d" % season3[1]
	else:
		random.shuffle(season4)
		print "Episode: %d" % season4[1]

def chose_series(choice):
	if series == "TOS":
		TOS()
	elif series == "TAS":
		TAS()
	elif series == "TNG":
		TNG()
	elif series == "DS9":
		DS9()
	elif series == "VOY":
		VOY()
	else:
		ENT()
		
series = raw_input("> TOS, TAS, TNG, DS9, VOY, ENT, or random \n> ")

if series == random:
	random.shuffle(which_series)
	chosen_series = which_series[1]
	chose_series(chosen_series)
else:
	chose_series(series)
