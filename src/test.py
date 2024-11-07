from maze import Maze
from best_first_search.state import State
from best_first_search.search import Algorithm
from best_first_search.search_ds import PriorityQueue
from best_first_search import dfs
from best_first_search import bfs
from best_first_search import a_star
from best_first_search import ucs

s = State()
s.load_from_file('input/input-01.txt')
s.map.print_map()
print(str(s))

algorithm = dfs.DFSAlgorithm(s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)
print(tr)

algorithm.print_stats('output_DFS.txt')

algorithm = bfs.BFSAlgorithm(s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)
print(tr)

algorithm.print_stats('output_BFS.txt')


algorithm = ucs.UCSAlgorithm(s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)
print(tr)

algorithm.print_stats('output_UCS.txt')

algorithm = a_star.AStarAlgorithm(s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)
print(tr)

algorithm.print_stats('output_AStar.txt')



