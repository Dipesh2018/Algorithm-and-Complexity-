import random
from search import linear_search
from time import time_ns
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
data = random.sample(range(10000000), 10000000)
start = time_ns()
index = linear_search(data, data[-1])
end = time_ns()
elapsed = end - start

print(elapsed)

# Search Test
import unittest
from search import linear_search

class TestSearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 5, 6, 12, 7, 4, 8]
        self.assertEqual(linear_search(data, 6), 4)
        self.assertEqual(linear_search(data, 10),  -1)

    def test_searchChar(self):
        data = ['t', 'a', 'b', 'l', 'e']
        self.assertEqual(linear_search(data, 'a'), 1)


if __name__ == "__main__":
    unittest.main()
    
