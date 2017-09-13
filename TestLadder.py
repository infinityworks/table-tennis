import unittest

class TestTableTennis(unittest.TestCase):
			
	def test_file_parser():
		file_path = 'names.txt'
		table_tennis = ladder
		parsed_names_list = parse_names_file(file_path)

		self.assertEqual(['dan', 'ivor', 'rebecca', 'john', 'bob', 'rowan'], parsed_names_list)