class Table_Tennis_Ladder:

	file = 'names.txt'


	def parse_names_from_file(self,path_to_file):
		players_list = []
		input_file = open(path_to_file, 'r')
		for names in input_file:
			players_list.append(names.strip())
		return players_list

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
		for player in list_of_players:
				if challenger in list_of_players and challengee in list_of_players:
					return True
				else:
					return False
