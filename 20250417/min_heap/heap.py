

class MinHeap:

    def __init__(self):
        self._values = []

    def peek(self):
        try:
            return self._values[0]
        except IndexError:
            raise ValueError('heap is empty')

    def add(self, value):
        self._values.append(value)
        self.heapify_up()

    def pop(self):
        if not self._values:
            raise ValueError('heap is empty')
        result = self._values[0]
        if len(self._values) == 1:
            self._values.pop()
            return result
        self._values[0] = self._values.pop()
        self.heapify_down()
        return result

    def heapify_up(self):
        def _heapify_by_index(i):
            i_parent = (i - 1) // 2

            if i_parent < 0:
                return

            if self._values[i_parent] > self._values[i]:
                self._values[i], self._values[i_parent] = self._values[i_parent], self._values[i]
                _heapify_by_index(i_parent)

        return _heapify_by_index(len(self._values) - 1)

    def heapify_down(self):
        def _heapify_by_index(i):
            i_left = 2 * i + 1
            i_right = 2 * i + 2
            smallest_i = i

            try:
                if self._values[i] > self._values[i_left]:
                    smallest_i = i_left

                if self._values[smallest_i] > self._values[i_right]:
                    smallest_i = i_right
            except IndexError:
                pass

            if smallest_i == i:
                return

            self._values[smallest_i], self._values[i] = self._values[i], self._values[smallest_i]
            _heapify_by_index(smallest_i)

        _heapify_by_index(0)