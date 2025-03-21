from data_structures.linked_lists import SinglyLinkedListNode, SinglyLinkedListManager


class Queue:

    def __init__(self):
        self.linked_list = SinglyLinkedListManager()
        self.front_ptr = None
        self.rear_prt = None

    def add(self, value):
        value_node = SinglyLinkedListNode(value)
        
        if self.front_ptr is None:
            self.front_ptr = value_node
            self.rear_prt = value_node
            self.linked_list.add(value_node)
            return
        
        self.linked_list.insert_after(self.rear_prt, value_node)
        self.rear_prt = self.rear_prt.next_node

    def remove(self):
        # as of now, this is o(n). but can be fixed
        self.rear_prt = self.linked_list.remove_node(self.rear_prt)

    def front(self):
        return self.front_ptr and self.front_ptr.value

    def rear(self):
        return self.rear_prt and self.rear_prt.value

    @property
    def is_empty(self):
        return self.front_ptr is None
