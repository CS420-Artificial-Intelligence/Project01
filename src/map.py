
import pygame 

class Map:
    def __init__(self, filename): 

        #input from file
        with open(filename, 'r') as file:
            input_data = file.read()

        self.maze = []
        self.stones = []  
        self.switches = []  
        self.ares_position = None

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
                elif char == '@' or char == '+':  # Ares
                    ares_position = (r, c)
                elif char == '.':  # Switch
                    self.switches.append((r, c))
                elif char == '*':  # Stone on switch
                    self.stones.append((r, c, stone_weights[stone_index]))
                    self.switches.append((r, c))
                    stone_index += 1
            self.maze.append(row)
        # with open(filename) as f:
        #     self.stones = list(map(int, f.readline().split()))
        #     while True:
        #         line = f.readline()
        #         if not line:
        #             break
        #         line = line[:-1]
        #         self.map.append(line)

    def getMap(self):
        return {
            'maze': self.maze,
            'stones': self.stones,
            'ares_position': self.ares_position,
            'switches': self.switches
        }

