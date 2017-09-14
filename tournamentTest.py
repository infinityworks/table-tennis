import unittest
import random
import time


# This is the function that will attempt to read files and throw an error if it is unable to do so.
def filereader(file):
	try:
		f = open(file, "r")
		return f
	except IOError:
		print "Sorry old chap, file " + file + " has been lost to the wind."
		exit()

# This is the function that will attempt to edit and append files and throw an error if it is unable to do so.
def fileediter(file):
	try:
		f2 = open(file, "a")
		return f2
	except IOError:
		print "Sorry old chap, file " + file + " has been lost to the wind."
		exit()

#class test(unittest.TestCase):

	#def test_tournament_draftrandomiseplayers_returnrandomisedlist(self):
		#
	#	testTournament = tournament()

		#
	#	result = testTournament.draft([alfonso,ben,clarence,dill])
		#test?
		# The issue here is the random function that is kind of difficult to test.
		#self.assertEqual(result)


class tournament():

	# This method takes in a file that contains seperated player names, it will strip and randomly shuffle the names
	# into pairs and place these into a pair array, it continues to do this until all the players have been selected.
	# (this has not yet been optimized for odd numbered players).
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

	# This method will allow the two players to input their scores and save it to a seperate results text file.
	def player_scores(pair_list):
		winners = []

		for pair in pair_list:
			player_1 = pair[0]
			player_2 = pair[1]
			print "Game between " + player_1 + " and " + player_2
			player_1_score = int(raw_input("Player 1 Score? "))
			player_2_score = int(raw_input("Player 2 Score? "))

			#if player_1_score || player_2_score > 21:
			#	print "You cannot score higher than 21 in this tournament of ping pong"

			#if player_1_score || player_2_score < 0:
			#	print "No one is this bad at ping pong, please input a score"

			scores = fileediter("results.txt")

			if player_1_score < player_2_score:
				winner = player_2
				winners.append(player_2)
			else:
				winner = player_1
				winners.append(player_1)

			scores.write(player_1 + " scored " + str(player_1_score) + " - " + 
				player_2 + " scored " + str(player_2_score) + " on " + time.strftime("%d/%m/%Y") + 
				" at " + time.strftime("%H:%M:%S") + "\n" + "The winner is - " + winner + "\n")
			print winner
		print winners

		return winners

	player_info = filereader("t-players.txt")

	# This will create a randomized arr
	pair_list = draft(player_info)
	player_scores(pair_list)


if __name__ == '__main__':
    unittest.main()










