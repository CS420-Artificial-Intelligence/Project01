class Maze:
    def __init__(self, filename = None): 
        self.num_rows = 0
        self.num_cols = 0
        self.maze = []
        self.stones = []
        self.switches = []
        self.ares_position = None
        if filename is not None:
            self.load_from_file(filename)
        
    def copy(self):
        new_map = Maze()
        new_map.num_rows = self.num_rows
        new_map.num_cols = self.num_cols
        new_map.maze = [row.copy() for row in self.maze]
        new_map.stones = self.stones.copy()
        new_map.switches = self.switches.copy()
        new_map.ares_position = self.ares_position
        return new_map
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            input_data = file.read()
        lines = input_data.strip().split('\n')
        stone_weights = list(map(int, lines[0].split()))
        
        stone_index = 0  
        for r, line in enumerate(lines[1:]):
            row = []
            for c, char in enumerate(line):
                row.append(char)
                if char == '$':  # Stone
                    self.stones.append((r, c, stone_weights[stone_index]))
                    stone_index += 1
                elif char == '*':  # Stone on switch
                    self.stones.append((r, c, stone_weights[stone_index]))
                    self.switches.append((r, c))
                    stone_index += 1
                elif char == '@': # Ares
                    self.ares_position = (r, c)
                elif char == '+':  # Ares on switch
                    self.ares_position = (r, c)
                    self.switches.append((r, c))
                elif char == '.':  # Switch
                    self.switches.append((r, c))
                else:
                    assert char == ' ' or char == '#', "Invalid character in input file, found " + char
            self.maze.append(row)
        self.num_rows = len(self.maze)
        self.num_cols = len(self.maze[0])
        self.stones = sorted(self.stones)
        self.switches = sorted(self.switches)

    def is_valid_position(self, r, c, is_stone):
        check_valid = (0 <= r < self.num_rows and 0 <= c < self.num_cols and self.maze[r][c] != '#')
        if is_stone:
            return check_valid and self.maze[r][c] != '*' and self.maze[r][c] != '$'
        return check_valid
    
    def move_stone(self, r, c, direction: str):
        m = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        new_r, new_c = r + m[direction][0], c + m[direction][1]
        return new_r, new_c

    def get_stone(self, r, c):
        for i, (stone_r, stone_c, _) in enumerate(self.stones):
            if stone_r == r and stone_c == c:
                return i
        return None
    
    def update_maze(self, r, c, new_r, new_c, new_stone_r, new_stone_c):
        #Handle ares position
        if (self.maze[r][c] == '+'):
            self.maze[r][c] = '.'
        else:
            self.maze[r][c] = ' '
        #Handle stone position
        if new_stone_r is not None:
            if (self.maze[new_r][new_c] == '*'):
                self.maze[new_r][new_c] = '.'
            else:
                self.maze[new_r][new_c] = ' '
        #Handle new ares position
        if (self.maze[new_r][new_c] == '.'):
            self.maze[new_r][new_c] = '+'
        else:
            self.maze[new_r][new_c] = '@'
        #Handle new stone position
        if new_stone_r is not None:
            if (self.maze[new_stone_r][new_stone_c] == '.'):
                self.maze[new_stone_r][new_stone_c] = '*'
            else:
                self.maze[new_stone_r][new_stone_c] = '$'

    #return 1 if we moved a stone, 0 if we move ares only, -1 if we can't move
    def apply_move(self, direction: str) -> tuple[int, int]:
        m = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        r, c = self.ares_position
        new_r, new_c = r + m[direction][0], c + m[direction][1]
        if not self.is_valid_position(new_r, new_c, False):
            return [-1, -1]
        stone_index = self.get_stone(new_r, new_c)
        if stone_index is not None:
            weight = self.stones[stone_index][2]
            new_stone_r, new_stone_c = self.move_stone(new_r, new_c, direction)
            if not self.is_valid_position(new_stone_r, new_stone_c, True):
                return [-1, -1]
            self.stones[stone_index] = (new_stone_r, new_stone_c, weight)   
            self.stones = sorted(self.stones)
            self.ares_position = (new_r, new_c)
            self.update_maze(r, c, new_r, new_c, new_stone_r, new_stone_c)
            return [1, weight]
        else:
            self.ares_position = (new_r, new_c)
            self.update_maze(r, c, new_r, new_c, None, None)
            return [0, 0]
        
    def print_map(self):
        for row in self.maze:
            print(''.join(row))
    def is_final(self) -> bool:
        for switch in self.switches:
            if switch not in [stone[:2] for stone in self.stones]:
                return False
        return True
    
    def __hash__(self):
        sorted_stones = sorted(self.stones)
        return hash((self.ares_position, tuple(sorted_stones)))

    def __eq__(self, other: 'Maze'):
        return self.ares_position == other.ares_position and self.stones == other.stones
