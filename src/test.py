from maze import Maze
from best_first_search.state import State
from best_first_search.search import Algorithm
from best_first_search.search_ds import PriorityQueue
from best_first_search import ucs, bfs, dfs
from save_stats import save_stats
import os

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

for file in ['input/input-01.txt']:
    id = file.split('.')[0].split('-')[1]
    output_file = f'output/output-{id}.txt'
    s = State()
    s.load_from_file(f'input/input-{id}.txt')
    print(s)
    ucs_algo = ucs.UCSAlgorithm(s)
    # bfs_algo = bfs.BFSAlgorithm(s)
    # dfs = dfs.DFSAlgorithm(s)
    ucs_algo.run()
    # bfs_algo.run()
    # dfs.run()
    save_stats(ucs_algo.stats_json(), output_file)
    # save_stats(bfs_algo.stats_json(), output_file)
    # save_stats(dfs.stats_json(), output_file)
    break