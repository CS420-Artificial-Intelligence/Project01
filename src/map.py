import pygame as pyg 
from block import Block

'''

class Block: Image that is drew on screen

class Map 
Attributes:
    drawable Attributes:
        block_size: int // the size of a block in pixels (block is a square) 
        screenbias: list // the map may be bigger than the screen, so we only draw a part of it, this is use to specify which part of the map to draw
        wall_block: Block // the block that represent a wall
        nonwall_block: Block // the block that represent a non-wall
        switch_block: Block // the block that represent a switch 
        stone_entity: Entity // the entity that represent a stone 
        ares_entity: Entity // the entity that represent Ares 
    
    value Attributes:
        block_size: int // default is 80, this is use for zoom in and zoom out. The size of a block in pixels (block is a square) 
        are_position: list // the position of Ares in the map
        filename: str // the filename of the map
        rockValue: list // the list of rock value in the map 
        matrix: list // the matrix that represent the map
Method: 
    __init__: 
        init filename, wall_block, nonwall_block, switch_block, stone_entity, ares_entity
        read the file and init rockValue and matrix 
        find the position of Ares in the matrix

    setBlockSizes:
        change the size of all drawable attributes to block_size 
        this is use for zoom in and zoom out the map 
    increaseBlockSizes:
        increase the block_size by 5 and call setBlockSizes 
        zoom in 
    decreaseBlockSizes: 
        decrease the block_size by 5 and call setBlockSizes
        zoom out
    isValidMove: 
        check if Ares can move to a new position
    movingAres:
        move Ares to a new position
    addBias:
        add bias to screenbias
        move the screen to the right, left, up, down
    loadmap:
        load a new map 
    print:
        print the rockValue and matrix 
    draw:

'''

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
        
        self.ares_position = [-1, -1]

        with open(filename, "r") as file:
            self.rockValue = list(map(int, file.readline().split()))
            self.matrix = [list(line) for line in file]
        for i in range(len(self.matrix)):
            if self.ares_position != [-1, -1]: 
                break
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "+":
                    self.ares_position = [i, j] 
                    break 
                if self.matrix[i][j] == "@":
                    self.ares_position = [i, j] 
                    break
        return

    def setBlockSizes(self, block_size):
        self.block_size = block_size
        self.wall_block.changeSize(block_size, block_size)
        self.nonwall_block.changeSize(block_size, block_size)
        self.switch_block.changeSize(block_size, block_size)
        self.stone_entity.changeSize(block_size, block_size)
        self.ares_entity.changeSize(block_size, block_size)

    def increaseBlockSizes(self):
        self.block_size += 5
        self.wall_block.changeSize(self.block_size, self.block_size)
        self.nonwall_block.changeSize(self.block_size, self.block_size)
        self.switch_block.changeSize(self.block_size, self.block_size)
        self.stone_entity.changeSize(self.block_size, self.block_size)
        self.ares_entity.changeSize(self.block_size, self.block_size)
    def decreaseBlockSizes(self):
        self.block_size -= 5
        self.wall_block.changeSize(self.block_size, self.block_size)
        self.nonwall_block.changeSize(self.block_size, self.block_size)
        self.switch_block.changeSize(self.block_size, self.block_size)
        self.stone_entity.changeSize(self.block_size, self.block_size)
        self.ares_entity.changeSize(self.block_size, self.block_size)

    def isValidMove(self, delta): 
        pass 
    def movingAres(self, delta):
        pass 
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
                position = (j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size
                if self.matrix[i][j] == "#":
                    self.wall_block.changePositionV(position)
                    self.wall_block.draw(screen)

                if self.matrix[i][j] == ".":
                    self.switch_block.changePositionV(position)
                    self.switch_block.draw(screen)

                if self.matrix[i][j] == "*":
                    self.switch_block.changePositionV(position)
                    self.switch_block.draw(screen)
                    self.stone_entity.changePositionV(position)
                    self.stone_entity.draw(screen)

                if self.matrix[i][j] == "+":
                    self.switch_block.changePositionV(position)
                    self.switch_block.draw(screen)
                    self.ares_entity.changePositionV(position)
                    self.ares_entity.draw(screen)

                if self.matrix[i][j] == " ":
                    self.nonwall_block.changePositionV(position)
                    self.nonwall_block.draw(screen)
                if self.matrix[i][j] == "@":
                    self.nonwall_block.changePositionV(position)
                    self.nonwall_block.draw(screen)
                    self.ares_entity.changePositionV(position)
                    self.ares_entity.draw(screen)
                if self.matrix[i][j] == "$":
                    self.nonwall_block.changePositionV(position)
                    self.nonwall_block.draw(screen)
                    self.stone_entity.changePositionV(position)
                    self.stone_entity.draw(screen)

