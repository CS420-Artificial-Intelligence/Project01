import pygame as pyg 
from block import Block
from entity import Entity
from map import Map


class AresTour: 
    def __init__(self):
        self.block_size = 80
        self.crop_image = (0, 0, -1, -1)
        self.screen_size = (1200, 720)
        self.game_surface_size = (900, 660)
        self.statusline_surface_size = (900, 60)
        self.config_surface_size = (300, 720)

        self.wall_img = pyg.image.load("assets/wall.png")
        self.wall_block = Block(self.wall_img, (0, 0, self.block_size, self.block_size), self.crop_image)
        self.nonwall_img = pyg.image.load("assets/nonwall.png")
        self.nonwall_block = Block(self.nonwall_img, (0, 0, self.block_size, self.block_size), self.crop_image)
        self.switch_img = pyg.image.load("assets/switch.png")
        self.switch_block = Block(self.switch_img, (0, 0, self.block_size, self.block_size), self.crop_image)
        self.stone_img = pyg.image.load("assets/stone.png")
        self.stone_Entity = Entity(self.stone_img, (0, 0, self.block_size, self.block_size), self.crop_image)
        self.ares_img = pyg.image.load("assets/ares.png")
        self.ares_Entity = Entity(self.ares_img, (0, 0, self.block_size, self.block_size), self.crop_image)


        pyg.init()
        self.screen = pyg.display.set_mode(self.screen_size)
        self.game_surface = pyg.Surface(self.game_surface_size)
        self.statusline_surface = pyg.Surface(self.statusline_surface_size)
        self.config_surface = pyg.Surface(self.config_surface_size)
        self.running = True
        self.map = Map("input/input-01.txt", self.wall_block, self.nonwall_block, self.switch_block, self.stone_Entity, self.ares_Entity)

    def statusline_screen(self):
        self.statusline_surface.fill((125, 125, 255))
        return
    def config_screen(self):
        self.config_surface.fill((255, 125, 125))
        return
    def game_screen(self): 
        self.game_surface.fill((255, 255, 255))
        self.map.draw(self.game_surface)
    def event_handler(self): 
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
                return
            # if i is press, add (1, 0) to the bias 
            # if k is press, add (-1, 0) to the bias 
            # if j is press, add (0, -1) to the bias 
            # if l is press, add (0, 1) to the bias 
            if event.type == pyg.KEYDOWN:
            # if ctrl j is press 
                if event.key == 106 and event.mod == 64:
                    self.running = False 
                    return 
                if event.key == 105:
                    self.map.addBias(1, 0)
                if event.key == 107:
                    self.map.addBias(-1, 0)
                if event.key == 106:
                    self.map.addBias(0, 1)
                if event.key == 108:
                    self.map.addBias(0, -1)
                if event.key == 61:
                    self.map.increaseBlockSizes()
                if event.key == 45:
                    self.map.decreaseBlockSizes()
                if event.key == 114:
                    self.map.explain("dfs")
        self.map.continueExplain()
        return 
    def draw(self):
        
        self.statusline_screen()
        self.config_screen()
        self.game_screen()

        self.screen.blit(self.game_surface, (0, 0))
        self.screen.blit(self.statusline_surface, (0, 660))
        self.screen.blit(self.config_surface, (900, 0))
        pyg.display.flip()
        pyg.time.delay(100)
