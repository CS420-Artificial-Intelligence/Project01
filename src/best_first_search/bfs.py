from best_first_search.search import Algorithm
from best_first_search.state import State
from best_first_search.search_ds import Queue


class BFSState(State):
    def f(self):
        return self.number_moved

class BFSAlgorithm(Algorithm):
    def __init__(self, initial_state: BFSState):
        super().__init__(Queue(), initial_state)
