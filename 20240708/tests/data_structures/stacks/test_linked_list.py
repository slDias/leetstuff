from unittest import TestCase

from data_structures.stacks.linked_list import Stack

class TestStack(TestCase):

    def test_add_element(self):
        s = Stack()

        s.push(1)

        assert s.peek() == 1
    
    def test_peek_empty(self):
        s = Stack()

        with self.assertRaises(ValueError):
            s.peek()

    def test_peek_value(self):
        s = Stack()
        s.push(2)

        res = s.peek()

        assert res == 2

    def test_pop_empty(self):
        s = Stack()

        with self.assertRaises(ValueError):
            s.pop()

    def test_pop(self):
        s = Stack()
        s.push(3)

        res = s.pop()

        assert res == 3
        assert s.is_empty is True

# todo do an array one
