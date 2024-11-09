from algorithm.search import Algorithm
from algorithm.search_ds.search_ds import SearchDataStructure
from algorithm.state import State
from algorithm.search_ds import PriorityQueue
from maze import Maze


class UCSState(State):
    def __init__(self, maze: Maze = Maze(), number_moved: int = 0, weight_moved: int = 0, parent_state: 'UCSState' = None, input_path: str = None):
        self.map = maze
        self.number_moved = number_moved
        self.weight_moved = weight_moved
        self.parent_state = parent_state
        self.input_path = input_path
    def f(self):
        return self.g()
    def apply_action(self, action: str) -> 'UCSState':
        new_map = self.map.copy()
        status, cost = new_map.apply_move(action)
        if status == -1:
            return None
        if status == 0:
            action = action.lower()
        return UCSState(new_map, self.number_moved + 1, self.weight_moved + cost, self, action)

class UCSAlgorithm(Algorithm):
    def __init__(self, search_ds: SearchDataStructure, initial_state: UCSState = UCSState(), expand_goal: bool = False):
        self.search_ds = search_ds
        self.search_ds.push(initial_state)
        self.expand_goal = expand_goal
        self.reached = dict()
        self.reached[initial_state] = initial_state.f()
        self.expanded = set()
        self.nodes_generated = 0
        self.time = 0
        self.memory = 0
        self.goal_state = None
        self.algorithm_name = 'UCS'
    # def __init__(self, initial_state: UCSState):
    #     super().__init__(PriorityQueue(), initial_state)
    #     self.algorithm_name = 'UCS'
