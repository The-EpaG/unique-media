import json
import os

from util.const import JSON_FILE
from util.state import State

class StateManager:
    def __init__(self) -> None:
        self.state:State = None 

    def _import_json_data(self) -> State:
        if not os.path.exists(JSON_FILE):
            self.state = State()
            return
        
        with open(JSON_FILE, "r") as json_file:
            self.state = State().from_dict(json.load(json_file))

    def _export_json_data(self) -> None:
        with open(JSON_FILE, "w") as json_file:
            json.dump(self.state.to_dict(), json_file)

    def _get_step(self) -> int:
        if self.state == None:
            self._import_json_data()

        return self.state.step

    def _set_step(self, step:int) -> None:
        self.state.step = step

    def should_start(self, step:int, should_exist=True) -> bool:
        if (should_exist and not os.path.exists(JSON_FILE)) or \
           (not should_exist and os.path.exists(JSON_FILE)):
            return False
        
        should_continue = self._get_step() < step
        self._set_step(step)

        return should_continue
    
    def get_state(self) -> dict:
        if self.state == None:
            self._import_json_data()
        
        return self.state.state

    def set_state(self, state) -> None:
        self.state.state = state
        self._export_json_data()