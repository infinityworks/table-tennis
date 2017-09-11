import random
import date

def filereader(file):
	try:
		f = open(file, "r")
		return f
	except IOError:
		print "Sorry old chap, file " + file + " has been lost to the wind."
		exit()

def fileediter(file):
	try:
		f2 = open(file, "a")
		return f2
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
	return pair_list

def player_scores(pair_list):

	for pair in pair_list:
		player_1 = pair[0]
		player_2 = pair[1]
		print "Game between " + player_1 + " and " + player_2
		player_1_score = raw_input("Player 1 Score? ")
		player_2_score = raw_input("Player 2 Score? ")
		scores = fileediter("results.txt")
		scores.write(player_1 + " scored " + player_1_score + " - " + player_2 + " scored " + player_2_score)


player_info = filereader("t-players.txt")

# This will create a randomized arr
pair_list = draft(player_info)
player_scores(pair_list)
