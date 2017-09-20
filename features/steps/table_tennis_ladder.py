class Table_Tennis_Ladder:

	file = 'names.txt'

	'''
	def parse_names_from_file(self,path_to_file):
		players_list = []
		try:
			input_file = open(path_to_file, 'r')
			for names in input_file:
				players_list.append(names.strip())
		except IOError:
			print file + " doesn't exist."
			exit()
		
		return players_list
	'''
	def write_names_from_list_to_file(self,path_to_file,names_list):
		output_file = open(path_to_file, 'w')

		# each player in reordered list added back into
		for name in names_list:
			output_file.write("{}\n".format(name))

	def reorder_list_of_players(self, list_of_players, challenger, challengee):

		player_a = list_of_players.index(challenger)
		player_b = list_of_players.index(challengee)


		top  = list_of_players[:player_b]
		winner = list_of_players[player_a]
		middle = list_of_players[player_b:player_a]
		bottom = list_of_players[player_a + 1:]
		reordered_player_list = top + [winner] + middle + bottom

		return reordered_player_list

	def defining_the_challenger_and_challengee(self, list_of_players, challenger, challengee):
		if challenger in list_of_players and challengee in list_of_players:
			return True
		else:
			return False

	def is_Challenger_Lower_Rank(self, list_of_players, challenger, challengee):
		if list_of_players.index(challenger) > list_of_players.index(challengee):
			return True
		else:
			return False

	def input_result(self, ladder_list, challenger, challengee):

		if self.is_Challenger_Lower_Rank(ladder_list, challenger, challengee) and self.defining_the_challenger_and_challengee(ladder_list, challenger, challengee):
			return self.reorder_list_of_players(ladder_list, challenger, challengee)
		else:
			return ladder_list
			

		


# 	def main(self):
#
# 		ladder_list = self.parse_names_from_file(file)
# 		challenger = raw_input('Who was the successful challenger? ').lower()
# 		challengee = raw_input('Who was the unsuccessful challengee? ').lower()
#
# 		while exists:
# 			if self.is_Challenger_Lower_Rank(ladder_list, challenger, challengee) and self.defining_the_challenger_and_challengee(ladder_list, challenger, challengee):
# 				self.reorder_list_of_players(ladder_list, challenger, challengee)
# 				self.write_names_from_list_to_file(file)
# 				print "Players have been rearranged" + self.parse_names_from_file(file)
# 				exists = False
# 			else:
# 				print "Challenger or Challengee doesn't exist"
# 				exists = True
#
#
#
# if __name__ == '__main__':
# 	Table_Tennis_Ladder().main()
