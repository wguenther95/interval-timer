from enum import Enum


class State(Enum):
    LOW: 0
    HIGH: 1
    WARMUP: 2
    COOLDOWN: 3
    REST: 4


class Routine:
    def __init__(self, name=None, num_cycles=1, warmup=10, cooldown=30):
        self.name = name
        self.num_cycles = num_cycles
        self.warmup = warmup
        self.cooldown = cooldown

        self.cycles = [Cycle()]

    def add_cycle(self, cycle):
        self.cycles.append(cycle)

    def update(self, name, num_cycles, warmup, cooldown):
        self.name = name
        self.num_cycles = num_cycles
        self.warmup = warmup
        self.cooldown = cooldown


class Cycle:
    def __init__(self, sets=10, low_time=10, high_time=60):
        self.sets = sets
        self.low_time = 10
        self.high_time = 60

    def update(self, sets, low_time, high_time):
        self.sets = sets
        self.low_time = low_time
        self.high_time = high_time
