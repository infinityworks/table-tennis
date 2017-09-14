# Maybe change to a pair creator????
def create_pairs(contestants):
	pair = []
	pair_list = []

	for player in contestants:
		pair.append(player)
		if len(pair) == 2:
			pair_list.append(pair)
			pair = []

	return pair_list


def file_splitter(file_contents):
	contestants = file_contents.split("\n")
	return contestants

# This is the function that will attempt to read files and throw an error if it is unable to do so.
def filereader(file):
	try:
		f = open(file, "r")
		return f
	except IOError:
		print "Unfortunately the file " + file + " could not be opened, please try again"
		exit()	



#file_contents = filereader("t-players.txt")
#file_splitter(file_contents)
#tournament_run(contestants)

#def tournament_run(player_info):


