import unittest
from typing import Any

# Assuming the Node and LinkedList classes are defined in a file named linked_list.py
from linked_list.doubly import Node, LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.empty_list = LinkedList()
        self.single_node_list = LinkedList(Node(1))
        self.multi_node_list = LinkedList(Node(1))
        self.multi_node_list.append(Node(2))
        self.multi_node_list.append(Node(3))

    def test_init(self):
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)
        self.assertEqual(self.single_node_list.head.val, 1)
        self.assertIsNone(self.single_node_list.head.prev_node)
        self.assertIsNone(self.single_node_list.head.next_node)

    def test_append(self):
        self.empty_list.append(Node(1))
        self.assertEqual(self.empty_list.head.val, 1)
        self.assertEqual(self.empty_list.tail.val, 1)

        self.single_node_list.append(Node(2))
        self.assertEqual(self.single_node_list.head.val, 1)
        self.assertEqual(self.single_node_list.tail.val, 2)
        self.assertEqual(self.single_node_list.head.next_node.val, 2)
        self.assertEqual(self.single_node_list.tail.prev_node.val, 1)

    def test_append_left(self):
        self.empty_list.append_left(Node(1))
        self.assertEqual(self.empty_list.head.val, 1)

        self.single_node_list.append_left(Node(0))
        self.assertEqual(self.single_node_list.head.val, 0)
        self.assertEqual(self.single_node_list.head.next_node.val, 1)
        self.assertEqual(self.single_node_list.tail.prev_node.val, 0)

    def test_remove_node(self):
        node_to_remove = self.multi_node_list.head.next_node
        self.multi_node_list.remove_node(node_to_remove)
        self.assertEqual(self.multi_node_list.head.next_node.val, 3)
        self.assertEqual(self.multi_node_list.tail.prev_node.val, 1)

    def test_remove_value(self):
        removed = self.multi_node_list.remove_value(2)
        self.assertEqual(removed.val, 2)
        self.assertEqual(self.multi_node_list.head.next_node.val, 3)
        self.assertEqual(self.multi_node_list.tail.prev_node.val, 1)

        removed = self.multi_node_list.remove_value(4)
        self.assertIsNone(removed)

    def test_pop(self):
        popped = self.multi_node_list.pop()
        self.assertEqual(popped.val, 3)
        self.assertEqual(self.multi_node_list.tail.val, 2)
        self.assertIsNone(self.multi_node_list.tail.next_node)

        popped = self.single_node_list.pop()
        self.assertEqual(popped.val, 1)
        self.assertIsNone(self.single_node_list.head)
        self.assertIsNone(self.single_node_list.tail)

    def test_pop_left(self):
        popped = self.multi_node_list.pop_left()
        self.assertEqual(popped.val, 1)
        self.assertEqual(self.multi_node_list.head.val, 2)
        self.assertIsNone(self.multi_node_list.head.prev_node)

        popped = self.single_node_list.pop_left()
        self.assertEqual(popped.val, 1)
        self.assertIsNone(self.single_node_list.head)
        self.assertIsNone(self.single_node_list.tail)

if __name__ == '__main__':
    unittest.main()
