from algorithm.search_ds.search_ds import SearchDataStructure
import timeit
import tracemalloc


class Algorithm:
    def __init__(self, search_ds: SearchDataStructure, initial_state, expand_goal: bool = True):
        self.search_ds = search_ds
        self.search_ds.push(initial_state)
        self.expand_goal = expand_goal
        self.reached = dict()
        self.reached[initial_state] = initial_state.f()
        self.expanded = set()
        self.nodes_generated = 0
        self.time = 0
        self.memory = 0
        self.goal_state = None
        self.algorithm_name = 'Best First Search'

    def expand(self, state):
        return state.expand()

    def run(self):
        start_time = timeit.default_timer()
        tracemalloc.start()
        try:
            while not self.search_ds.is_empty():
                current_state = self.search_ds.pop()
                if self.expand_goal and current_state.is_goal():
                    self.goal_state = current_state
                    return current_state
                if current_state.f() != self.reached[current_state]:
                    continue
                self.expanded.add(current_state)
                for state in self.expand(current_state):
                    if not self.expand_goal and state.is_goal():
                        self.goal_state = state
                        return state
                    if state not in self.expanded:
                        if state not in self.reached or state.f() < self.reached[state]:
                            self.reached[state] = state.f()
                            self.search_ds.push(state)
            self.goal_state = None
            return None
        finally:
            self.nodes_generated = len(self.reached)
            self.time = timeit.default_timer() - start_time
            self.memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
            tracemalloc.stop()


    def trace(self, state):
        # str -> action
        action = []
        steps = state.map.number_moved
        weight = state.map.weight_moved
        tot_cost = state.g()
        while state is not None:
            action.append(state.input_path)
            state = state.parent_state
        action = action[:-1]

        action = ''.join(action[::-1])

        return action, steps, weight, tot_cost

    def stats_json(self):
        return {
            'strategy': self.algorithm_name,
            'steps': self.goal_state.map.number_moved,
            'weight': self.goal_state.map.weight_moved,
            'node': self.nodes_generated,
            'time(ms)': self.time * 1000,
            'memory(MB)': self.memory,
            'solution': self.trace(self.goal_state)[0],
        }
    def print_stats(self, file_name: str):
        with open(file_name, 'w') as f:
            f.write(f'Nodes generated: {self.nodes_generated}\n')
            f.write(f'Time: {self.time}s\n')
            f.write(f'Memory: {self.memory}MB\n')
            f.write(f'Expanded nodes: {len(self.expanded)}\n')
            tracing = self.trace(self.goal_state)
            f.write(f'Path: {tracing[0]}\n')
            f.write(f'Step: {tracing[1]}\n')
            f.write(f'Weight: {tracing[2]}\n')
            f.write(f'Total cost: {tracing[3]}\n')
