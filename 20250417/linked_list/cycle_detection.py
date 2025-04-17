from linked_list.node import Node


def tortoise_and_hare(root: Node) -> bool:
    if not root.next_node or not root.next_node.next_node:
        return False

    i = root.next_node
    j = i.next_node
    while i != j:
        i = i.next_node
        if not j.next_node or not j.next_node.next_node:
            return False
        j = j.next_node.next_node

    return True


def reverse(root: Node) -> Node:
    cursor = root
    prev_node = None

    while cursor:
        new_prev_node = cursor
        new_cursor = cursor.next_node
        cursor.next_node = prev_node
        cursor = new_cursor
        prev_node = new_prev_node

    return prev_node
