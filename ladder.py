file = 'names.txt'

def parse_names_file(path_to_file):
	input_file = open(path_to_file, 'r')
	for names in path_to_file:
		array_for_writing.append(names.strip())