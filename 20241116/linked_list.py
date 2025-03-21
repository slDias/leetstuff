class Node:
    value = None
    next_ptr = None

    def __init__(self, value, next_ptr=None):
        self.next_ptr = next_ptr
        self.value = value

    def __next__(self):
        return self.next_ptr


class LinkedList:
    head: Node = None

    def insert_head(self, value):
        new_head = Node(value)

        if self.head is not None:
            new_head.next_ptr = self.head

        self.head = new_head

    def insert_tail(self, value):
        new_tail = Node(value)

        current = self.head
        while current.next_ptr is not None:
            current = next(current)

        current.next_ptr = new_tail