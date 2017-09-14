import unittest
from tournament import draft
from tournament import file_splitter

class tournament_tests(unittest.TestCase):

	def test_splitlistintopairs(self):

		result = draft(["a","b","c","d"])

		self.assertEqual([["a","b"],["c","d"]], result)

	def test_draft_splitnonamesadded(self):

		result = draft([])

		self.assertEqual([], result)

	def test_draft_splitnolistadded(self):

		result = draft("")

		self.assertEqual([],result)

	def test_draft_splittwoplayers(self):

		result = draft(["a","b"])

		self.assertEqual([["a","b"]], result)

	'''
	def test_tournament_draftsplit_addoneplayer(self):

		result = draft(["a"])

		self.assertEqual([["a"]], result)


	def test_tournament_draftsplit_listoddnumbernames(self):

		result = draft(["a","b","c","d","e"])

		self.assertEqual([["a","b"],["c","d"]["e"]], result)


	'''

	
	def test_filesplitter_splitintostrings_inlist(self):

		result = file_splitter("a\nb\nc\nd")

		self.assertEqual(["a","b","c","d"], result)

	def test_filesplitter_splitintostrings_inlist(self):

		result = file_splitter("eggplant\nbins\ncats\ndogs")

		self.assertEqual(["eggplant","bins","cats","dogs"], result)


	#Input [John,Rowan] if John won or [Rowan, John] if John won.

	def test_resulttofile_inputabthenawin(self):

		result = resulttofile(["a,b"])

		self.assertEqual("a", result)


	def test_resulttofile_inputabthenawin(self):

		result = resulttofile(["b,a"])

		self.assertEqual("b", result)

