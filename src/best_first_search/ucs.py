from best_first_search.search import Algorithm
from best_first_search.state import State
from best_first_search.search_ds import PriorityQueue


class UCSState(State):
    def f(self):
        return self.g()

class UCSAlgorithm(Algorithm):
    def __init__(self, initial_state: UCSState):
        super().__init__(PriorityQueue(), initial_state)
        self.algorithm_name = 'UCS'
