import pygame as pyg 
from block import Block


img = pyg.image.load("assets/rock.jpeg")

position = (20, 20)
crop = (167, 50, 301 - 167, 167 - 50)

block = Block(img, position[0], position[1], crop)

screen = pyg.display.set_mode((800, 600))
running = True

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    block.draw(screen)
    pyg.display.flip()
