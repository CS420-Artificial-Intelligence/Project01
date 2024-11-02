from map import Map
from map import Direction

input_file1 = 'map/input-01.txt'
input_file2 = 'map/input-01.txt'
map1 = Map()
map2 = Map()
map1.load_from_file(input_file1)
map2.load_from_file(input_file2)
map1.print_map()
while True:
    direction = input()
    if direction == 'U':
        map1.apply_move(Direction.U)
    elif direction == 'D':
        map1.apply_move(Direction.D)
    elif direction == 'L':
        map1.apply_move(Direction.L)
    elif direction == 'R':
        map1.apply_move(Direction.R)
    else: 
        break
    map1.print_map()
    print(map1.get_cost())
