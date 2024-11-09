
import time 

from algorithm.state import State
from algorithm.search import Algorithm
from algorithm.search_ds import PriorityQueue, Queue, Stack
from algorithm import ucs, bfs, dfs, a_star

import pygame as pyg 

from block import Block
from maze import Maze


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
        
        self.maze = Maze(self.filename)
        self.inexplainmode = False
        self.last_move = time.time()
        self.duration = 0.5 

        self.fontpath = "assets/Noto_Sans_Mono/NotoSansMono-VariableFont_wdth,wght.ttf"
        self.fontsize = 35
        self.font = pyg.font.Font(self.fontpath, self.fontsize)
        self.textlist = []
        self.stoneslist = self.maze.stones 
        self.solution = []
        self.prev_solution = []

        WHITE = (255, 255, 255)

        for stone in self.stoneslist:
            self.textlist.append(self.font.render(str(stone[2]), True, WHITE))
        return
    def loadMap(self, filename):
        self.filename = filename
        self.maze = Maze(self.filename)
        self.stoneslist = self.maze.stones
        self.textlist = []
        for stone in self.stoneslist:
            self.textlist.append(self.font.render(str(stone[2]), True, (255, 255, 255)))
        return

    def return_num_col(self):
        return self.maze.num_cols

    def return_num_row(self):
        return self.maze.num_rows

    def run_ucs(self):
        # state = State(self.maze)
        # ucs_engine = ucs.UCSAlgorithm(state) 
        state = ucs.UCSState(self.maze)
        ucs_engine = ucs.UCSAlgorithm(PriorityQueue(), state)
        ucs_engine.run()
        str = ucs_engine.stats_json()['solution'] 
        
        # for loop from end to begin 
        for i in range(len(str) - 1, -1, -1):
            self.solution.append(str[i])

    def run_dfs(self):
        # state = State(self.maze)
        # dfs_engine = dfs.DFSAlgorithm(state)
        state = dfs.DFSState(self.maze)
        dfs_engine = dfs.DFSAlgorithm(Stack(), state)
        dfs_engine.run()
        str = dfs_engine.stats_json()['solution']
        
        for i in range(len(str) - 1, -1, -1):
            self.solution.append(str[i]) 

    def run_bfs(self):
        # state = State(self.maze)
        # bfs_engine = bfs.BFSAlgorithm(state)
        state = bfs.BFSState(self.maze)
        bfs_engine = bfs.BFSAlgorithm(Queue(), state)
        bfs_engine.run()
        str = bfs_engine.stats_json()['solution']

        for i in range(len(str) - 1, -1, -1):
            self.solution.append(str[i])
        

    def run_a_star(self):
        # state = State(self.maze)
        # a_star_engine = a_star.AStarAlgorithm(state)
        state = a_star.AStarState(self.maze)
        a_star_engine = a_star.AStarAlgorithm(PriorityQueue(), state)
        a_star_engine.run()
        
        str = a_star_engine.stats_json()['solution']

        for i in range(len(str) - 1, -1, -1):
            self.solution.append(str[i])
    
    def isInExplainMode(self):
        return self.inexplainmode
    
    def explain(self, str):
        self.inexplainmode = True
        self.last_move = time.time() 
        self.solution = []
        if str == "ucs":
            self.run_ucs()
        if str == "dfs":
            self.run_dfs()
        if str == "bfs":
            self.run_bfs()
        if str == "a_star":
            self.run_a_star()

    
    def continueExplain(self):
        if self.inexplainmode == False:
            return 
        if len(self.solution) == 0:
            self.inexplainmode = False
            return 
        if time.time() - self.last_move < self.duration:
            return 
        chr = self.solution.pop() 
        self.maze.apply_move(chr)
        self.last_move = time.time()
        self.prev_solution.append(chr)

    def explainNext(self): 
        if len(self.solution) == 0:
            self.inexplainmode = False
            return 
        if time.time() - self.last_move < 0.1:
            return
        chr = self.solution.pop() 
        self.maze.apply_move(chr)
        self.last_move = time.time()
        self.prev_solution.append(chr)
    def explainPrev(self): 
        print("Not implemented yet: Map.explainPrev()")
        if len(self.prev_solution) == 0:
            return
        if time.time() - self.last_move < 0.1:
            return
        chr = self.prev_solution.pop()
        self.maze.back_move(chr)
        self.last_move = time.time()
        self.solution.append(chr)
        # pass 

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
        
        self.fontsize += 5 
        for stone in self.stoneslist:
            self.textlist.append(self.font.render(str(stone[2]), True, (255, 255, 255)))

    def decreaseBlockSizes(self):
        self.block_size -= 5
        self.wall_block.changeSize(self.block_size, self.block_size)
        self.nonwall_block.changeSize(self.block_size, self.block_size)
        self.switch_block.changeSize(self.block_size, self.block_size)
        self.stone_entity.changeSize(self.block_size, self.block_size)
        self.ares_entity.changeSize(self.block_size, self.block_size)

        self.fontsize -= 5 
        for stone in self.stoneslist:
            self.textlist.append(self.font.render(str(stone[2]), True, (255, 255, 255)))

    def addBias(self, x, y):
        self.screenbias[1] += x
        self.screenbias[0] += y
    def draw(self, screen):
        self.matrix = self.maze.maze
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                position = (j + self.screenbias[0]) * self.block_size, (i + self.screenbias[1]) * self.block_size
                if self.matrix[i][j] == "#":
                    self.nonwall_block.changePositionV(position)
                    self.nonwall_block.draw(screen)
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
        stoneslist = self.maze.stones
        for i in range(len(stoneslist)): 
            stone = stoneslist[i]
            hw = 0
            hh = 0
            position = (stone[1] + self.screenbias[0]) * self.block_size + hw, hh + (stone[0] + self.screenbias[1]) * self.block_size
            screen.blit(self.textlist[stone[3]], position)


