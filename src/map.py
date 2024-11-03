import pygame as pyg 
from block import Block

class Map:
    def __init__(self, filename, wall_block, nonwall_block, switch_block, stone_entity, ares_entity): 
        self.block_size = 80
        self.screenbias = [0, 0]
        self.wall_block = wall_block
        self.nonwall_block = nonwall_block
        self.switch_block = switch_block
        self.stone_entity = stone_entity 
        self.ares_entity = ares_entity
        self.filename = filename
        
        with open(filename, "r") as file:
            self.rockValue = list(map(int, file.readline().split()))
            self.matrix = [list(line) for line in file]
    def setBlockSizes(self, block_size):
        self.block_size = block_size
    def addBias(self, x, y):
        self.screenbias[1] -= x
        self.screenbias[0] -= y
    def loadmap(self, filename): 
        self.filename = filename
        with open(filename, "r") as file:
            self.rockValue = list(map(int, file.readline().split()))
            self.matrix = [list(line) for line in file]
    def print(self):
        print(self.rockValue)
        print(self.matrix)
    def draw(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "#":
                    self.wall_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.wall_block.draw(screen)
                if self.matrix[i][j] == ".":
                    self.switch_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.switch_block.draw(screen)
                if self.matrix[i][j] == "*":
                    self.switch_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.switch_block.draw(screen)
                    self.stone_entity.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.stone_entity.draw(screen)
                if self.matrix[i][j] == "+":
                    self.switch_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.switch_block.draw(screen)
                    self.ares_entity.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.ares_entity.draw(screen)
                if self.matrix[i][j] == " ":
                    self.nonwall_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.nonwall_block.draw(screen)
                if self.matrix[i][j] == "@":
                    self.nonwall_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.nonwall_block.draw(screen)
                    self.ares_entity.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.ares_entity.draw(screen)
                if self.matrix[i][j] == "$":
                    self.nonwall_block.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.nonwall_block.draw(screen)
                    self.stone_entity.changePosition ((j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size)
                    self.stone_entity.draw(screen)

