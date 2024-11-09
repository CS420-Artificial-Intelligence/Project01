from maze import Maze
import numpy as np
from scipy.optimize import linear_sum_assignment
class State:
    def __init__(self, maze: Maze = Maze(), number_moved: int = 0, weight_moved: int = 0, parent_state: 'State' = None, input_path: str = None):
        self.map = maze
        self.number_moved = number_moved
        self.weight_moved = weight_moved
        self.parent_state = parent_state
        self.input_path = input_path

    def load_from_file(self, input_path: str) -> None:
        self.map.load_from_file(input_path)

    def apply_action(self, action: str) -> 'State':
        assert False, 'This method should be overriden'
        # new_map = self.map.copy()
        # status, cost = new_map.apply_move(action)
        # if status == -1:
        #     return None
        # if status == 0:
        #     action = action.lower()
        # return State(new_map, self.number_moved + 1, self.weight_moved + cost, self, action)

    def g(self) -> int:
        return self.weight_moved + self.number_moved
    def h(self) -> int:
        # heuristic: Hungarian algorithm
        cost_matrix = np.zeros((len(self.map.stones), len(self.map.switches)))
        for i, stone in enumerate(self.map.stones):
            for j, switch in enumerate(self.map.switches):
                cost_matrix[i, j] = (abs(stone[0] - switch[0]) + abs(stone[1] - switch[1])) * stone[2]
        row_indices, col_indices = linear_sum_assignment(cost_matrix)
        cost =  cost_matrix[row_indices, col_indices].sum()
        return cost
    def f(self) -> int:
        assert False, 'This method should be overriden'
        # return self.g() + self.h()
    def __hash__(self) -> int:
        # hash stones, switches, character, walls
        return hash(self.map)
    def __eq__(self, other) -> bool:
        return self.map == other.map
    def is_goal(self) -> bool:
        return self.map.is_final()
    def parent_state(self):
        return self.parent_state
    def expand(self):
        result = []
        for action in ['U', 'D', 'L', 'R']:
            new_state = self.apply_action(action)
            if new_state is not None:
                result.append(new_state)
        return result
    def __str__(self) -> str:
        return 'character: ' + str(self.map.ares_position) + ', stones: ' + str(self.map.stones) + ', switches: ' + str(self.map.switches) + ', cost: ' + str(self.g())


