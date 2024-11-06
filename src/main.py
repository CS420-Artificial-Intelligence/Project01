import pygame as pyg 
from block import Block
from entity import Entity
from map import Map


#img = pyg.image.load("assets/rock.jpeg")
#position = (20, 20)
#crop = (167, 50, 301 - 167, 167 - 50)
#block = Block(img, position[0], position[1], crop)

block_size = 80
crop_image = (0, 0, -1, -1)
screen_size = (1200, 720)
game_surface_size = (700, 500)

wall_img = pyg.image.load("assets/wall.png")
wall_block = Block(wall_img, (0, 0, block_size, block_size), crop_image)
nonwall_img = pyg.image.load("assets/nonwall.png")
nonwall_block = Block(nonwall_img, (0, 0, block_size, block_size), crop_image)
switch_img = pyg.image.load("assets/switch.png")
switch_block = Block(switch_img, (0, 0, block_size, block_size), crop_image)
stone_img = pyg.image.load("assets/stone.png")
stone_Entity = Entity(stone_img, (0, 0, block_size, block_size), crop_image)
ares_img = pyg.image.load("assets/ares.png")
ares_Entity = Entity(ares_img, (0, 0, block_size, block_size), crop_image)



screen = pyg.display.set_mode(screen_size)
game_surface = pyg.Surface(game_surface_size)
running = True
map = Map("input/input-01.txt", wall_block, nonwall_block, switch_block, stone_Entity, ares_Entity)
map.addBias(0, 2)



def game_screen():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            print("Quit")
            return 0
        # if i is press, add (1, 0) to the bias 
        # if k is press, add (-1, 0) to the bias 
        # if j is press, add (0, -1) to the bias 
        # if l is press, add (0, 1) to the bias 
        if event.type == pyg.KEYDOWN:
            if event.key == 105:
                map.addBias(1, 0)
            if event.key == 107:
                map.addBias(-1, 0)
            if event.key == 106:
                map.addBias(0, 1)
            if event.key == 108:
                map.addBias(0, -1)


            if event.key == 61:
                map.increaseBlockSizes()
            if event.key == 45:
                map.decreaseBlockSizes()

    game_surface.fill((255, 255, 255))
    map.draw(game_surface)
    screen.blit(game_surface, (0, 0))
    pyg.display.flip()
    return 1

while running != 0:
    running = game_screen()
    pyg.time.delay(100)
