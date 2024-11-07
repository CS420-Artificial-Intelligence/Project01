from maze import Maze
from best_first_search.state import State
from best_first_search.search import Algorithm
from best_first_search.search_ds import PriorityQueue
from best_first_search import ucs, bfs, dfs, a_star
from save_stats import save_stats
import os

for file in ['input/input-01.txt']:
    id = file.split('.')[0].split('-')[1]
    output_file = f'output/output-{id}.txt'
    s = State()
    s.load_from_file(f'input/input-{id}.txt')
    print(s)
    ucs_algo = ucs.UCSAlgorithm(s)
    bfs_algo = bfs.BFSAlgorithm(s)
    dfs_algo = dfs.DFSAlgorithm(s)
    a_star_algo = a_star.AStarAlgorithm(s)
    ucs_algo.run()
    bfs_algo.run()
    dfs_algo.run()
    a_star_algo.run()
    save_stats(ucs_algo.stats_json(), output_file)
    save_stats(bfs_algo.stats_json(), output_file)
    save_stats(dfs_algo.stats_json(), output_file)
    save_stats(a_star_algo.stats_json(), output_file)
    break