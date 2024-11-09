from algorithm.search_ds.stack import Stack
from maze import Maze
from algorithm.state import State
from algorithm.search import Algorithm
from algorithm.search_ds import PriorityQueue, Queue
from algorithm import ucs, bfs, dfs, a_star
from save_stats import save_stats
import os

#run all file in input
id = "01"
input_file = "input/" + "input-" + id + ".txt"
output_file = "output/" + "output-" + id + ".txt"
bfs_state = bfs.BFSState()
bfs_state.load_from_file(input_file)
bfs_algo = bfs.BFSAlgorithm(Queue(), bfs_state)
bfs_algo.run()
save_stats(bfs_algo.stats_json(), output_file)
print("Done")

dfs_state = dfs.DFSState()
dfs_state.load_from_file(input_file)
dfs_algo = dfs.DFSAlgorithm(Stack(), dfs_state)
dfs_algo.run()
save_stats(dfs_algo.stats_json(), output_file)
print("Done")

ucs_state = ucs.UCSState()
ucs_state.load_from_file(input_file)
ucs_algo = ucs.UCSAlgorithm(PriorityQueue(), ucs_state)
ucs_algo.run()
save_stats(ucs_algo.stats_json(), output_file)
print("Done")

a_star_state = a_star.AStarState()
a_star_state.load_from_file(input_file)
a_star_algo = a_star.AStarAlgorithm(PriorityQueue(), a_star_state)
a_star_algo.run()
save_stats(a_star_algo.stats_json(), output_file)
path = a_star_algo.trace(a_star_algo.goal_state)[0]
print("Done")


