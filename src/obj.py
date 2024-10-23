import pygame 

class Object:
    def __init__(self, filepath):
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
    
    def getImage(self):
        return self.image
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
