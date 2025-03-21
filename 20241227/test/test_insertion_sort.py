import unittest

from arrays.insertion_sort import main

class TestInsertionSort(unittest.TestCase):
    def test_main(self):
        main(list(range(100, 0, -1)))

if __name__ == '__main__':
    unittest.main()
