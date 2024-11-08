import pygame as pyg 
from block import Block
from entity import Entity
from map import Map
import menu


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


pyg.init()
screen = pyg.display.set_mode(screen_size)
game_surface = pyg.Surface(game_surface_size)
running = True
map = Map("input/input-01.txt", wall_block, nonwall_block, switch_block, stone_Entity, ares_Entity)
map.addBias(0, 2)



def game_screen(map_idx: int):
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
            # if press esc
            if event.key == 27:
                return 0

    map.continueExplain()

    game_surface.fill((255, 255, 255))
    map.draw(game_surface)
    screen.blit(game_surface, (0, 0))
    pyg.display.flip()
    return 1


def game_screen_loop(map_idx: int):
    running = 1
    while running != 0:
        running = game_screen(map_idx)
        pyg.time.delay(100)
    return 1


def main():
    running = True
    current_screen = 'MENU'
    current_map = 0
    while running:
        if current_screen == 'MENU':
            status = menu.run_menu(screen)
            if status == -1:
                running = False
            else:
                current_screen = 'GAME'
                current_map = status
        else:
            running = game_screen_loop(current_map)
            current_screen = 'MENU'


if __name__ == '__main__':
    main()
    pyg.quit()

