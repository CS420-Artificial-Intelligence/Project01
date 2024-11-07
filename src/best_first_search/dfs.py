from best_first_search.search import Algorithm
from best_first_search.state import State
from best_first_search.search_ds import Stack


class DFSState(State):
    def f(self):
        return self.number_moved

class DFSAlgorithm(Algorithm):
    def __init__(self, initial_state: DFSState):
        super().__init__(Stack(), initial_state)
        self.algorithm_name = 'DFS'
