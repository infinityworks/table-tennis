import unittest
from tournament import create_pairs
from tournament import file_splitter
from tournament import find_winner
from tournament import inputarg

class tournament_tests(unittest.TestCase):

#inputarg tests

	def test_inputarg_incorrectcommand_invalidmessage(self):

		result = inputarg(['tournament.py', 'dog'])

		self.assertEqual("please enter one of the following arguments: init", result)
	
	def test_inputarg_initcommand_okmessage(self):

		result = inputarg(['tournament.py', 'init'])

		self.assertEqual("ok", result)



#Function Tests
    
	def test_filesplitter_splitintostrings_inlist(self):

		result = file_splitter("a\nb\nc\nd")

		self.assertEqual(["a","b","c","d"], result)

	def test_filesplitter_splitintostrings_wordsinlist(self):

		result = file_splitter("eggplant\nbins\ncats\ndogs")

		self.assertEqual(["eggplant","bins","cats","dogs"], result)

	def test_splitlistintopairs(self):

		result = create_pairs(["a","b","c","d"])

		self.assertEqual([["a","b"],["c","d"]], result)

	def test_create_pairs_splitnonamesadded(self):

		result = create_pairs([])

		self.assertEqual([], result)

	def test_create_pairs_splitnolistadded(self):

		result = create_pairs("")

		self.assertEqual([],result)

	def test_create_pairs_splittwoplayers(self):

		result = create_pairs(["a","b"])

		self.assertEqual([["a","b"]], result)

	def test_findwinner_addwinnername(self):

		result = find_winner(["a","b"], "a")

		self.assertEqual("a", result)

	def test_findwinner_nonplayingname(self):

		result = find_winner(["a","b"], "c")

		self.assertEqual("Didn't Play", result)

	def test_generatetree_createtree(self):

		result = generate_tree(["a","b"],["c","d"])


'''
	def test_tournament_draftsplit_addoneplayer(self):

		result = create_pairs(["a"])

		self.assertEqual([["a"]], result)


	def test_tournament_draftsplit_listoddnumbernames(self):

		result = create_pairs(["a","b","c","d","e"])

		self.assertEqual([["a","b"],["c","d"]["e"]], result)


	#Input [John,Rowan] if John won or [Rowan, John] if John won.


	def test_resulttofile_inputabthenawin(self):

		result = resulttofile(["a","b"])

		self.assertEqual("a", result)


	def test_resulttofile_inputabthenawin(self):

		result = resulttofile(["b,a"])

		self.assertEqual("b", result)
'''




