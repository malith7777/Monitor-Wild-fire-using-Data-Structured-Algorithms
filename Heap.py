class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    
    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


class DSAHeap:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
        self._bubble_up(len(self.data) - 1)

    def pop(self):
        if self.is_empty():
            return None

        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._bubble_down(0)
        return item

    def is_empty(self):
        return len(self.data) == 0

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _bubble_up(self, index):
        parent_index = self._parent(index)
        while index > 0 and self.data[parent_index] > self.data[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(index)

    def _bubble_down(self, index):
        while True:
            left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)
            smallest_child_index = index

            if (left_child_index < len(self.data) and
                self.data[left_child_index] < self.data[smallest_child_index]):
                smallest_child_index = left_child_index

            if (right_child_index < len(self.data) and
                self.data[right_child_index] < self.data[smallest_child_index]):
                smallest_child_index = right_child_index

            if smallest_child_index == index:
                break

            self._swap(index, smallest_child_index)
            index = smallest_child_index

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

