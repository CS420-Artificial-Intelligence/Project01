import pygame as pyg 
from block import Block

class Button: 
    def __init__(self, imgpath1, imgpath2, rect): 
        img1 = pyg.image.load(imgpath1)
        img2 = pyg.image.load(imgpath2)

        self.img1 = Block(img1, rect, (0, 0, -1, -1))
        self.img2 = Block(img2, rect, (0, 0, -1, -1))
        self.rect = rect
        self.is_hover = False
        return 
    def mousemove(self, pos):
        self.is_hover = self.rect.collidepoint(pos)
        return
    def draw(self, screen):
        if self.is_hover:
            self.img1.draw(screen)
        else:
            self.img2.draw(screen)
        return
