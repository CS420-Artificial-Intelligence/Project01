from maze import Maze
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
        new_map = self.map.copy()
        status, cost = new_map.apply_move(action)
        if status == -1:
            return None
        if status == 0:
            action = action.lower()
        return State(new_map, self.number_moved + 1, self.weight_moved + cost, self, action)

    def g(self) -> int:
        return self.number_moved + self.weight_moved
    def h(self) -> int:
        # heuristic
        sorted_stones_weight = sorted(self.map.stones, key=lambda x: x[2], reverse=True)
        tmp_switches = self.map.switches
        sum_h = 0
        for i, (r, c, _, _) in enumerate(sorted_stones_weight):
            max_dis = (0, 0)
            for j, (r_switch,c_switch) in enumerate(tmp_switches):
                max_dis = max(max_dis, (abs(r - r_switch) + abs(c - c_switch), j))
            sum_h += max_dis[0]
            tmp_switches.pop(max_dis[1])
        return sum_h
    def f(self) -> int:
        # base on a specific algorithm
        return self.g()
        pass
    def __hash__(self) -> int:
        # hash stones, switches, character, walls
        return hash(self.map)
    def __eq__(self, other) -> bool:
        return self.map == other.map
    def is_goal(self) -> bool:
        return self.map.is_final()
    def parent_state(self) -> 'State':
        return self.parent_state
    def expand(self) -> list['State']:
        result = []
        for action in ['U', 'D', 'L', 'R']:
            new_state = self.apply_action(action)
            if new_state is not None:
                result.append(new_state)
        return result
    def __str__(self) -> str:
        return 'character: ' + str(self.map.ares_position) + ', stones: ' + str(self.map.stones) + ', switches: ' + str(self.map.switches) + ', cost: ' + str(self.g())


