import unittest
from ladder import Table_Tennis_Ladder

class TestTableTennis(unittest.TestCase):

	def test_file_parser_Should_return_list_with_names(self):
		file_path = 'names.txt'
		ladder = Table_Tennis_Ladder()
		parsed_names_list = ladder.parse_names_file(file_path)
		self.assertEqual(['dan', 'ivor', 'rebecca', 'rowan', 'john', 'bob'], parsed_names_list)
			


if __name__ == '__main__':
    unittest.main()