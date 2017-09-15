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

	def test_reorder_list_of_players_Should_Move_Up_One_Space(self):
		players_list = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		reordered_player_list = ladder.reorder_list_of_players(players_list,"c", "b")

		self.assertEqual(['a', 'c', 'b'], reordered_player_list)

	def test_reorder_list_of_players_Should_Move_To_The_Top(self):
		players_list = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		reordered_player_list = ladder.reorder_list_of_players(players_list,"c", "a")

		self.assertEqual(['c', 'a', 'b'], reordered_player_list)

	def test_reorder_list_of_players_Should_Move_From_Middle_To_Top(self):
		players_list = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		reordered_player_list = ladder.reorder_list_of_players(players_list,"b", "a")

		self.assertEqual(['b', 'a', 'c'], reordered_player_list)

	def test_reorder_list_of_players_Only_Two_Players_Should_Swap(self):
		players_list = ['a', 'b']
		ladder = Table_Tennis_Ladder()
		reordered_player_list = ladder.reorder_list_of_players(players_list,"b", "a")

		self.assertEqual(['b', 'a'], reordered_player_list)

	def test_reorder_list_of_players_Checking_Multiple_Players_In_List(self):
		players_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
		ladder = Table_Tennis_Ladder()
		reordered_player_list = ladder.reorder_list_of_players(players_list,"h", "c")

		self.assertEqual(['a', 'b', 'h', 'c', 'd', 'e', 'f', 'g', 'i', 'j'], reordered_player_list)

	def test_defining_the_challenger_and_challengee_Should_Return_Valid_Users(self):
		player_names = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		self.assertTrue(ladder.defining_the_challenger_and_challengee(player_names, "a", "b"))

	def test_is_Challenger_Lower_Rank_Should_Return_True(self):
		player_names = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		self.assertTrue(ladder.is_Challenger_Lower_Rank(player_names, "c", "a"))

	def test_is_Challenger_Lower_Rank_Should_Return_False(self):
		player_names = ['a', 'b', 'c']
		ladder = Table_Tennis_Ladder()
		self.assertFalse(ladder.is_Challenger_Lower_Rank(player_names, "a", "c"))

if __name__ == '__main__':
    unittest.main()