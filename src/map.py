
import pygame 

# create a map class which is a 2D array of tiles 
# The first line contains list of integers representing the weights of each stone, in the order they appear in the grid, from left to right and top to bottom

class Map:
    def __init__(self, filename): 
        self.map = []
        
        
        with open(filename) as f:
            self.stones = list(map(int, f.readline().split()))
            while True:
                line = f.readline()
                if not line:
                    break
                line = line[:-1]
                self.map.append(line)

    def getMap(self):
        return self.map

