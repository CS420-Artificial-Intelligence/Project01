import best_first_search.search_ds.search_ds as search_ds

class Stack(search_ds.SearchDataStructure):
    def __init__(self):
        self.stack = []
    def pop(self):
        return self.stack.pop()
    def push(self, item):
        self.stack.append(item)
    def clear(self):
        self.stack.clear()
    def is_empty(self):
        return len(self.stack) == 0