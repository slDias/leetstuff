


class Node:

    def __init__(self, value: int = None, next_node: 'Node' = None, prev_node: 'Node' = None) -> None:
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def append_right(self, new_node: 'Node') -> None:
        return self.append(new_node)

    def append(self, new_node: 'Node') -> None:
        self.next_node = new_node

    def append_left(self, new_node: 'Node') -> None:
        self.prev_node = new_node

    def remove(self) -> 'Node':
        result = self.next_node
        self.next_node = None
        return result

    def remove_left(self) -> 'Node':
        result = self.prev_node
        self.prev_node = None
        return result
