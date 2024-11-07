from best_first_search.search import Algorithm
from best_first_search.state import State
from best_first_search.search_ds import Queue


class AStarState(State):
    def f(self):
        return self.g() + self.h()

class AStarAlgorithm(Algorithm):
    def __init__(self, initial_state: AStarState):
        super().__init__(Queue(), initial_state)
