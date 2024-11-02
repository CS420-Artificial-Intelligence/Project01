class State:
    def __init__(self):
        pass
    def load_from_file(self, input_path: str) -> None:
        pass
    def apply_action(self, action: str) -> 'State':
        pass
    def g(self) -> int:
        # cumulative cost
        pass
    def h(self) -> int:
        # heuristic
        pass
    def f(self) -> int:
        # base on a specific algorithm
        pass
    def __hash__(self) -> int:
        pass
    def __eq__(self, other) -> bool:
        pass
    def is_final(self) -> bool:
        pass
    def parent_state(self) -> 'State':
        pass
    def expand(self) -> list['State']:
        pass



