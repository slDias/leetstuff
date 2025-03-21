from typing import Optional


class Node:

    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def append(self, node):
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = node

    def append_left(self, node: Node):
        self.head, node.next_node = node, self.head

    def remove_node(self, node: Node) -> bool:

        if node == self.head:
            self.head = self.head.next_node
            return True

        node_pre_remove = self.head
        to_remove = self.head.next_node
        while to_remove is not None:
            if to_remove == node:
                break
            node_pre_remove = to_remove
            to_remove = to_remove.next_node
        else:
            return False

        node_pre_remove.next_node = to_remove.next_node
        return True

    def remove_value(self, value) -> Optional[Node]:

        if value == self.head.val:
            result = self.head
            self.head = self.head.next_node
            return result

        pre_current = self.head
        current = self.head.next_node

        while current is not None:
            if current.val == value:
                break
            pre_current = current
            current = current.next_node
        else:
            return

        pre_current.next_node = current.next_node
        return current

    def pop(self) -> Optional[Node]:

        if not self.head:
            return None

        if not self.head.next_node:
            result = self.head
            self.head = None
            return result

        pre_current = self.head
        current = self.head.next_node
        while current.next_node:
            pre_current = current
            current = current.next_node

        pre_current.next_node = None
        return current

    def pop_left(self):
        if not self.head:
            return None

        result = self.head
        self.head = self.head.next_node
        return result


# the code was written entirely by me, I've used AI to write unittests for it and for this review:
# ai review
# Suggestions for Improving the LinkedList Implementation:

# 1. Type Hinting:
#    - Add more type hints to improve code readability and catch potential type-related errors.
#    - Ensure all method parameters and return types are properly annotated.

# 2. Consistency:
#    - In the remove_value method, consider using a flag instead of an else statement after the while loop for consistency with the remove_node method.

# 3. Error Handling:
#    - Add checks for empty list operations where appropriate, especially in methods like remove_value, to avoid potential errors.

# 4. Method for Traversal:
#    - Implement a helper method for traversing the list, which can be reused in methods like append and pop to simplify their logic.

# 5. Additional Methods:
#    - Consider adding a __len__ method to get the length of the list.
#    - Implement a __str__ or __repr__ method for easier debugging and visualization of the list's contents.
