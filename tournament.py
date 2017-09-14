# Maybe change to a pair creator????
def draft(players):
	pair = []
	pair_list = []

	for player in players:
		pair.append(player)
		if len(pair) == 2:
			pair_list.append(pair)
			pair = []

	return pair_list

def file_splitter(file_contents):
	contestants = []

		for line in file_contents:
			name = line.strip()
			contestants.append(name)

		return contestants
		

file_contents = filereader("t-players.txt")
file_splitter(file_contents)
tournament_run(contestants)

def tournament_run(player_info):


