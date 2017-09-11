import random

def filereader(file):
	try:
		f = open(file, "r")
		return f
	except IOError:
		print "Sorry old chap, file " + file + " has been lost to the wind."
		exit()

def draft(player_info):
	players = []

	for line in player_info:
		name = line.strip()
		players.append(name)

	random.shuffle(players)
	print players

	pair = []
	pair_list = []

	for player in players:
		if len(pair) < 2:
			pair.append(player)
			#print "player added" + str(player)
			#print "the pair is " + str(pair)
			if len(pair) == 2:
				pair_list.append(pair)
				pair = []
				#print pair
				#print "pair appended" + str(pair_list)

	print pair_list

player_info = filereader("t-players.txt")

# This will create a randomized arr
draft(player_info)
