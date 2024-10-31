from map import Map

input_file = 'map/input-01.txt'
result = Map(input_file).getMap()
print("Maze:")
for row in result['maze']:
    print("".join(row))
print("\nStones with weights:", result['stones'])
print("Ares Position:", result['ares_position'])
print("Switches:", result['switches'])
