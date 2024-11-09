from maze import Maze
from algorithm.state import State
from algorithm.search import Algorithm
from algorithm.search_ds import PriorityQueue
from algorithm import ucs, bfs, dfs, a_star
from save_stats import save_stats
import os

s = Maze('input/input-01.txt')
s.print_map()
print(s.ares_position)
print(s.stones)
s.apply_move('U')
s.print_map()
print(s.ares_position)
print(s.stones)
s.apply_move('R')
s.print_map()
print(s.ares_position)
print(s.stones)
s.back_move('R')
s.print_map()
print(s.ares_position)
print(s.stones)
s.back_move('u')
s.print_map()
print(s.ares_position)
print(s.stones)
# for file in ['input/input-02.txt']:
#     id = file.split('.')[0].split('-')[1]
#     output_file = f'output/output-{id}.txt'
#     s = State()
#     s.load_from_file(f'input/input-{id}.txt')
#     print(s)
#     ucs_algo = ucs.UCSAlgorithm(s)
#     bfs_algo = bfs.BFSAlgorithm(s)
#     dfs_algo = dfs.DFSAlgorithm(s)
#     a_star_algo = a_star.AStarAlgorithm(s)
    

#     bfs_algo.run()
#     # save_stats(bfs_algo.stats_json(), output_file)
#     # print("Done")
#     # break
#     dfs_algo.run()
#     save_stats(dfs_algo.stats_json(), output_file)
#     print("Done")
#     ucs_algo.run()
#     save_stats(ucs_algo.stats_json(), output_file)
#     print("Done")
#     a_star_algo.run()
#     save_stats(a_star_algo.stats_json(), output_file)
#     break