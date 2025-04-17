import pytest

from .heap import MinHeap

def test_add_and_peek():
    heap = MinHeap()
    heap.add(5)
    assert heap.peek() == 5
    heap.add(3)
    assert heap.peek() == 3
    heap.add(8)
    assert heap.peek() == 3
    heap.add(1)
    assert heap.peek() == 1


def test_pop():
    heap = MinHeap()
    heap.add(5)
    heap.add(3)
    heap.add(8)
    heap.add(1)

    assert heap.pop() == 1
    assert heap.peek() == 3
    assert heap.pop() == 3
    assert heap.peek() == 5
    assert heap.pop() == 5
    assert heap.peek() == 8
    assert heap.pop() == 8


def test_pop_empty_heap():
    heap = MinHeap()
    with pytest.raises(ValueError):
        heap.pop()


def test_peek_empty_heap():
    heap = MinHeap()
    with pytest.raises(ValueError):
        heap.peek()


def test_add_multiple_elements():
    heap = MinHeap()
    elements = [10, 4, 5, 6, 2, 1, 3]
    for el in elements:
        heap.add(el)

    sorted_elements = sorted(elements)
    for el in sorted_elements:
        assert heap.pop() == el