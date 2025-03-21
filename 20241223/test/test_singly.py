#ai generated
import unittest
from typing import Optional

# Assuming the LinkedList and Node classes are defined in a file named linked_list.py
from linked_list.singly import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.empty_list = LinkedList()
        self.single_node_list = LinkedList(Node(1))
        self.multi_node_list = LinkedList(Node(1))
        self.multi_node_list.append(Node(2))
        self.multi_node_list.append(Node(3))
        self.multi_node_list.append(Node(4))  # Added fourth node

    def test_init(self):
        self.assertIsNone(self.empty_list.head)
        self.assertEqual(self.single_node_list.head.val, 1)
        self.assertIsNone(self.single_node_list.head.next_node)

    def test_append(self):
        self.empty_list.append(Node(1))
        self.assertEqual(self.empty_list.head.val, 1)

        self.single_node_list.append(Node(2))
        self.assertEqual(self.single_node_list.head.next_node.val, 2)

        self.multi_node_list.append(Node(5))
        current = self.multi_node_list.head
        values = []
        while current:
            values.append(current.val)
            current = current.next_node
        self.assertEqual(values, [1, 2, 3, 4, 5])

    def test_append_left(self):
        self.empty_list.append_left(Node(1))
        self.assertEqual(self.empty_list.head.val, 1)

        self.single_node_list.append_left(Node(0))
        self.assertEqual(self.single_node_list.head.val, 0)
        self.assertEqual(self.single_node_list.head.next_node.val, 1)

        self.multi_node_list.append_left(Node(0))
        self.assertEqual(self.multi_node_list.head.val, 0)
        self.assertEqual(self.multi_node_list.head.next_node.val, 1)

    def test_remove_node(self):
        node_to_remove = self.multi_node_list.head.next_node.next_node
        self.multi_node_list.remove_node(node_to_remove)
        self.assertEqual(self.multi_node_list.head.next_node.next_node.val, 4)

        self.multi_node_list.remove_node(self.multi_node_list.head)
        self.assertEqual(self.multi_node_list.head.val, 2)

    def test_remove_value(self):
        removed_node = self.multi_node_list.remove_value(2)
        self.assertEqual(removed_node.val, 2)
        self.assertEqual(self.multi_node_list.head.next_node.val, 3)

        removed_node = self.multi_node_list.remove_value(1)
        self.assertEqual(removed_node.val, 1)
        self.assertEqual(self.multi_node_list.head.val, 3)

        removed_node = self.multi_node_list.remove_value(5)
        self.assertIsNone(removed_node)

    def test_pop(self):
        popped_node = self.multi_node_list.pop()
        self.assertEqual(popped_node.val, 4)
        self.assertEqual(self.multi_node_list.head.next_node.next_node.val, 3)
        self.assertIsNone(self.multi_node_list.head.next_node.next_node.next_node)

        popped_node = self.single_node_list.pop()
        self.assertEqual(popped_node.val, 1)
        self.assertIsNone(self.single_node_list.head)

        popped_node = self.empty_list.pop()
        self.assertIsNone(popped_node)

    def test_pop_left(self):
        popped_node = self.multi_node_list.pop_left()
        self.assertEqual(popped_node.val, 1)
        self.assertEqual(self.multi_node_list.head.val, 2)

        popped_node = self.single_node_list.pop_left()
        self.assertEqual(popped_node.val, 1)
        self.assertIsNone(self.single_node_list.head)

        popped_node = self.empty_list.pop_left()
        self.assertIsNone(popped_node)

if __name__ == '__main__':
    unittest.main()
