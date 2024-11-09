import algorithm.search_ds.search_ds as search_ds
from collections import deque

class Queue(search_ds.SearchDataStructure):
    def __init__(self):
        self.queue = deque()
    def pop(self):
        return self.queue.popleft()
    def push(self, item):
        self.queue.append(item)
    def clear(self):
        self.queue.clear()
    def is_empty(self):
        return len(self.queue) == 0