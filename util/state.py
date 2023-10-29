from util.const import STATE_INDEX, STEP_INDEX


class State():
    def __init__(self, step=-1, state={}) -> None:
        self.step = step
        self.state = state
     

    def from_dict(self, dict:dict) -> None:
        self.step = dict[STEP_INDEX]
        self.state = dict[STATE_INDEX]
        return self
    
    def to_dict(self) -> dict:
        return {
            STEP_INDEX: self.step,
            STATE_INDEX: self.state
        }