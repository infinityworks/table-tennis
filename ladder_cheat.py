# list of known competitors
input_file = open('names.txt', 'r')

# list where names from input will be added
player_list = []

# appends names from input into list created 
for names in input_file:
	player_list.append(names.strip())

# manual input of the challenger and challengee 
challenger = raw_input('Who was the successful challenger? ')
challengee = raw_input('Who was the unsuccessful challengee? ')

# player_a is the lower ranked challenger and player_b is the higher ranked challengee
# determines index of challenger and challengee in the list
player_a = player_list.index(challenger)
player_b = player_list.index(challengee)

# creates the splices for the 4 general cases: top = players ranked higher than challengee, winner = the challenger, middle = the challengee down to the rank of the challenger initially
# bottom = the players that were ranked lower than the challenger
top  = player_list[:player_b]
winner = player_list[player_a]
middle = player_list[player_b:player_a]
bottom = player_list[player_a + 1:]

# make winner a list instead of a string then concatenate the four lists
new_player_list = top + [winner] + middle + bottom


output_file = open('latest_rankings.txt', 'w')
output_file.write("{}\n".format(new_player_list))