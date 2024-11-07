from algorithm.search import Algorithm
from algorithm.state import State
from algorithm.search_ds import Stack


class DFSState(State):
    def f(self):
        return self.number_moved

class DFSAlgorithm(Algorithm):
    def __init__(self, initial_state: DFSState):
        super().__init__(Stack(), initial_state)
        self.algorithm_name = 'DFS'
