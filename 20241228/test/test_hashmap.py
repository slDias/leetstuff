import unittest

# Assuming the Hashmap class is defined in a file named hashmap.py
from hashmap import Hashmap


class TestHashmap(unittest.TestCase):

    def setUp(self):
        self.hashmap = Hashmap()

    def test_add_and_get_single_item(self):
        self.hashmap.add("key1", "value1")
        self.assertEqual(self.hashmap.get("key1"), "value1")

    def test_add_and_get_multiple_items(self):
        self.hashmap.add("key1", "value1")
        self.hashmap.add("key2", "value2")
        self.hashmap.add("key3", "value3")
        self.assertEqual(self.hashmap.get("key1"), "value1")
        self.assertEqual(self.hashmap.get("key2"), "value2")
        self.assertEqual(self.hashmap.get("key3"), "value3")

    def test_get_nonexistent_key(self):
        with self.assertRaises(KeyError):
            self.hashmap.get("nonexistent_key")

    def test_overwrite_existing_key(self):
        self.hashmap.add("key1", "value1")
        self.hashmap.add("key1", "new_value1")
        self.assertEqual(self.hashmap.get("key1"), "new_value1")

    def test_add_and_get_different_types(self):
        self.hashmap.add(1, "int_key")
        self.hashmap.add(3.14, "float_key")
        self.hashmap.add(True, "bool_key")
        self.hashmap.add((1, 2), "tuple_key")

        self.assertEqual(self.hashmap.get(1), "int_key")
        self.assertEqual(self.hashmap.get(3.14), "float_key")
        self.assertEqual(self.hashmap.get(True), "bool_key")
        self.assertEqual(self.hashmap.get((1, 2)), "tuple_key")

    def test_collision_handling(self):
        # This test assumes that the hash function might produce collisions
        # We'll add multiple items and ensure they can all be retrieved correctly
        for i in range(20):
            self.hashmap.add(f"key{i}", f"value{i}")

        for i in range(20):
            self.assertEqual(self.hashmap.get(f"key{i}"), f"value{i}")


if __name__ == '__main__':
    unittest.main()
