import best_first_search.search_ds.search_ds as search_ds

class Queue(search_ds.SearchDataStructure):
    def __init__(self):
        self.queue = []
    def pop(self):
        return self.queue.pop(0)
    def push(self, item):
        self.queue.append(item)
    def clear(self):
        self.queue.clear()
    def is_empty(self):
        return len(self.queue) == 0