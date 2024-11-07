from algorithm.search import Algorithm
from algorithm.state import State
from algorithm.search_ds import Queue


class AStarState(State):
    def f(self):
        return self.g() + self.h()

class AStarAlgorithm(Algorithm):
    def __init__(self, initial_state: AStarState):
        super().__init__(Queue(), initial_state)
        self.algorithm_name = 'A*'