import pygame as pyg 
from block import Block
from entity import Entity
from map import Map

from selectbox import selectBox
from algochoose import algoChoose
from speed_button import speedButton
from step_button import stepButton
from statusline import statusLine

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

        self.config_level_select = selectBox(pyg.Rect(0, 0, 300, 60))
        self.algochoose = algoChoose(pyg.Rect(0, 70, 300, 60))
        self.speedbutton = speedButton(pyg.Rect(0, 150, 300, 60))
        self.stepbutton = stepButton(pyg.Rect(0, 220, 300, 60))
        
        inf = [["Score", "0"], ["Moving", "0"], ["Time", "0s"]]
        self.statusline = statusLine(pyg.Rect(0, 0, 900, 60), inf)


    def statusline_screen_draw(self):
        self.statusline.draw(self.statusline_surface)
        return
    def statusline_screen_event_handler(self, event):
        return 

    def config_screen_draw(self):
        self.config_surface.fill((255, 125, 125))
        self.speedbutton.draw(self.config_surface)
        self.stepbutton.draw(self.config_surface)
        self.algochoose.draw(self.config_surface)
        self.config_level_select.draw(self.config_surface)
        return
    def config_screen_event_handler(self, event):
        self.config_level_select.event_handler(event)
        self.algochoose.event_handler(event)
        return

    def game_screen_draw(self): 
        self.game_surface.fill((255, 255, 255))
        self.map.draw(self.game_surface)

    def game_screen_event_handler(self, event):
        if event.type == pyg.KEYDOWN:
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
    
    def event_handler(self): 
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
                return
            self.game_screen_event_handler(event)
            self.config_screen_event_handler(event)
            self.statusline_screen_event_handler(event)

        self.map.continueExplain()
        return 
    def draw(self):
        
        self.statusline_screen_draw()
        self.config_screen_draw()
        self.game_screen_draw()

        self.screen.blit(self.game_surface, (0, 0))
        self.screen.blit(self.statusline_surface, (0, 660))
        self.screen.blit(self.config_surface, (900, 0))
        pyg.display.flip()
        pyg.time.delay(100)
