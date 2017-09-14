import unittest
from ladder import Table_Tennis_Ladder

class TestTableTennis(unittest.TestCase):

	def test_file_parser_Should_return_list_with_names(self):
		file_path = 'names.txt'
		ladder = Table_Tennis_Ladder()
		parsed_names_list = ladder.parse_names_from_file(file_path)
		self.assertEqual(['dan', 'ivor', 'rebecca', 'rowan', 'john', 'bob'], parsed_names_list)
			
	def test_parsed_file_Should_write_to_file(self):
		file_path = 'test_write.txt'
		names_list = ['dan', 'ivor', 'rebecca', 'rowan', 'john', 'bob']
		ladder = Table_Tennis_Ladder()
		new_names_list = ladder.write_names_from_list_to_file(file_path, names_list)

		input_file = open(file_path, 'r')
		return_names_list = []
		for names in input_file:
			return_names_list.append(names)

		self.assertEqual(['dan\n', 'ivor\n', 'rebecca\n', 'rowan\n', 'john\n', 'bob\n'], return_names_list)

if __name__ == '__main__':
    unittest.main()