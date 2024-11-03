from best_first_search.state import State
from best_first_search.search import Algorithm
from best_first_search.search_ds import PriorityQueue

s = State()

s.load_from_file('input.txt')

algorithm = Algorithm(PriorityQueue(), s)

goal_state = algorithm.run()

tr = algorithm.trace(goal_state)

print(tr)

algorithm.print_stats('output.txt')