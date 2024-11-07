from algorithm.search import Algorithm
from algorithm.state import State
from algorithm.search_ds import Queue


class BFSState(State):
    def f(self):
        return self.number_moved

class BFSAlgorithm(Algorithm):
    def __init__(self, initial_state: BFSState):
        super().__init__(Queue(), initial_state)
        self.algorithm_name = 'BFS'
