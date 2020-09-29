import time
from enum import Enum


class TimerObject:
    def __init__(self):
        self.start_time = None


class State(Enum):
    ACTIVE = 0
    REST = 1
