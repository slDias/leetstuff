import unittest
from heap.min_heap import MinHeap


class TestMinHeap(unittest.TestCase):

    def test_init(self):
        heap = MinHeap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.assertEqual(len(heap.vals), 11)
        self.assertLessEqual(heap.vals[0], heap.vals[1])
        self.assertLessEqual(heap.vals[0], heap.vals[2])

    def test_init_single_element(self):
        heap = MinHeap([])
        self.assertEqual(len(heap.vals), 0)

    def test_swap(self):
        heap = MinHeap([1, 2, 3])
        heap.swap(0, 2)
        self.assertEqual(heap.vals, [3, 2, 1])

    def test_heapify_up(self):
        heap = MinHeap([3, 2, 1])
        heap.heapify_up(2)
        self.assertEqual(heap.vals[0], 1)

    def test_heapify_down(self):
        heap = MinHeap([3, 1, 2])
        heap.heapify_down()
        self.assertEqual(heap.vals[0], 1)

    def test_peek(self):
        heap = MinHeap([1, 2, 3])
        self.assertEqual(heap.peek(), 1)
        self.assertEqual(len(heap.vals), 3)  # Ensure peek doesn't remove the element

    def test_is_empty(self):
        heap = MinHeap([])
        self.assertTrue(heap.is_empty())
        heap.add(1)
        self.assertFalse(heap.is_empty())

    def test_pop(self):
        heap = MinHeap([1, 2, 3])
        min_val = heap.pop()
        self.assertEqual(min_val, 1)
        self.assertEqual(len(heap.vals), 2)
        self.assertLessEqual(heap.vals[0], heap.vals[1])

    def test_add(self):
        heap = MinHeap([2, 3, 4])
        heap.add(1)
        self.assertEqual(heap.vals[0], 1)
        self.assertEqual(len(heap.vals), 4)

    def test_repr(self):
        heap = MinHeap([1, 2, 3])
        self.assertEqual(repr(heap), "MinHeap<1,2,3>")

    def test_empty_heap(self):
        heap = MinHeap([])
        self.assertEqual(len(heap.vals), 0)

    def test_single_element_heap(self):
        heap = MinHeap([1])
        self.assertEqual(len(heap.vals), 1)
        self.assertEqual(heap.vals[0], 1)

    def test_add_multiple_elements(self):
        heap = MinHeap([])
        for i in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]:
            heap.add(i)
        self.assertEqual(len(heap.vals), 11)
        self.assertLessEqual(heap.vals[0], heap.vals[1])
        self.assertLessEqual(heap.vals[0], heap.vals[2])

    def test_pop_all_elements(self):
        original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        heap = MinHeap(original)
        popped = []
        for element in heap:
            popped.append(element)

        self.assertEqual(len(popped), len(original))
        for i in range(1, len(popped)):
            self.assertLessEqual(popped[i - 1], popped[i])
        self.assertEqual(sorted(popped), sorted(original))


if __name__ == '__main__':
    unittest.main()
