import pygame as pyg 
from block import Block

class Map:
    def __init__(self, filename, wall_block, nonwall_block): 
        self.wall_block = wall_block
        self.nonwall_block = nonwall_block
        self.filename = filename
        # the first line is the integer array 
        # the rest is the char matrix
        
        with open(filename, "r") as file:
            self.rockValue = list(map(int, file.readline().split()))
            self.matrix = [list(line) for line in file]
    def print(self):
        print(self.rockValue)
        print(self.matrix)
    def draw(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "1":
                    self.wall_block.changePosition(j * 33, i * 33)
                    self.wall_block.draw(screen)
                else:
                    self.nonwall_block.changePosition(j * 33, i * 33)
                    self.nonwall_block.draw(screen)

