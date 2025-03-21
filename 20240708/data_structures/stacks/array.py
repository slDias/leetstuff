class Stack:

    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)

    def remove(self):
        if self._data:
            return self._data.pop()

        return None

    def peek(self):
        if self._data:
            return self._data[-1]

        return None