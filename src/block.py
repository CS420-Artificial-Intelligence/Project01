import pygame as pyg


# block class with init data is sprite, position, and size of each image in sprite


class Block(pyg.sprite.Sprite):

    def __init__(self, image, x, y, crop):
        pyg.sprite.Sprite.__init__(self)
        self.raw_img = image

        self.img = self.raw_img.subsurface(crop)
        self.rect = pyg.Rect(x, y, crop[2], crop[3])
    
    def chooseSprite(self, crop):
        self.img = self.raw_img.subsurface(crop)
        self.rect = pyg.Rect(self.rect.x, self.rect.y, crop[2], crop[3])

    def draw(self, screen):
        screen.blit(self.img, self.rect)
