from typing import Any, Hashable


class Node:
    def __init__(self, key: Any, val: Any, next_node: 'Node' = None) -> None:
        self.val = val
        self.key = key
        self.next_node = next_node

class Hashmap:

    def __init__(self) -> None:
        self.vals = [None] * 10

    def hash_key(self, key: Hashable) -> int:
        # I know this is dumb. but im not interested in writing a hash function right now,
        # just want something that works
        return key % 10 if isinstance(key, int) else int(str(hash(key))[1])

    def add(self, key: Hashable, value: Any) -> None:
        index = self.hash_key(key)

        try:
            result_list_head = self.vals[index]
        except IndexError:
            result_list_head = None

        self.vals[index] = Node(key, value, result_list_head)

    def get(self, key: Hashable) -> Any:
        index = self.hash_key(key)

        try:
            result_list_head = self.vals[index]
        except IndexError:
            result_list_head = None

        result = result_list_head
        while result is not None:
            if result.key == key and type(key) == type(result.key):
                return result.val

            result = result.next_node
        else:
            raise KeyError(key)
