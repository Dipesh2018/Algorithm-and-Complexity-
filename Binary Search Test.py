#Binary Search test
from binary_search import binary_Search
import unittest

class TestSearch(unittest.TestCase):

	def test_search(self):
		data = [0,1,2,3,4,5,6,7,8,9]
		self.assertEqual (binary_Search(data,4),4)
		self.assertEqual(binary_Search(data,11),False) 

	def test_searchchar(self):
		data = ['a','b','c','d','e','f','g']
		self.assertEqual (binary_Search(data,'a'),0)
		self.assertEqual(binary_Search(data,'h'),False) 
if __name__ == '__main__':
	unittest.main()
