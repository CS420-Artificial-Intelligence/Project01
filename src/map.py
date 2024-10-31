
import pygame 

class Map:
    def __init__(self):
        self.maze = []
        self.stones = []
        self.switches = []
        self.ares_position = None
    
    def __init__(self, filename): 
        self.load_from_file(filename)
        
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
                
        self.maze.append(row)
    
    
    def getMap(self):
        return {
            'maze': self.maze,
            'stones': self.stones,
            'ares_position': self.ares_position,
            'switches': self.switches
        }

