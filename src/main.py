import pygame as pyg 
from block import Block
from map import Map

#img = pyg.image.load("assets/rock.jpeg")
#position = (20, 20)
#crop = (167, 50, 301 - 167, 167 - 50)
#block = Block(img, position[0], position[1], crop)

wall_img = pyg.image.load("assets/wall.png")
wall_block = Block(wall_img, 0, 0, (0, 0, 32, 32))
nonwall_img = pyg.image.load("assets/nonwall.png")
nonwall_block = Block(nonwall_img, 0, 0, (0, 0, 32, 32))


screen = pyg.display.set_mode((800, 600))
running = True
map = Map("map/input-01.txt", wall_block, nonwall_block)

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    map.draw(screen)
#    block.draw(screen)
    pyg.display.flip()
