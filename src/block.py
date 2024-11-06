import pygame as pyg


# block class with init data is sprite, position, and size of each image in sprite

'''
class Block: 
    Attributes:
        raw_img: pygame.image // the raw image of the block
        cropTable: list // the list of crop value of the image
        index: int // the index of the current crop value in cropTable
        img: pygame.image // the image that is drew on screen (crop from raw_img with cropTable[index])
        rect: pygame.Rect // the position and size of the image on screen
    method: 
        __init__:
            init raw_img, rect, crop
            if crop[2] == -1 that mean use the whole image
            set cropTable to [crop]
            set index to 0
            set img to raw_img.subsurface(crop)
            set img to scale to rect size

        setCropTable:
            set cropTable to cropTable

        chooseSprite:
            set img to raw_img.subsurface(crop)
            set cropTable to [crop]
            set index to 0

        chooseSpriteByIndex:
            set img to raw_img.subsurface(cropTable[index])
            set index to index

        changePosition:
            set rect to (x, y, rect.width, rect.height)

        changePositionV:
            same as changePosition but take a tuple as argument

        changeSize:
            set rect to (rect.x, rect.y, width, height)
            set img to raw_img.subsurface(cropTable[index])
            set img to scale to (width, height)

        draw:
            draw img on screen at rect
'''

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
    def changePositionV(self, pos):
        self.rect = pyg.Rect(pos[0], pos[1], self.rect.width, self.rect.height)
    def changeSize(self, width, height):
        self.rect = pyg.Rect(self.rect.x, self.rect.y, width, height)
        self.img = self.raw_img.subsurface(self.cropTable[self.index])
        self.img = pyg.transform.scale(self.img, (width, height))

        
    def draw(self, screen):
        screen.blit(self.img, self.rect)
