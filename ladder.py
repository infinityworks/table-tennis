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

	def tournament():
		# manual input of the challenger and challengee 
		challenger = raw_input('Who was the successful challenger? ').lower()
		challengee = raw_input('Who was the unsuccessful challengee? ').lower()

		# player_a is the lower ranked challenger and player_b is the higher ranked challengee
		# determines index of challenger and challengee in the list
		player_a = player_list.index(challenger)
		player_b = player_list.index(challengee)

	def new_list_of_players(self, player_list, player_a, player_b):
		top  = player_list[:player_b]
		winner = player_list[player_a]
		middle = player_list[player_b:player_a]
		bottom = player_list[player_a + 1:]

		# make winner a list instead of a string then concatenate the four lists
		new_player_list = top + [winner] + middle + bottom

		return new_player_list