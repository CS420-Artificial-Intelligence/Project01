import algorithm.search_ds.search_ds as search_ds
import algorithm.state as state

class PriorityQueue(search_ds.SearchDataStructure):
    def __init__(self):
        self.queue = []
    def pop(self):
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        value = self.queue.pop()
        idx = 0
        while idx < len(self.queue):
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left >= len(self.queue):
                break
            if right >= len(self.queue):
                if self.queue[left].f() < self.queue[idx].f():
                    self.queue[left], self.queue[idx] = self.queue[idx], self.queue[left]
                    idx = left
                else:
                    break
            else:
                if self.queue[left].f() < self.queue[right].f():
                    if self.queue[left].f() < self.queue[idx].f():
                        self.queue[left], self.queue[idx] = self.queue[idx], self.queue[left]
                        idx = left
                    else:
                        break
                else:
                    if self.queue[right].f() < self.queue[idx].f():
                        self.queue[right], self.queue[idx] = self.queue[idx], self.queue[right]
                        idx = right
                    else:
                        break
        return value
    def push(self, item: state.State):
        self.queue.append(item)
        idx = len(self.queue) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.queue[parent].f() > self.queue[idx].f():
                self.queue[parent], self.queue[idx] = self.queue[idx], self.queue[parent]
                idx = parent
            else:
                break
    def clear(self):
        self.queue.clear()
    def is_empty(self):
        return len(self.queue) == 0