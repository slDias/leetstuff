import random

from .cycle_detection import tortoise_and_hare, reverse
from .node import Node


def test_init():
    expected_value = random.randint(1, 10)
    expected_next = Node(2)
    expected_prev = Node(3)

    node = Node(expected_value, expected_next, expected_prev)

    assert node.value == expected_value
    assert node.next_node == expected_next
    assert node.prev_node == expected_prev


def test_append():
    expected_node = Node(2)
    root_node = Node(1)

    root_node.append(expected_node)

    assert root_node.next_node == expected_node


def test_append_left():
    expected_node = Node(2)
    root_node = Node(1)

    root_node.append_left(expected_node)

    assert root_node.prev_node == expected_node


def test_append_right():
    expected_node = Node(2)
    root_node = Node(1)

    root_node.append_right(expected_node)

    assert root_node.next_node == expected_node


def test_remove():
    expected_node = Node(2)
    node = Node(1, next_node=expected_node)

    result = node.remove()

    assert node.next_node is None
    assert result == expected_node


def test_remove_left():
    expected_node = Node(2)
    node = Node(1, prev_node=expected_node)

    result = node.remove_left()

    assert node.prev_node is None
    assert result == expected_node


def test_has_cycle():
    root = Node(0)
    last_node = root
    cursor = root
    for v in range(100_000):
        last_node = Node(v)
        cursor.append(last_node)
        cursor = last_node
    last_node.append(root)

    res = tortoise_and_hare(root)

    assert res is True

def test_has_no_cycle():
    root = Node(0)
    cursor = root
    for v in range(100_000):
        cursor.append(Node(v))
        cursor = cursor.next_node

    res = tortoise_and_hare(root)

    assert res is False


def test_reverse():
    root = Node(0)
    last = root
    cursor = root
    for v in range(100_000):
        last = Node(v)
        cursor.append(last)
        cursor = cursor.next_node

    res = reverse(root)

    assert res == last
    cursor = res
    for v in range(99_999, 0, -1):
        assert cursor.value == v
        cursor = cursor.next_node

