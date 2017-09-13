class Table_Tennis_Ladder:

	file = 'names.txt'

	def __init__(self):
		pass

	def parse_names_file(self,path_to_file):
		players_list = []
		input_file = open(path_to_file, 'r')
		for names in input_file:
			players_list.append(names.strip())
		return players_list

	