import pygame as pyg


# block class with init data is sprite, position, and size of each image in sprite


class Block(pyg.sprite.Sprite):

    def __init__(self, image, rect, crop):
        
        pyg.sprite.Sprite.__init__(self)
        self.raw_img = image

        # if crop[2] == -1 that mean use the whole image
        if crop[2] == -1:
            crop = (0, 0, image.get_width(), image.get_height())
        
        self.cropTable = [crop]
        self.index = 0
        self.img = self.raw_img.subsurface(crop)
        self.img = pyg.transform.scale(self.img, (rect[2], rect[3]))
        self.rect = pyg.Rect(rect)
    def setCropTable(self, cropTable):
        self.cropTable = cropTable
    def chooseSprite(self, crop):
        self.img = self.raw_img.subsurface(crop)
        self.cropTable = [crop]
        self.index = 0
    def chooseSpriteByIndex(self, index):
        crop = self.cropTable[index]
        self.img = self.raw_img.subsurface(crop)
        self.index = index

    def changePosition(self, x, y):
        self.rect = pyg.Rect(x, y, self.rect.width, self.rect.height)
    def changeSize(self, width, height):
        self.rect = pyg.Rect(self.rect.x, self.rect.y, width, height)
        self.img = self.raw_img.subsurface(self.cropTable[self.index])
        self.img = pyg.transform.scale(self.img, (width, height))

        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
