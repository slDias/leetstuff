import unittest

from arrays.selection_sort import main


class TestSelectionSort(unittest.TestCase):
    def test_main(self):
        result = main([4, 3, 2, 1])
        assert [1, 2, 3, 4] == result

if __name__ == '__main__':
    unittest.main()
