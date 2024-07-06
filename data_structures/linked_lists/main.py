from typing import Optional 

class SinglyLinkedListNode:
    def __init__(self, value = None, next_node: Optional['SinglyLinkedListNode'] = None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedListManager:
    def __init__(self, head: SinglyLinkedListNode):
        self.head = head

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr
            ptr = ptr.next_node

    def _get_node_to_ptr(self, node = None) -> SinglyLinkedListNode:
        if node == self.head:
            return None
        
        ptr = self.head
        while ptr is not None and ptr.next_node != node:
            ptr = ptr.next_node
        
        return ptr

    def _get_last_node(self) -> SinglyLinkedListNode:
        return self._get_node_to_ptr()

    def add(self, node: SinglyLinkedListNode):
        adder_ptr = self._get_last_node()
        adder_ptr.next_node = node

    def remove_node(self, node: SinglyLinkedListNode):
        if node == self.head:
            self.head = self.head.next
            return
        
        ptr_node = self._get_node_to_ptr(node)
        ptr_node.next_node = node.next_node
        node.next_node = None

    def insert_after(self, position: SinglyLinkedListNode, node: SinglyLinkedListNode):
        node.next_node, position.next_node = position.next_node, node

    def insert_before(self, position: SinglyLinkedListNode, node: SinglyLinkedListNode):
        node_before = _get_node_to_ptr(position)
        
        if node_before is None:
            node.next_node = self.head
            self.head = node
            return
        
        node.next_node, node_before.next_node = position, node
