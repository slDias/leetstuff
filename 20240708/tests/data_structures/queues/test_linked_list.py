from unittest import TestCase

from data_structures.queues.linked_list import Queue


class TestQueue(TestCase):

    def test_add(self):
        q = Queue()

        q.add(1)

        assert q.front() == 1

    def test_remove(self):
        q = Queue()
        q.add(1)
        q.add(2)

        q.remove()

        res = q.rear()
        assert res == 1

    def test_front(self):
        q = Queue()
        q.add(2)

        res = q.front()

        assert res == 2

    def test_rear(self):
        q = Queue()
        q.add(2)
        q.add(3)

        res = q.rear()

        assert res == 3

    def test_is_empty_true(self):
        q = Queue()

        res = q.is_empty

        assert res is True

    def test_is_empty_false(self):
        q = Queue()
        q.add(1)

        res = q.is_empty

        assert res is False
