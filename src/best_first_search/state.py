class State:
    def __init__(self, walls: list[tuple[int, int]] = [], stones: list[tuple[int, int, int]] = [], character: tuple[int, int] = [], switches: list[tuple[int, int]] = [], number_moved: int = 0, weight_moved: int = 0, parent_state: 'State' = None, input_path: str = None):
        self.walls = walls.copy()
        self.stones = stones.copy()
        self.character = character
        self.switches = switches.copy()
        self.number_moved = number_moved
        self.weight_moved = weight_moved
        self.parent_state = parent_state
        self.input_path = input_path
    def load_from_file(self, input_path: str) -> None:
        with open(input_path, 'r') as file:
            s = file.readlines()
            weights = list(map(int, s[0].split()))
            for i in range(1, len(s)):
                s[i] = s[i].strip()
                for j in range(len(s[i])):
                    if s[i][j] == '#':
                        self.walls.append((i, j))
                    elif s[i][j] == '$':
                        self.stones.append((i, j, weights[0]))
                        weights.pop(0)
                    elif s[i][j] == '@':
                        self.character = (i, j)
                    elif s[i][j] == '.':
                        self.switches.append((i, j))
                    elif s[i][j] == '*':
                        self.stones.append((i, j, weights[0]))
                        weights.pop(0)
                        self.switches.append((i, j))
                    elif s[i][j] == '+':
                        self.character = (i, j)
                        self.switches.append((i, j))
                    else:
                        assert s[i][j] == ' ', "Invalid character in input file, found " + s[i][j]
            self.walls = sorted(self.walls)
            self.stones = sorted(self.stones)
            self.switches = sorted(self.switches)


    def apply_action(self, action: str) -> 'State':
        m = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        direction = m[action]
        new_character = (self.character[0] + direction[0], self.character[1] + direction[1])
        if new_character in self.walls:
            return None
        new_stones = self.stones.copy()
        tot_cost = 0
        # check if there is a stone in the new character position
        act = action.lower()
        if new_character in [stone[:2] for stone in new_stones]:
            new_stone_pos = (new_character[0] + direction[0], new_character[1] + direction[1])
            if new_stone_pos in self.walls or new_stone_pos in [stone[:2] for stone in new_stones]:
                return None
            act = action.upper()
            cost_stones = [stone[2] for stone in new_stones if stone[:2] == new_character][0]
            new_stones.remove((new_character[0], new_character[1], cost_stones))
            new_stones.append((new_stone_pos[0], new_stone_pos[1], cost_stones))
            tot_cost += cost_stones
        return State(self.walls, new_stones, new_character, self.switches, self.number_moved + 1, self.weight_moved + tot_cost, self, act)

    def g(self) -> int:
        return self.number_moved + self.weight_moved
    def h(self) -> int:
        # heuristic
        pass
    def f(self) -> int:
        # base on a specific algorithm
        return self.g()
        pass
    def __hash__(self) -> int:
        # hash stones, switches, character, walls
        return hash((tuple(self.stones), tuple(self.switches), self.character, tuple(self.walls)))
    def __eq__(self, other) -> bool:
        # compare stones, switches, character, walls
        return self.stones == other.stones and self.switches == other.switches and self.character == other.character and self.walls == other.walls
    def is_goal(self) -> bool:
        # check if all stones are on switches
        return all([stone[:2] in self.switches for stone in self.stones])
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
        return 'character: ' + str(self.character) + ', stones: ' + str(self.stones) + ', switches: ' + str(self.switches) + ', walls: ' + str(self.walls) + ', cost: ' + str(self.g())


