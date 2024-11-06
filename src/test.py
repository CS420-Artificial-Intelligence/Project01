from maze import Maze
from best_first_search.state import State
from best_first_search.search import Algorithm
from best_first_search.search_ds import PriorityQueue

s = State()
s.load_from_file('input/input-01.txt')
s.map.print_map()
print(str(s))

algorithm = Algorithm(PriorityQueue(), s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)
print(tr)

algorithm.print_stats('output.txt')

