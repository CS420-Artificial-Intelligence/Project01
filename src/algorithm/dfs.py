from algorithm.search import Algorithm
from algorithm.search_ds.search_ds import SearchDataStructure
from algorithm.state import State
from algorithm.search_ds import Stack
from maze import Maze


class DFSState(State):
    def __init__(self, maze: Maze = Maze(), parent_state: 'DFSState' = None, input_path: str = None):
        self.map = maze
        self.parent_state = parent_state
        self.input_path = input_path
    def f(self):
        return self.map.number_moved
    def apply_action(self, action: str) -> 'DFSState':
        new_map = self.map.copy()
        status = new_map.apply_move(action)
        if status == -1:
            return None
        if status == 0:
            action = action.lower()
        return DFSState(new_map, self, action)

class DFSAlgorithm(Algorithm):
    def __init__(self, search_ds: SearchDataStructure, initial_state: DFSState = DFSState(), expand_goal: bool = False):
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
        self.algorithm_name = 'DFS'
    # def __init__(self, initial_state: DFSState):
    #     super().__init__(Stack(), initial_state)
    #     self.algorithm_name = 'DFS'
