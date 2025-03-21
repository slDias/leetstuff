from typing import Iterable, Any

# code is mine, comments are an AI review

class MinHeap:

    def __init__(self, vals: Iterable[Any]) -> None:
        self.vals = list(vals)
        for node_index in range((len(self.vals) // 2) - 1, -1, -1):
            self.heapify_down(node_index)
        # Good: Correct implementation of bottom-up heap construction
        # Improvement: Consider renaming heapify_down to _sift_down for clarity

    def swap(self, index_a, index_b) -> None:
        self.vals[index_a], self.vals[index_b] = self.vals[index_b], self.vals[index_a]
        # Good: Simple and effective swap method

    def heapify_up(self, target_index: int) -> None:
        if target_index == 0:
            return None

        parent_index = (target_index - 1) // 2

        if self.vals[target_index] < self.vals[parent_index]:
            self.swap(target_index, parent_index)
            return self.heapify_up(parent_index)
        # Good: Correct implementation of heapify_up
        # Improvement: Consider using an iterative approach for better performance

    def heapify_down(self, target_index: int = 0) -> None:
        left_index = target_index * 2 + 1
        right_index = target_index * 2 + 2

        smallest_index = left_index

        try:
            if self.vals[right_index] < self.vals[left_index]:
                smallest_index = right_index
        except IndexError:
            if len(self.vals) - 1 < left_index:
                return None

        if self.vals[smallest_index] < self.vals[target_index]:
            self.swap(smallest_index, target_index)
            return self.heapify_down(smallest_index)
        # Improvement: Replace try-except with explicit bounds checking
        # Improvement: Consider using an iterative approach for better performance

    def peek(self) -> Any:
        return self.vals[0]
        # Good: Simple peek implementation
        # Improvement: Add error handling for empty heap

    def is_empty(self) -> bool:
        return not self.vals
        # Good: Concise implementation

    def pop(self) -> Any:
        result = self.vals.pop(0)
        self.heapify_down()
        return result
        # Improvement: pop(0) is O(n), consider swapping with last element and then heapify_down

    def add(self, val: Any) -> None:
        self.vals.append(val)
        self.heapify_up(len(self.vals) - 1)
        # Good: Correct implementation of add method

    def __repr__(self) -> str:
        return f'MinHeap<{",".join([str(x) for x in self.vals])}>'
        # Good: Clear string representation

    def __iter__(self):
        while not self.is_empty():
            yield self.pop()
        # Good: Efficient iterator implementation using generator
