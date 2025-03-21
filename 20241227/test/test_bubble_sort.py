import unittest

from arrays.bubble_sort import main


class TestBubbleSort(unittest.TestCase):

    def test_something(self):
        assert [1, 2, 3] == main([3, 2, 1])
        print(main([3, 2, 1]))
        print(main([1, 2, 3]))