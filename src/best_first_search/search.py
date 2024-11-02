from best_first_search.search_ds.search_ds import SearchDataStructure
from best_first_search.state import State


class Algorithm:
    def __init__(self, search_ds: SearchDataStructure, initial_state: State, expand_goal: bool = True):
        self.search_ds = search_ds
        self.search_ds.push(initial_state)
        self.expand_goal = expand_goal
        self.reached = dict()
        self.reached[initial_state] = 0
        self.expanded = set()

    def expand(self, state: State):
        return state.expand()

    def run(self):
        self.nodes_generated = 1
        while not self.search_ds.is_empty():
            current_state = self.search_ds.pop()
            if self.expand_goal and current_state.is_goal():
                return current_state
            if current_state.f() != self.reached[current_state]:
                continue
            self.expanded.add(current_state)
            for state in self.expand(current_state):
                if not self.expand_goal and state.is_goal():
                    return state
                if state not in self.expanded:
                    if state not in self.reached or state.f() < self.reached[state]:
                        if state not in self.reached:
                            self.nodes_generated += 1
                        self.reached[state] = state.f()
                        self.search_ds.push(state)
        return None

