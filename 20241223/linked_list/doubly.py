from typing import Any


class Node:
    def __init__(self, val: Any = None, prev_node: "Node" = None, next_node: "Node" = None):
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node

class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head
        self.tail = head
        while self.tail and self.tail.next_node is not None:
            self.tail = self.tail.next_node

    def append(self, node: Node) -> None:
        current = self.tail

        if current is None:
            self.head = node
            self.tail = node
            return None

        current.next_node = node
        node.prev_node = current
        self.tail = node

    def append_left(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
            return None

        prev_head = self.head
        node.next_node = prev_head
        node.prev_node = None
        prev_head.prev_node = node
        self.head = node

    def remove_node(self, node: Node) -> None:
        if node == self.head:
            self.head = self.head.next_node
            self.head.prev_node = None
            return None

        if node == self.tail:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return None

        prev_node = node.prev_node
        next_node = node.next_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node

    def remove_value(self, value: Any) -> Node | None:
        if not self.head:
            return None

        if self.head.val == value:
            removed = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            removed.next_node = None
            return removed

        if self.tail.val == value:
            removed = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            removed.prev_node = None
            return removed

        current = self.head.next_node
        while current is not None:
            if current.val == value:
                current.prev_node.next_node = current.next_node
                current.next_node.prev_node = current.prev_node
                return current

            current = current.next_node

        return None

    def pop(self) -> Node | None:
        last_node = self.tail
        if last_node is None:
            return None

        if last_node == self.head:
            self.head = None
            self.tail = None
        else:
            pre_last_node = last_node.prev_node
            pre_last_node.next_node = None
            self.tail = pre_last_node
            last_node.prev_node = None

        return last_node

    def pop_left(self) -> Node | None:
        if not self.head:
            return None

        result = self.head
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        else:
            self.tail = None

        result.next_node = None
        return result


#In the remove_value method:

    #If the head node is removed and it's the only node, the tail is not updated to None.
    #If the removed node is in the middle of the list, its prev_node and next_node references are not cleared.
