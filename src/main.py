import pygame as pyg 
from block import Block
from entity import Entity
from map import Map
from src.GUI.Button import Button
from src.GUI.ComboBox import ComboBox

#img = pyg.image.load("assets/rock.jpeg")
#position = (20, 20)
#crop = (167, 50, 301 - 167, 167 - 50)
#block = Block(img, position[0], position[1], crop)

block_size = 80
crop_image = (0, 0, -1, -1)
screen_size = (1200, 720)
game_surface_size = (1200, 720)

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


pyg.init()
screen = pyg.display.set_mode(screen_size)
font = pyg.font.Font(None, 30)
combo_box = ComboBox(250,0,200,30,font,["DFS","BFS","UCS","A*"])
level_select = ComboBox(0,0,200,30,font,["Map 1", "Map 2", "Map 3", "Map 4", "Map 5", "Map 6", "Map 7", "Map 8", "Map 9", "Map 10"])

load_level_button = Button(500,0,150,30,"Load Level",font,(33, 155, 157),(255,255,255))
previous_button = Button(700,0,150,30,"Previous",font,(33, 155, 157),(255,255,255))
next_button = Button(900,0,150,30,"Next",font,(33, 155, 157),(255,255,255))

width_left = 1200
height_left = 690

game_surface = pyg.Surface(game_surface_size)
running = True
map = Map("input/input-01.txt", wall_block, nonwall_block, switch_block, stone_Entity, ares_Entity)



def game_screen():
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            print("Quit")
            return 0
        level_select.handle_event(event)
        combo_box.handle_event(event)
        if load_level_button.handle_event(event):
            Str = level_select.get_selected()
            num = int(Str[len(Str) - 1])
            ref = "input/input-"
            if num < 10:
                ref += "0" + str(num)
            else:
                ref += str(num)
            ref += ".txt"
            map.__init__(ref,wall_block, nonwall_block, switch_block, stone_Entity, ares_Entity)

        previous_button.handle_event(event)
        next_button.handle_event(event)
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
            
#            if event.key == 97: 
#                map.maze.apply_move('L')
#            if event.key == 100:
#                map.maze.apply_move('R')
#            if event.key == 119:
#                map.maze.apply_move('U')
#            if event.key == 115:
#                map.maze.apply_move('D')
            # if press r 
            if event.key == 114:
                map.explain("dfs")


    map.continueExplain()

    game_surface.fill((255, 255, 255))

    map.draw(game_surface)
    screen.blit(game_surface, (0, 0))

    combo_box.draw(screen)
    level_select.draw(screen)
    load_level_button.draw(screen)
    previous_button.draw(screen)
    next_button.draw(screen)

    pyg.display.flip()
    return 1

while running != 0:
    running = game_screen()
    pyg.time.delay(100)
