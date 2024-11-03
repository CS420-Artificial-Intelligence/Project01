from block import Block

class Entity(Block):
    def __init__(self, image, rect, crop):
        super().__init__(image, rect, crop)
    def changePosition(self, x, y):
        super().changePosition(x, y)
    def draw(self, screen):
        super().draw(screen)
