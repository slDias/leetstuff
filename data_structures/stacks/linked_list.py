from data_structures.linked_lists import SinglyLinkedListNode, SinglyLinkedListManager


class Stack:

    def __init__(self):
        self.linked_list = SinglyLinkedListManager()
        self._top_ptr = None

    def push(self, value):
        new_node = SinglyLinkedListNode(value)

        if self.is_empty:
            self._top_ptr = new_node
            self.linked_list.add(self._top_ptr)
            return
        
        self.linked_list.insert_before(self._top_ptr, new_node)
    
    def peek(self):
        if self.is_empty:
            raise ValueError("Stack is empty")
        
        return self._top_ptr.value
    
    def pop(self):
        if self.is_empty:
            raise ValueError("Stack is empty")
        
        tmp = self._top_ptr.next_node
        val = self._top_ptr.value
        self.linked_list.remove_node(self._top_ptr)
        self._top_ptr = tmp

        return val

    @property
    def is_empty(self):
        return self._top_ptr is None
