from unittest import TestCase

from data_structures.stacks.array import Stack


class TestStack(TestCase):

    def test_add(self):
        s = Stack()

        s.add(5)

        assert 5 == s.peek()
    
    def test_remove(self):
        s = Stack()
        s.add(3)

        result = s.remove()

        assert 3 == result
        assert s.peek() is None

    def test_peek(self):
        s = Stack()
        s.add(2)

        result = s.peek()

        assert 2 == result

    def test_peek_empty(self):
        s = Stack()

        result = s.peek()

        assert result is None
