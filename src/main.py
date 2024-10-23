from map import Map
from obj import Object
import pygame


obj = Object("assets/wall.png")

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Pygame Example')


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    obj.draw(screen, 0, 0)

    pygame.display.flip()
